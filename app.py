import psycopg2
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Route to test database connection
@app.route('/db_test')
def db_test():
    """
    Test the connection to the PostgreSQL database.

    Returns:
        str: Success message if the connection is successful, 
             error message otherwise.
    """
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        conn.close()  # Close the connection
        return "Database Connection Successful."
    except Exception as e:
        return f"An error occurred: {e}"

# Route to create the Basketball table
@app.route('/db_create')
def db_create():
    """
    Create the 'Basketball' table in the PostgreSQL database if it doesn't already exist.

    Returns:
        str: Success message if the table is created successfully, 
             error message otherwise.
    """
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        
        # Create the Basketball table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        ''')
        
        conn.commit()  # Commit the changes
        cur.close()    # Close the cursor
        conn.close()   # Close the connection
        return "Basketball table successfully created."
    except Exception as e:
        return f"An error occurred: {e}"

# Route to insert data into the Basketball table
@app.route('/db_insert')
def db_insert():
    """
    Insert predefined data into the 'Basketball' table.

    Returns:
        str: Success message if the data is inserted successfully, 
             error message otherwise.
    """
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        
        # Insert data into the Basketball table
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
        
        conn.commit()  # Commit the changes
        cur.close()    # Close the cursor
        conn.close()   # Close the connection
        return "Basketball table populated."
    except Exception as e:
        return f"An error occurred: {e}"

# Route to select and display data from the Basketball table
@app.route('/db_select')
def db_select():
    """
    Select all data from the 'Basketball' table and display it as an HTML table.

    Returns:
        str: HTML table with the records from the Basketball table, 
             or an error message if an error occurs.
    """
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        
        # Execute the SELECT query
        cur.execute('SELECT * FROM Basketball;')
        records = cur.fetchall()
        cur.close()    # Close the cursor
        conn.close()   # Close the connection

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

# Route to drop the Basketball table
@app.route('/db_drop')
def db_drop():
    """
    Drop the 'Basketball' table from the PostgreSQL database.

    Returns:
        str: Success message if the table is dropped successfully, 
             error message otherwise.
    """
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect("postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres")
        cur = conn.cursor()
        
        # Drop the Basketball table
        cur.execute('DROP TABLE Basketball;')
        
        conn.commit()  # Commit the changes
        cur.close()    # Close the cursor
        conn.close()   # Close the connection
        return "Basketball table dropped."
    except Exception as e:
        return f"An error occurred: {e}"

# Route for the home page
@app.route('/')
def hello_world():
    """
    Default route that returns a simple greeting message.

    Returns:
        str: Greeting message.
    """
    return 'Hello World from Evan Bean in 3308'
