import logging
import os

import psycopg2
from dotenv import load_dotenv

def main():
    # load environment variables
    load_dotenv()

    # connect to the PostgreSQL server
    logging.info('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(host="localhost",
                            database=os.getenv('POSTGRES_DB'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'))

    logging.info('Connected.')

    # create table products
    logging.info('Creating table...')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS products')
    cur.execute('CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, price float NOT NULL)')

    # make a list of 20 test product names and prices - assuming we have electronics store
    products = [('Iphone 13', 40000.00), ('Iphone 13 Pro', 42000.00), ('Iphone 13 Pro Max', 45000.00), ("Samsung Galaxy S21", 35000.00), ("Samsung Galaxy S21 Ultra", 40000.00), ("Samsung Galaxy S21 Plus", 37000.00), ("OnePlus 9 Pro", 50000.00), ("OnePlus 9", 45000.00), ("OnePlus 9R", 40000.00), ("OnePlus 9T", 45000.00), ("OnePlus Nord 2", 40000.00), ("OnePlus Nord CE 5G", 35000.00), ("OnePlus Nord N200 5G", 30000.00), ("OnePlus Nord N10 5G", 25000.00), ("OnePlus Nord N100", 20000.00), ("OnePlus Nord N10", 15000.00), ("OnePlus Nord N100", 10000.00), ("OnePlus Nord N10", 5000.00), ("OnePlus Nord N100", 2500.00), ("OnePlus Nord N10", 1000.00)]

    # insert a new products
    logging.info('Inserting data...')
    for product in products:
        if product[1] < 40000.00:
            cur.execute(f"INSERT INTO products (name, price) VALUES ('{product[0]}', '{product[1]}')")

    conn.commit()

    # display the products
    logging.info('Displaying data...')
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()
    for row in rows:
        logging.info(row)

    # close the communication with the PostgreSQL
    cur.close()
    conn.close()
    logging.info('Done.')

if __name__ == "__main__":
    format = "SRV: %(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%F-%H-%M-%S")

    main()