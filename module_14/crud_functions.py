import sqlite3


def initiate_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, price INTEGER NOT NULL, photo TEXT''')
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    products = c.fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT title, price FROM products WHERE id = ?", (product_id,))
    product_info = c.fetchone()
    conn.close()
    return product_info
