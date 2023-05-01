import sqlite3

def create_connection(db_name):
    conect = None
    try:
        conect = sqlite3.connect(db_name)
        return conect
    except sqlite3.Error as error:
        print(error)

def create_table(connect, sql):
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def create_product(connect, product: tuple):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)
        '''
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as error:
        print(error)

def update_quantity(connect, product: tuple):
    try:
        sql = '''update products set quantity = ? where id = ?
        '''
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as error:
        print(error)

def update_price(connect, product: tuple):
    try:
        sql = '''update products set price = ? where id = ?
        '''
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as error:
        print(error)

def delete_product(connect, id):
    try:
        sql = '''delete from products where id = ?
        '''
        cursor = connect.cursor()
        cursor.execute(sql, (id,))
        connect.commit()
    except sqlite3.Error as error:
        print(error)

def select_all_products(connect):
    try:
        sql = '''select * from products
        '''
        cursor = connect.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_by_price_and_quantity(connect, limit):
    try:
        sql = '''select * from products where price < ? and quantity > ?
        '''
        cursor = connect.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def search_by_word(connect, word):
    try:
        sql = '''select * from products where product_title like ?
        '''
        cursor = connect.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


database = r'hw.db'

vizof = create_connection(database)

sql_create_products_table = '''
create table products (
id integer primary key autoincrement,
product_title varchar(200) not null,
price  double(10, 2) not null default 0.0,
quantity integer(5) not null default 0
)
'''

create_table(vizof, sql_create_products_table)
create_product(vizof, ('помидор', 80.5, 10))
create_product(vizof, ('банан', 90, 10))
create_product(vizof, ('яблоко', 56.5, 10))
create_product(vizof, ('грушы', 100, 10))
create_product(vizof, ('огурец', 33, 10))
create_product(vizof, ('вишня', 13, 7))
create_product(vizof, ('черешня', 33.33, 10))
create_product(vizof, ('картошка', 80.10, 10))
create_product(vizof, ('моковка', 80.5, 10))
create_product(vizof, ('апельсин', 80.5, 10))
create_product(vizof, ('лимон', 67.45, 10))
create_product(vizof, ('перец', 23.6, 10))
create_product(vizof, ('слива', 87, 10))
create_product(vizof, ('клубника', 80.5, 10))
create_product(vizof, ('персик', 80.5, 10))
update_quantity(vizof, (13, 7))
update_price(vizof, (33.33, 10))
delete_product(vizof, 2)
select_all_products(vizof)
select_by_price_and_quantity(vizof, (100, 5))
search_by_word(vizof, 'огурец')


vizof.close()