import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()



    # Создать новую таблицу с полем image_path для хранения локального пути к изображению
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            image_path TEXT  -- Поле для локального пути к изображению
        )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance INTEGER NOT NULL
                      )''')


    conn.commit()
    conn.close()

def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    balance = 1000
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
               (username, email, age, balance))
    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')  # Get all records, including image_url
    products = cursor.fetchall()

    conn.close()
    return products
#
# def insert_sample_products():
#     conn = sqlite3.connect('products.db')
#     cursor = conn.cursor()
#
#     # Добавляем продукты с локальными путями к изображениям
#     products = [
#         ('Product1', 'Описание 1', 100, 'images/product1.jpg'),
#         ('Product2', 'Описание 2', 200, 'images/product2.jpg'),
#         ('Product3', 'Описание 3', 300, 'images/product3.jpg'),
#         ('Product4', 'Описание 4', 400, 'images/product4.jpg')
#     ]
#
#     cursor.executemany('INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)', products)
#
#     conn.commit()
#     conn.close()
# insert_sample_products()

