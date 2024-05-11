import sqlite3
from faker import Faker
import secrets

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

fake = Faker()

orders_data = []
inventory_data = []

for _ in range(15):
    order_data = {
        'order_date': fake.date_between(start_date='-1y', end_date='today'),
        'order_number': fake.random_int(min=100000, max=999999),
        'order_email': fake.email(),
        'color': fake.color_name(),
        'size': secrets.SystemRandom().randint(10, 30),
        'status': fake.random_element(elements=('shipped', 'order pending', 'delivered'))
    }
    orders_data.append(order_data)
    for _ in range(secrets.SystemRandom().randint(1, 30)):
        inventory_data.append({
            'size': order_data['size'],
            'color': fake.color_name(),
            'quantity': secrets.SystemRandom().randint(10, 30),
            'description': fake.word(),
            'is_active': fake.boolean(),
            'is_featured': fake.boolean(),
            'type': fake.random_element(elements=('T-Shirt', 'Shirt', 'Pants', 'Shoes'))
        })

for order_data in orders_data:
    c.execute("INSERT INTO consumers_order (order_date, order_number, order_email, color, size, status, created, modified, order_code) VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'), ?)",
              (order_data['order_date'], order_data['order_number'], order_data['order_email'], order_data['color'], order_data['size'], order_data['status'],"ORD"+order_data['order_number'].__str__()))

for inventory_data in inventory_data:
    c.execute("INSERT INTO products_inventory (size, color, quantity, created, modified, type) VALUES (?, ?, ?, datetime('now'), datetime('now'), ?)",
              (inventory_data['size'], inventory_data['color'], inventory_data['quantity'], inventory_data['type']))

conn.commit()
conn.close()
