# models.py 

from app import db


class Tablets(db.Model):
    __tablename__ = "tablets"

    tabletId = db.Column(db.Integer, primary_key=True)
    tabletname = db.Column(db.String)
    tabletcost = db.Column(db.Integer)
    tabletquantity = db.Column(db.Integer)

    


class Orders(db.Model):
    """"""
    __tablename__ = "orders"

    orderId = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    productId = db.Column(db.Integer, db.ForeignKey("tablets.tabletId"))
    ordercost = db.Column(db.Integer)
    productname = db.Column(db.String)