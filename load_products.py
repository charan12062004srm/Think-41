
import sqlite3
import pandas as pd

df = pd.read_csv("products.csv")

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY ,
        name TEXT, 
        category TEXT,
        price REAL,
        stock INTEGER 
    )              
''')
df.to_sql("products",conn,if_exists = "replace", index=False)
cursor.execute("SELECT * FROM products LIMIT 5")
rows = cursor.fetchall()
print("\nSample Row from DB:")
for row in rows:
    print(row)
conn.close()