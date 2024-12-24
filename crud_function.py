import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def add_product(title, description, price):
    cursor.execute(f'''INSERT INTO Products(title, description, price) VALUES('{title}', '{description}', '{price}')''')
    connection.commit()

initiate_db()

# add_product('Витамин A', 'Описание товара Витамин A', 100)
# add_product('Витамин B', 'Описание товара Витамин B', 200)
# add_product('Витамин С', 'Описание товара Витамин C', 300)
# add_product('Витамин D', 'Описание товара Витамин D', 400)

