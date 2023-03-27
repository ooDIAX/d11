# minimal flask server
# Path: mini-server.py
# Compare this snippet from src/test-db.py:
import logging
import os
import flask
import psycopg2

from dotenv import load_dotenv

app = flask.Flask(__name__)

# main route
@app.route('/')
def index():
    # read environment variables
    load_dotenv()
    # connect to the PostgreSQL server
    logging.info('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(host=os.getenv('POSTGRES_HOST_EXTERNAL'),
                            database=os.getenv('POSTGRES_DB'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'))

    logging.info('Connected.')

    # read products from database
    logging.info('Reading data...')
    cur = conn.cursor()
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()

    # generate html
    html = '<h1>Products</h1>'
    html += '<table>'
    html += '<tr><th>ID</th><th>Name</th><th>Price</th></tr>'
    for row in rows:
        html += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>'
    html += '</table>'

    # close the communication with the PostgreSQL
    cur.close()
    conn.close()
    logging.info('Done.')

    return html
