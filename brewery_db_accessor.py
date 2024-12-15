import os
import psycopg2
import subprocess
import sys
import concealed_vars as cv

# Configuration - update these variables
pg_user = cv.DB_USER
pg_password = cv.COMMON_PASS
pg_host = 'localhost'
pg_port = '5432'
db_name = 'bb_contacts'
dump_file = r'C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\sql\bb_contacts_dump.sql'

# Set environment variable for password (optional, if password is needed)
os.environ['PGPASSWORD'] = pg_password


def check_database_exists():
    """Check if the database exists."""
    try:
        conn = psycopg2.connect(
            dbname='postgres',  # Connect to the default 'postgres' database
            user=pg_user,
            host=pg_host,
            port=pg_port
        )
        conn.autocommit = True  # To run the query immediately without needing to commit
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
        exists = cur.fetchone() is not None
        cur.close()
        conn.close()
        return exists
    except psycopg2.Error as e:
        print(f'Error checking database existence: {e}')
        sys.exit(1)


def create_database():
    """Create the database if it doesn't exist."""
    try:
        conn = psycopg2.connect(
            dbname='postgres',  # Connect to the default 'postgres' database
            user=pg_user,
            host=pg_host,
            port=pg_port
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f'CREATE DATABASE {db_name}')
        cur.close()
        conn.close()
        print(f"Database '{db_name}' created successfully.")
    except psycopg2.Error as e:
        print(f'Error creating database: {e}')
        sys.exit(1)


'''
def restore_dump():
    """Restore the dump file into the created database."""
    try:
        restore_command = f'psql -U {pg_user} -d {db_name} -f {dump_file} -h {pg_host} -p {pg_port}'
        subprocess.run(restore_command, check=True, shell=True)
        print(f"Dump file '{dump_file}' has been applied to the database '{db_name}'.")
    except subprocess.CalledProcessError as e:
        print(f'Error restoring dump: {e}')
        sys.exit(1)
'''


def restore_dump():
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
        subprocess.run(restore_command, check=True)
        print(f"Dump file '{dump_file}' has been applied to the database '{db_name}'.")
    except subprocess.CalledProcessError as e:
        print(f'Error restoring dump: {e}')
        sys.exit(1)