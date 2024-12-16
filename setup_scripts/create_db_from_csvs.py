import brewery_db_accessor as bda
import load_database as ldb

csv_folder = r'C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\data'


def populate_companies():
    companies_csv = csv_folder + r'\companies.csv'
    with open(companies_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            company_name = spline[1].replace("'", "''")
            bda.execute_db_command(f"insert into companies(name) values ('{company_name}')")


def populate_people():
    people_csv = csv_folder + r'\people.csv'
    with open(people_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            first_name = spline[1].replace("'", "''")
            last_name = spline[2].replace("'","''")
            bda.execute_db_command(f"insert into people (first_name, last_name) values ('{first_name}', '{last_name}')")


def populate_addresses():
    addresses_csv = csv_folder + r'\addresses.csv'
    with open(addresses_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            street_address = spline[1].replace("'", "''")
            po_box = spline[2].replace("'", "''")
            city = spline[3].replace("'", "''")
            state = spline[4].replace("'", "''")
            zip_code = spline[5].replace("'", "''")

            bda.execute_db_command(f"""insert into addresses (street_address, po_box, city, state, zip_code)
                                       values ('{street_address}', '{po_box}', '{city}', '{state}', '{zip_code}')""")


def populate_email_addresses():
    email_addresses_csv = csv_folder + r'\email_addresses.csv'
    with open(email_addresses_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            email_address = spline[1].replace("'", "''")

            bda.execute_db_command(f"insert into email_addresses (email_address) values ('{email_address}')")


def populate_phone_numbers():
    phone_numbers_csv = csv_folder + r'\phone_numbers.csv'
    with open(phone_numbers_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            phone_number = spline[1].replace("'", "''")

            bda.execute_db_command(f"insert into phone_numbers (phone_number) values ('{phone_number}')")


def populate_fax_numbers():
    fax_numbers_csv = csv_folder + r'\fax_numbers.csv'
    with open(fax_numbers_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            fax_number = spline[1].replace("'", "''")

            bda.execute_db_command(f"insert into fax_numbers (fax_number) values ('{fax_number}')")


def populate_websites():
    websites_csv = csv_folder + r'\websites.csv'
    with open(websites_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().split(',')
            website = spline[1].replace("'", "''")

            bda.execute_db_command(f"insert into websites (website) values ('{website}'")


def populate_people_companies():
    pass


def main():
    bda.drop_database()
    ldb.load()
    populate_companies()
    populate_people()
    populate_addresses()
    populate_phone_numbers()
    populate_fax_numbers()
    populate_people_companies()


if __name__ == "__main__":
    main()
