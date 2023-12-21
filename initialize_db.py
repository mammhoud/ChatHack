from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection
engine = create_engine('sqlite:///../../db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

# Define the ORM model classes
Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(String)
    order_number = Column(Integer)
    order_email = Column(String)
    color = Column(String)
    size = Column(Integer)
    status = Column(String)
    

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    color = Column(String)

# Create the tables
Base.metadata.create_all(engine)

# Insert data into the tables
orders_data = [
    {'order_date': '2023-11-05', 'order_number': 123456, 'order_email': 'example@valu.com', 'color': 'blue', 'size': 9, 'status': 'shipped'},
    {'order_date': '2023-12-05', 'order_number': 123457, 'order_email': 'me@saws.com', 'color': 'black', 'size': 10, 'status': 'order pending'},
    {'order_date': '2023-11-25', 'order_number': 123458, 'order_email': 'me@gmail.com', 'color': 'gray', 'size': 11, 'status': 'delivered'},
    {'order_date': '2023-12-15', 'order_number': 123460, 'order_email': 'mahmoud.mcrm@gmail.com', 'color': 'blue', 'size': 7, 'status': 'order pending'},
    {'order_date': '2023-12-25', 'order_number': 123461, 'order_email': 'mostafa.emad@gmail.com', 'color': 'black', 'size': 8, 'status': 'order pending'}
]

inventory_data = [
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 25, 'color': 'red'},
        {'size': 25, 'color': 'red'},
        {'size': 25, 'color': 'red'},
        {'size': 25, 'color': 'red'},
        {'size': 22, 'color': 'red'},
        {'size': 22, 'color': 'red'},
        {'size': 22, 'color': 'red'},
        {'size': 22, 'color': 'red'},
        {'size': 22, 'color': 'red'},
        {'size': 22, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 20, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 24, 'color': 'red'},
        {'size': 26, 'color': 'red'},
        {'size': 26, 'color': 'red'},
        {'size': 26, 'color': 'red'},
        {'size': 26, 'color': 'red'},


]

for order_data in orders_data:
    order = Order(**order_data)
    session.add(order)

for inventory_data in inventory_data:
    inventory = Inventory(**inventory_data)
    session.add(inventory)

# Commit the changes
session.commit()

# Close the session
session.close()



# import sqlite3
# conn = sqlite3.connect('../../db.sqlite3')

# c = conn.cursor()

# # Create table
# c.execute('''CREATE TABLE orders
#               (text, trans text, symbol text, qty real, price real)''')


# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2016-01-05','BUY','RHAT',100,35.14)")

# # EXISTING ORDERS
# # Create table
# c.execute('''CREATE TABLE orders
#              (order_date, order_number, order_email, color, size, status)''')

# # data to be added
# purchases = [('2023-11-05',123456,'example@valu.com','blue', 9, 'shipped'),
#              ('2023-12-05',123457,'me@saws.com','black', 10, 'order pending'),
#              ('2023-11-25',123458,'me@gmail.com','gray', 11, 'delivered'),
#                 ('2023-12-15',123460,'mahmoud.mcrm@gmail.com','blue', 7, 'order pending'),
#                 ('2023-12-25',123461,'mostafa.emad@gmail.com','black', 8, 'order pending'),

#             ]

# # add data
# c.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', purchases)

# # AVAILABLE INVENTORY
# # Create table
# c.execute('''CREATE TABLE inventory
#              (size, color)''')

# # data to be added
# inventory = [(1000000, 'blue'),
#              (1000000, 'yellow'),
#              (1000000, 'gray'),
#              (1000000, 'green'),
#              (1000000, 'white'),
#             ]

# # add data
# c.executemany('INSERT INTO inventory VALUES (?,?)', inventory)


# # Save (commit) the changes
# conn.commit()

# # end connection
# conn.close()