from datetime import datetime
import os
import psycopg
import subprocess
import sys
import concealed_vars as cv


class BreweryDBAccessor:
    # Configuration - update these variables
    pg_user = cv.DB_USER
    pg_password = cv.COMMON_PASS
    # pg_host = cv.DB_HOST
    pg_host = "71.31.104.78"
    pg_port = '5432'
    db_name = 'bb_contacts'
    dump_directory = r'C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\dal\dumps'
    dump_file = rf'{dump_directory}\gold_dumps\bb_contacts.gold.20241223.110753.dump'

    # Set environment variable for password (optional, if password is needed)
    os.environ['PGPASSWORD'] = pg_password

    def connect_to_db(self, dbname = db_name):
        conn = psycopg.connect(
            dbname=dbname,  # Connect to the default 'postgres' database
            user=self.pg_user,
            host=self.pg_host,
            port=self.pg_port
        )

        conn.autocommit = True  # To run the query immediately without needing to commit
        return conn

    def execute_db_command(self, query, dbname='bb_contacts'):
        results = None
        try:
            conn = self.connect_to_db(dbname)
            cur = conn.cursor()
            cur.execute(query)

            if query.strip().upper().startswith('SELECT'):
                # check that the results set is not empty
                # an empty results set is a falsey value
                # https://www.psycopg.org/docs/cursor.html#cursor.fetchall
                results = cur.fetchall()
        finally:
            cur.close()
            conn.close()
            return results

    def check_database_exists(self):
        """Check if the database exists."""
        try:
            results = self.execute_db_command(f"""SELECT 1 FROM pg_catalog.pg_database
                                                  WHERE datname = '{self.db_name}'""", dbname = 'postgres')
            return results is not None
        except psycopg.Error as e:
            print(f'Error checking database existence: {e}')
            sys.exit(1)


    def create_database(self):
        """Create the database if it doesn't exist."""
        try:

            self.execute_db_command(f'CREATE DATABASE {self.db_name}', 'postgres')
            print(f"Database '{self.db_name}' created successfully.")
        except psycopg.Error as e:
            print(f'Error creating database: {e}')
            sys.exit(1)

    def restore_dump(self, dump=dump_file):
        """Restore the dump file into the created database."""
        try:
            restore_command = [
                'psql',
                '-U', self.pg_user,
                '-d', self.db_name,
                '-f', dump,
                '-h', self.pg_host,
                '-p', self.pg_port
            ]
            subprocess.run(restore_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"Dump file '{self.dump_file}' has been applied to the database '{self.db_name}'.")
        except subprocess.CalledProcessError as e:
            print(f'Error restoring dump: {e}')
            sys.exit(1)

    def create_dump(self, dump_type = 'unspecified_type'):
        dump_to = rf"{self.dump_directory}\{self.db_name}.{dump_type}.{datetime.now().strftime("%Y%m%d.%H%M%S")}.dump"

        """Restore the dump file into the created database."""
        try:
            pg_dump_command = [
                'pg_dump',
                '-U', self.pg_user,
                '-E', 'utf8',
                '-f', dump_to,
                self.db_name,
            ]

            subprocess.run(pg_dump_command, check=True)
            print(f"Dump file '{dump_to}' created successfully.")

        except subprocess.CalledProcessError as e:
            print(f'Error creating dump: {e}')
            sys.exit(1)

    def drop_database(self, dbname='bb_contacts'):
        self.execute_db_command(f'drop database if exists {dbname}', 'postgres')
