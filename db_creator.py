# db_creator.py

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///healthcare.db', echo=True)
Base = declarative_base()


class Tablets(Base):
    __tablename__ = "tablets"

    tabletId = Column(Integer, primary_key=True)
    tabletname = Column(String)
    tabletcost = Column(Integer)
    tabletquantity = Column(Integer)

    def __init__(self, tabletname, tabletcost, tabletquantity):
        """"""
        self.tabletname = tabletname
        self.tabletcost = tabletcost
        self.tabletquantity = tabletquantity

class Orders(Base):
    """"""
    __tablename__ = "orders"

    orderId = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    ordercost = Column(Integer)
    productId = Column(Integer, ForeignKey("tablets.tabletId"))
    productname = Column(String)
        
    def __init__(self, quantity, ordercost,productname):
        """"""
        self.quantity = quantity
        self.ordercost = ordercost
        self.productname = productname
    
# create tables
Base.metadata.create_all(engine)