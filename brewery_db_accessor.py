from datetime import datetime
import os
import psycopg
import subprocess
import sys
import concealed_vars as cv

# Configuration - update these variables
pg_user = cv.DB_USER
pg_password = cv.COMMON_PASS
pg_host = 'localhost'
pg_port = '5432'
db_name = 'bb_contacts'
dump_directory = r'C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\sql'
dump_file = rf'{dump_directory}\bb_contacts.schema.20241220.104703.dump'

# Set environment variable for password (optional, if password is needed)
os.environ['PGPASSWORD'] = pg_password


def connect_to_db(dbname):
    conn = psycopg.connect(
        dbname=dbname,  # Connect to the default 'postgres' database
        user=pg_user,
        host=pg_host,
        port=pg_port
    )

    conn.autocommit = True  # To run the query immediately without needing to commit
    return conn


def execute_db_command(query, dbname = 'bb_contacts'):
    try:
        results = None
        conn = connect_to_db(dbname)
        cur = conn.cursor()
        cur.execute(query)

        if query.strip().upper().startswith('SELECT'):
            # check that the results set is not empty
            # an empty results set is a falsey value
            # https://www.psycopg.org/docs/cursor.html#cursor.fetchall
            results = cur.fetchall()

        return results
    finally:
        cur.close()
        conn.close()


def check_database_exists():
    """Check if the database exists."""
    try:
        results = execute_db_command(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'", dbname = 'postgres')
        return results is not None
    except psycopg.Error as e:
        print(f'Error checking database existence: {e}')
        sys.exit(1)


def create_database():
    """Create the database if it doesn't exist."""
    try:

        execute_db_command(f'CREATE DATABASE {db_name}', 'postgres')
        print(f"Database '{db_name}' created successfully.")
    except psycopg.Error as e:
        print(f'Error creating database: {e}')
        sys.exit(1)


def restore_dump(dump = dump_file):
    """Restore the dump file into the created database."""
    try:
        restore_command = [
            'psql',
            '-U', pg_user,
            '-d', db_name,
            '-f', dump_file,
            '-h', pg_host,
            '-p', pg_port
        ]
        subprocess.run(restore_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"Dump file '{dump_file}' has been applied to the database '{db_name}'.")
    except subprocess.CalledProcessError as e:
        print(f'Error restoring dump: {e}')
        sys.exit(1)


def create_dump(dump_type = 'unspecified_type'):
    dump_to = rf"{dump_directory}\{db_name}.{dump_type}.{datetime.now().strftime("%Y%m%d.%H%M%S")}.dump"

    """Restore the dump file into the created database."""
    try:
        pg_dump_command = [
            'pg_dump',
            '-U', pg_user,
            '-E', 'utf8',
            '-f', dump_to,
            db_name,
        ]

        subprocess.run(pg_dump_command, check=True)
        print(f"Dump file '{dump_to}' created successfully.")

    except subprocess.CalledProcessError as e:
        print(f'Error creating dump: {e}')
        sys.exit(1)


def drop_database(dbname='bb_contacts'):
    execute_db_command(f'drop database if exists {dbname}', 'postgres')