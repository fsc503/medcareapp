# forms.py

from wtforms.validators import ValidationError, DataRequired, Length
from wtforms import Form, StringField,TextAreaField
def char_check(form,field):
    if not field.data.isalpha():
        raise ValidationError('kindly enter only characters!')
def integer_check(form,field):
    if not field.data.isdigit():
        raise ValidationError('kindly enter only number!')
class TabletSearchFrom(Form):
    search = StringField(label=('Enter Tablet Name to search:'),validators=[DataRequired(message='*Required')])
    
class OrderForm(Form):
    name= StringField(label=('Enter your Name:'),validators=[DataRequired(),Length(min=5, max=20, message='Kindly check ,Name length must be between 5 and 64 characters!'),char_check])
    address = TextAreaField(label=('Enter your Address:'),validators=[DataRequired(),Length(max=100, message='Kindly check,Address must be upto 100 characters!')])
    phone = StringField(label=('Enter your PhoneNumber:'),validators=[DataRequired(),Length(min=10,max=10, message='kindly chech, phonenumber must be 10 characters!'),integer_check])
    quantity = StringField(label=('Enter Tablet Quantity:'),validators=[DataRequired(message='*Required'),integer_check])
    age= StringField(label=('Enter your Age:'),validators=[DataRequired(),Length(min=1, max=2, message='kindly check,Age must be between 5 to 100!'),integer_check])
    
class TabletDeleteForm(Form):
    orderid = StringField(label=('Enter OrderId:'),validators=[DataRequired(),Length(min=4,max=6, message='Kindly check,orderid must be between 4 to 6 digits!'),integer_check])