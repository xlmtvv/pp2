import csv
import psycopg2
from db import insert_data, query_data, delete_data, update_data, enter_data, upload_csv
from db import get_records_by_pattern, insert_or_update_user, insert_many_users, query_data_with_pagination, delete_data_by_username_or_phone


# Connect to your postgres DB
conn = psycopg2.connect("postgres://pp2_db_test_user:lfFfLH7HjK2ivnEzcN1ZokpgdhFi3WEZ@dpg-cohofjtjm4es739ccgn0-a.oregon-postgres.render.com/pp2_db_test", sslmode='require')
# Open a cursor to perform database operations
cur = conn.cursor()



userlist = [
    ("No", "No", "7017017012"), 
    ("New", "User", "0987654721"),
    ("User", "Neww", "1431231234"),
    ("Hello", "World", "3213993214")
]

# insert_many_users(userlist)

# get_records_by_pattern("Te")
insert_or_update_user("New", "User", "12345678")


# upload_csv("./numbers.csv")
query_data()