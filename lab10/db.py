import csv
import psycopg2
from psycopg2 import sql

# Connect to your postgres DB
conn = psycopg2.connect("postgres://pp2_db_test_user:lfFfLH7HjK2ivnEzcN1ZokpgdhFi3WEZ@dpg-cohofjtjm4es739ccgn0-a.oregon-postgres.render.com/pp2_db_test", sslmode='require')
# Open a cursor to perform database operations
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")

# Commit changes
conn.commit()

def insert_data(first_name, last_name, phone):
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            insert_data(row[0], row[1], row[2])

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

def update_data(id, first_name=None, phone=None):
    if first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE id = %s", (first_name, id))
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    conn.commit()

def query_data(filter=None):
    if filter:
        cur.execute("SELECT * FROM phonebook WHERE %s", (filter,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(id):
    cur.execute("DELETE FROM phonebook WHERE id = %s", (id,))
    conn.commit()



insert_data("John", "Doe", "123-456-7890")