# app1.py
from app import app
from db_setup import init_db, db_session
from forms import TabletSearchFrom,OrderForm,TabletDeleteForm
from flask import flash, render_template, request, redirect #imported flask
from models import Tablets,Orders
from tables import Results,Details
import random

init_db()


@app.route('/', methods=['GET', 'POST']) #first page; to search the tablet from tablet table in healthcare database
def index():
    search = TabletSearchFrom(request.form) #to get the data from tabletsearchform in form.py
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search) #index.html has search box designed in it


@app.route('/results')
def search_results(search): #search has the form from prev page
    results = []
    search_string = search.data['search'] #search_string contains tablet name user searches

    if search_string:
    
        qry = db_session.query(Tablets).filter(
                    Tablets.tabletname.contains(search_string) , Tablets.tabletquantity>0 )
        results = qry.all()
    
    if not results:
        flash('No tablet with such name found! OR  tablet may be outstock!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table) #results displayed in form of table
        

    
def save_order(tablet, form): #from add it is called to add details into order table
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    orderid=int(random.randint(1000,2000))

    orders = Orders() 
    orders.quantity = int(form.quantity.data)
    orders.orderId = orderid
    orders.productId = tablet.tabletId
    orders.productname = tablet.tabletname
    orders.ordercost = tablet.tabletcost*orders.quantity
    tablet.tabletquantity = tablet.tabletquantity-orders.quantity
       
    db_session.add(orders)
    # commit the data to the database
    db_session.commit()
    return orderid   
    
    
@app.route('/item/<int:id>', methods=['GET', 'POST'])
def add(id):
     qry = db_session.query(Tablets).filter(
                Tablets.tabletId==id)
     tablet = qry.first() 
     if tablet:
        form = OrderForm(formdata=request.form, obj=tablet) 
        if request.method == 'POST' and form.validate():
            orderid=save_order(tablet, form)
            return order_details(id,orderid)
        return render_template('add_items.html', form=form) #to display the form to add user details
     else:
        return 'Error loading #{id}'.format(id=tabletId)
'</int:id>'

@app.route('/details')
def order_details(id,orderid):
    details = []
    
    
    if orderid:
    
        qry = db_session.query(Orders).filter(
                Orders.orderId==orderid)
        details = qry.all()

    if not details:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table1 = Details(details)
        table1.border = True
        return render_template('details.html', table1=table1) #displaying the orderid details in table format
        
@app.route('/delete/<int:id>', methods=['GET','DELETE'])
def delete(id): #direct deletion form the order details table
    
    qry = db_session.query(Orders).filter(
        Orders.orderId==id)
    order = qry.first()
    tid = order.productId
    qry = db_session.query(Tablets).filter(
        Tablets.tabletId==tid)
    tablet = qry.first()
    if order:
        
        tablet.tabletquantity = tablet.tabletquantity+order.quantity
            # delete the item from the database
        db_session.delete(order)
        db_session.commit()
        flash('your order is deleted successfully!')
        return redirect('/')
         
       
    else:
       return 'Error deleting #{id}'.format(id=order.orderId)
       
@app.route('/returnback/<int:id>', methods=['GET','POST'])      
def returnback(id): #to exit to first page from order table page
    
    qry = db_session.query(Orders).filter(
        Orders.orderId==id)
    order = qry.first()
    
    if order:
        
        flash('your order is placed successfully!')
        return redirect('/')
         
       
    else:
       return 'Error ordering #{id}'.format(id=orderId)
    
'</int:id>'     
@app.route('/delete_order', methods=['GET', 'POST','DELETE'])   
def delete_order(): #deleting from first page
    
    form = TabletDeleteForm(request.form)
    
    if request.method == 'POST' and form.validate():
        order=Orders()
        delete_details(order,form)
        return redirect('/')
    return render_template('delete_order.html', form=form)
    
def delete_details(order,form):
    
    tablet=Tablets()
    id=int(form.orderid.data)
    qry = db_session.query(Orders).filter(
        Orders.orderId==id)
    order = qry.first()
    if order:
        tid = order.productId
        qry = db_session.query(Tablets).filter(
            Tablets.tabletId==tid)
        tablet = qry.first()
    
    
        tablet.tabletquantity = tablet.tabletquantity+order.quantity
        db_session.delete(order)
        db_session.commit()
        flash('your order is deleted successfully!')
        
    else:
        flash('orderid does not exsit deleting order is unsuccessfully!')
        

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
