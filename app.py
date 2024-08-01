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
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
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

@app.route('/db_insert')
def db_insert():
    try:
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        conn.commit()
        cur.close()
        conn.close()
        return "Basketball table populated."
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/db_select')
def db_select():
    try:
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Basketball;')
        records = cur.fetchall()
        cur.close()
        conn.close()

        # Create an HTML table from the records
        response = '<table border="1"><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>'
        for row in records:
            response += '<tr>'
            for item in row:
                response += f'<td>{item}</td>'
            response += '</tr>'
        response += '</table>'

        return response
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/db_drop')
def db_drop():
    try:
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        cur.execute('DROP TABLE Basketball;')
        conn.commit()
        cur.close()
        conn.close()
        return "Basketball table dropped."
    except Exception as e:
        return f"An error occurred: {e}"
    
    
@app.route('/')
def hello_world():
    return 'Hello, World!'
