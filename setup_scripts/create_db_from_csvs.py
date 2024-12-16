import brewery_db_accessor as bda
import os
import psycopg2

'''
for each normalized csv

grab the contents of the csv
insert each row into the table for that csv
'''
csv_folder = r'C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\data'


def populate_companies():
    companies_csv = csv_folder + r'\companies.csv'

    with open(companies_csv, 'r', newline='') as file:

        for line in file:
            splitline = line.split(',')
            company_name = splitline[1].replace("'", "''")
            bda.execute_db_command(f"insert into companies(name) values ('{company_name}')")




def populate_people():
    pass


def populate_addresses():
    pass


def populate_email_addresses():
    pass


def populate_phone_numbers():
    pass


def populate_fax_numbers():
    pass


def populate_people_companies():
    pass


populate_companies()
