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
    
@app.route('/')
def hello_world():
    return 'Hello, World!'
