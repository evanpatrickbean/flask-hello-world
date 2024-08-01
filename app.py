import psycopg2

from flask import Flask
app = Flask(__name__)


@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        conn.close()
        return "Database Connection Successful."
    except Exception as e:
        return f"An error occurred: {e}"
    
    
@app.route('/db_create')
def db_create():
    try:
        conn = psycopg2.connect("your_db_url_here")
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        return "Basketball table successfully created."
    except Exception as e:
        return f"An error occurred: {e}"
    
    
@app.route('/')
def hello_world():
    return 'Hello, World!'
