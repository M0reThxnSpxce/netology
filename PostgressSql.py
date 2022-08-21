import psycopg2

def create_db(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS customers(
        client_id SERIAL PRIMARY KEY,
        first_name VARCHAR(40),
        last_name VARCHAR(60),
        email VARCHAR(60)
        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        phone VARCHAR(12)
        );""")
    cur.execute("""CREATE table customers_phones (
        client_id integer references customers(client_id),
        phone_id integer references phones(id),
        Constraint cs primary key (client_id, phone_id)
        );""")
    conn.commit()

def add_client(conn, first_name, last_name, email, phones=None):
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s);
    """, (first_name, last_name, email))
    conn.commit()
    cur.execute("SELECT client_id from customers Order By client_id")
    client_id = cur.fetchone()
    conn.commit()
    cur.execute("""
    INSERT INTO phones (phone) VALUES (%s);
    """, (phones))
    conn.commit()
    cur.execute("SELECT phone_id from phones Order By phone_id")
    phone_id = cur.fetchone()
    cur.execute("""
    INSERT INTO customers_phones (client_id, phone_id) VALUES (%s, %s);
    """, (client_id, phone_id))
    conn.commit()

def add_phone(conn, client_id, phone):
    pass

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass

def delete_phone(conn, client_id, phone):
    pass

def delete_client(conn, client_id):
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="clients_db", user="postgres", password="root") as conn:
    print("Меню")
    print("1. Создание структуры БД (Персональная информация о клиентах)")
    print("2. Добавить нового клиента")
    number_menu = int(input(' '))
    if number_menu == 1:
        create_db(conn)
    if number_menu == 2:
        first_name = str(input('Имя клиента: '))
        last_name = str(input('Фамилия клиента: '))
        email = str(input('Email клиента: '))
        phones = str(input('Телефон клиента (при отсутствии - нажмите Enter): '))
        add_client(conn, first_name, last_name, email, phones)

conn.close()