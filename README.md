# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.

# Flask Lab - Basketball Database Application

## Overview
This Flask application demonstrates basic interaction with a PostgreSQL database using the `psycopg2` library. The application allows you to create, insert, select, and drop data from a `Basketball` table. The following routes are available:

- **`/db_test`**: Tests the connection to the PostgreSQL database.
- **`/db_create`**: Creates the `Basketball` table if it does not exist.
- **`/db_insert`**: Inserts predefined records into the `Basketball` table.
- **`/db_select`**: Selects and displays all records from the `Basketball` table as an HTML table.
- **`/db_drop`**: Drops the `Basketball` table from the database.
- **`/`**: A simple route that returns a greeting message.

## Dependencies
The application relies on the following Python packages:
- Flask: A lightweight WSGI web application framework.
- psycopg2: A PostgreSQL database adapter for Python.

To install these dependencies, run:

```bash
pip install Flask psycopg2
```

## Database Connection
postgresql://lab_10_postgres_user:PVxDQrWoflMYiIPdyUnUZQvATUReZHKZ@dpg-cqletq08fa8c73aq845g-a/lab_10_postgres

## How To Run
Run the Flask application using the following command:
```bash
flask run
Access the application in your web browser at http://127.0.0.1:5000.
```

## Routes and Usage
* Test Database Connection: Access http://127.0.0.1:5000/db_test to verify the database connection.
* Create Table: Access http://127.0.0.1:5000/db_create to create the Basketball table.
* Insert Data: Access http://127.0.0.1:5000/db_insert to populate the Basketball table with predefined data.
* Select Data: Access http://127.0.0.1:5000/db_select to view all records in the Basketball table.
* Drop Table: Access http://127.0.0.1:5000/db_drop to drop the Basketball table from the database.
* Home Page: Access http://127.0.0.1:5000/ to see a simple greeting message.
