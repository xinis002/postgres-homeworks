import csv
import psycopg2

import csv
import psycopg2


db_params = {'host': 'localhost', 'database': 'north', 'user': 'postgres','password': '191819'}


def insert_csv_data(csv_file_path, insert_query, data_columns):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with conn.cursor() as cur:
            for row in csv_reader:
                data_to_insert = tuple(row[column] for column in data_columns)
                cur.execute(insert_query, data_to_insert)
            conn.commit()



conn = psycopg2.connect(**db_params)

try:

    insert_csv_data(
        csv_file_path='north_data/employees_data.csv',
        insert_query='INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)',
        data_columns=['employee_id', 'first_name', 'last_name', 'title', 'birth_date', 'notes']
    )


    insert_csv_data(
        csv_file_path='north_data/orders_data.csv',
        insert_query='INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)',
        data_columns=['order_id', 'customer_id', 'employee_id', 'order_date', 'ship_city']
    )

    insert_csv_data(
        csv_file_path='north_data/customers_data.csv',
        insert_query='INSERT INTO customers_data (customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
        data_columns=['customer_id', 'company_name', 'contact_name']
    )
finally:

    conn.close()