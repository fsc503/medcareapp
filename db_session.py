
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_creator import Tablets
engine = create_engine('sqlite:///healthcare.db', echo=True)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
# Create an tabletstable
tablet_table = Tablets("Dolo","30","10")
#tabletcost = Tablets("30")
#tabletquantity = Tablets("10")
#tablet_table.tablets=[Tablets("30","10")]
                        

# Add the record to the session object
session.add(tablet_table)
# commit the record the database
session.commit()

session.add_all([
    Tablets("acetaminophen","30","10")
    ])
session.commit()