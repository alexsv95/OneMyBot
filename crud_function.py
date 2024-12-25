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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connection.commit()

# Функции для работы с таблицей Products
def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def add_product(title, description, price):
    cursor.execute(f'''INSERT INTO Products(title, description, price) VALUES('{title}', '{description}', '{price}')''')
    connection.commit()


# Функции для работы с таблицей Users
def add_user(username, email, age):
    balance = 1000
    cursor.execute(f'''INSERT INTO Users(username, email, age, balance) VALUES('{username}', '{email}', '{age}', '{balance}')''')
    connection.commit()

def is_included(username):
    list_users = cursor.execute('SELECT username FROM Users')
    for user in list_users:
        if user[0] == username:
            return True
    else:
        return False

initiate_db()

# add_user('User1', 'user1@mail.ru', 25)

# print(is_included('User22'))

# cursor.execute('DELETE FROM Users WHERE id < ?', (10,))
# connection.commit()

# add_product('Витамин A', 'Описание товара Витамин A', 100)
# add_product('Витамин B', 'Описание товара Витамин B', 200)
# add_product('Витамин С', 'Описание товара Витамин C', 300)
# add_product('Витамин D', 'Описание товара Витамин D', 400)

