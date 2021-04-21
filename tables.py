from flask_table import Table, Col,LinkCol

class Results(Table):
    tabletId = Col('TabletId',show=False)
    tabletname = Col('TabletName')
    tabletcost = Col('TabletCost')
    edit = LinkCol('ADDtoCART', 'add', url_kwargs=dict(id='tabletId'))
    
class Details(Table):
    productId = Col('productId',show=False)
    orderId = Col('OrderId')
    quantity = Col('Tabletquantity')
    ordercost = Col('TabletCost')
    productname = Col('Tabletname')
    delete = LinkCol('DeletefromCART', 'delete', url_kwargs=dict(id='orderId'))  
    returnback = LinkCol('Exit', 'returnback',url_kwargs=dict(id='orderId'))
