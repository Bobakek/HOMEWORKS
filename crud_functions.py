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

    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')  # Get all records, including image_url
    products = cursor.fetchall()

    conn.close()
    return products
