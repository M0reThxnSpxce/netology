import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS customers(
            client_id SERIAL PRIMARY KEY,
            first_name VARCHAR(40),
            last_name VARCHAR(60),
            email VARCHAR(60)
            );""")

        cur.execute("""CREATE TABLE IF NOT EXISTS phones(
            id SERIAL PRIMARY KEY,
            client_id INTEGER REFERENCES customers(client_id),
            phone VARCHAR(12)
            );""")
        conn.commit()

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s);
        """, (first_name, last_name, email))
        if not (phones is None):
            with conn.cursor() as cur:
                cur.execute("SELECT client_id from customers Order By client_id")
                client_id = cur.fetchone()
                add_phone(conn, client_id, phones)

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO phones (client_id, phone) VALUES (%s, %s);
        """, (client_id, phones))

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if not (first_name is None):
            cur.execute("""
            UPDATE customers SET first_name=%s WHERE client_id=%s;
            """, (first_name, client_id))

        if not (last_name is None):
            cur.execute("""
            UPDATE customers SET last_name=%s WHERE client_id=%s;
            """, (last_name, client_id))

        if not (email is None):
            cur.execute("""
            UPDATE customers SET email=%s  WHERE client_id=%s;
            """, (email, client_id))

        if not (phones is None):
            cur.execute("""
            UPDATE phones SET phone=%s WHERE client_id=%s;
            """, (phones, client_id))

def delete_phone(conn, client_id, phones=None):
    if not (phones is None):
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM phones WHERE client_id =%s;
            """, (client_id))
    else:
        print("Ошибка: У клиента номер телефона отсутствует.")
def delete_client(conn, client_id, client=None):
    if not (client is None):
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM customers WHERE client_id =%s;
            """, (client_id))
    else:
        print("Ошибка: Такого клиента нет в базе данных.")    


with psycopg2.connect(database="clients", user="postgres", password="root") as conn:
    print("Меню")
    print("1. Создание структуры БД (Персональная информация о клиентах)")
    print("2. Добавить нового клиента")
    print("3. Добавить телефон для существующего клиента")
    print("4. Изменить данные о клиенте")
    print("5. Удалить телефон для существующего клиента")
    print("6. Удалить существующего клиента")
    number_menu = int(input(' '))
    if number_menu == 1:
        create_db(conn)
    elif number_menu == 2:
        first_name = str(input('Имя клиента: '))
        last_name = str(input('Фамилия клиента: '))
        email = str(input('Email клиента: '))
        phones = str(input('Телефон клиента (при отсутствии - нажмите Enter): '))
        add_client(conn, first_name, last_name, email, phones)
    elif number_menu == 3:
        client_id = int(input('Введите номер клиента: '))
        phones = str(input('Телефон клиента: '))
        add_phone(conn, client_id, phones)
    elif number_menu == 4:
        client_id = int(input('Введите номер клиента: '))
        print("--- Изменение данных о клиенте ---")
        first_name = str(input('Имя клиента: '))
        last_name = str(input('Фамилия клиента: '))
        email = str(input('Email клиента: '))
        phones = str(input('Телефон клиента (при отсутствии - нажмите Enter): '))
        change_client(conn, client_id, first_name, last_name, email, phones)
    elif number_menu == 5:
        client_id = int(input('Введите номер клиента: '))
        phone = str(input('Телефон клиента: '))
        with conn.cursor() as cur:
            cur.execute("""SELECT phone FROM phones WHERE client_id=%s AND phone=%s
            """, (client_id, phone))
            phones = cur.fetchone()
        delete_phone(conn, client_id, phones)
    elif number_menu == 6:
        client_id = input('Введите id клиента которого хотите удалить: ')
        last_name = str(input('Введите фамилию клиента которого хотите удалить: '))
        with conn.cursor() as cur:
            cur.execute("""SELECT client_id, last_name FROM customers WHERE client_id=%s AND phone=%s
            """, (client_id, last_name))
            client = cur.fetchone()
        delete_client(conn, client_id, client)

conn.close()