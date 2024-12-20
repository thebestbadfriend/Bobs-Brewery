import brewery_db_accessor as bda
import load_database as ldb

csv_folder = r'C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\data'


def populate_companies():
    print('Populating companies')

    companies_csv = csv_folder + r'\companies.csv'
    with open(companies_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_name = spline[1]        #.replace("'", "''")

            bda.execute_db_command(f"insert into companies(name) values ('{company_name}')")

            results = bda.execute_db_command(f"select id from companies where name = '{company_name}'")
            if results:
                company_id = results[0][0]
                bda.execute_db_command(f"""insert into contacts(company_id) values({company_id})""")

                results = bda.execute_db_command(f"select contact_id from contacts where company_id = '{company_id}'")
                if results:
                    contact_id = results[0][0]
                    bda.execute_db_command(f"""update companies
                                               set contact_id = '{contact_id}'
                                               where id = '{company_id}'""")
    print('Companies populated')


def populate_people():
    print('Populating people')
    people_csv = csv_folder + r'\people.csv'
    with open(people_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')

            first_name = spline[1]      #.replace("'", "''")
            last_name = spline[2]       #.replace("'", "''")
            suffix = spline[3]       #.replace("'", "''")
            nickname = spline[4]       #.replace("'", "''")

            bda.execute_db_command(f"""insert into people (first_name, last_name, suffix, nickname)
                                       values ('{first_name}', '{last_name}', '{suffix}', '{nickname}')""")

            results = bda.execute_db_command(f"""select id from people
                                                 where first_name = '{first_name}'
                                                 and last_name = '{last_name}'""")
            if results:
                person_id = results[0][0]
                bda.execute_db_command(f"insert into contacts(person_id) values({person_id})")

                results = bda.execute_db_command(f"""select contact_id
                                                     from contacts
                                                     where person_id = '{person_id}'""")
                if results:
                    contact_id = results[0][0]
                    bda.execute_db_command(f"update people set contact_id = '{contact_id}' where id = '{person_id}'")
    print('People populated')


def populate_addresses():
    print('Populating addresses')
    addresses_csv = csv_folder + r'\addresses.csv'
    with open(addresses_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            street_address = spline[1]  #.replace("'", "''")
            po_box = spline[2]          #.replace("'", "''")
            city = spline[3]            #.replace("'", "''")
            state = spline[4]           #.replace("'", "''")
            zip_code = spline[5]        #.replace("'", "''")

            bda.execute_db_command(f"""insert into addresses (street_address, po_box, city, state, zip_code)
                                       values ('{street_address}', '{po_box}', '{city}', '{state}', '{zip_code}')""")
    print('Addresses populated')


def populate_contacts_addresses():
    print('Populating contacts addresses')
    contact_details_csv = csv_folder + r'\contacts.csv'
    with open(contact_details_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_id = spline[0]
            person_id = spline[1]
            address_id = spline[7]

            if address_id:
                if company_id:
                    query = rf'select contact_id from contacts where company_id = {company_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        company_contact_id = results[0][0]
                        query = rf"""insert into contacts_addresses(contact_id, address_id)
                                     values({company_contact_id}, {address_id}) on conflict do nothing"""
                        bda.execute_db_command(query)

                if person_id:
                    query = rf'select contact_id from contacts where person_id = {person_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        person_contact_id = results[0][0]
                        query = rf"""insert into contacts_addresses(contact_id, address_id)
                                     values({person_contact_id}, {address_id}) on conflict do nothing"""
                        bda.execute_db_command(query)

    print('Contacts addresses populated')


def populate_email_addresses():
    print('Populating email addresses')
    email_addresses_csv = csv_folder + r'\email_addresses.csv'
    with open(email_addresses_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            email_address = spline[1]       #.replace("'", "''")

            bda.execute_db_command(f"insert into email_addresses (email_address) values ('{email_address}')")
    print('Email addresses populated')


def populate_contacts_email_addresses():
    print('Populating contacts email addresses')
    contact_details_csv = csv_folder + r'\contacts.csv'
    with open(contact_details_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_id = spline[0]
            person_id = spline[1]
            email_address_id = spline[6]

            if email_address_id:
                if company_id:
                    query = rf'select contact_id from contacts where company_id = {company_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        email_address_contact_id = results[0][0]
                        query = rf"""insert into contacts_email_addresses(contact_id, email_address_id)
                                     values ('{email_address_contact_id}', '{email_address_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

                if person_id:
                    query = rf'select contact_id from contacts where person_id = {person_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        email_address_contact_id = results[0][0]
                        query = rf"""insert into contacts_email_addresses(contact_id, email_address_id)
                                     values ('{email_address_contact_id}', '{email_address_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)



    print('Contacts email addresses populated')


def populate_phone_numbers():
    print('Populating phone numbers')
    phone_numbers_csv = csv_folder + r'\phone_numbers.csv'
    with open(phone_numbers_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            phone_number = spline[1]        #.replace("'", "''")

            bda.execute_db_command(f"insert into phone_numbers (phone_number) values ('{phone_number}')")
    print('Phone numbers populated')


def populate_contacts_phone_numbers():
    print('Populating contacts phone numbers')
    contact_details_csv = csv_folder + r'\contacts.csv'
    with open(contact_details_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_id = spline[0]
            person_id = spline[1]
            primary_phone_number_id = spline[2]
            secondary_phone_number_id = spline[3]

            if primary_phone_number_id:
                if company_id:
                    query = rf'select contact_id from contacts where company_id = {company_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        phone_number_contact_id = results[0][0]
                        query = rf"""insert into contacts_phone_numbers(contact_id, phone_number_id)
                                     values ('{phone_number_contact_id}', '{primary_phone_number_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

                if person_id:
                    query = rf'select contact_id from contacts where person_id = {person_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        phone_number_contact_id = results[0][0]
                        query = rf"""insert into contacts_phone_numbers(contact_id, phone_number_id)
                                     values ('{phone_number_contact_id}', '{primary_phone_number_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

            if secondary_phone_number_id:
                if company_id:
                    query = rf'select contact_id from contacts where company_id = {company_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        phone_number_contact_id = results[0][0]
                        query = rf"""insert into contacts_phone_numbers(contact_id, phone_number_id)
                                     values ('{phone_number_contact_id}', '{secondary_phone_number_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

                if person_id:
                    query = rf'select contact_id from contacts where person_id = {person_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        phone_number_contact_id = results[0][0]
                        query = rf"""insert into contacts_phone_numbers(contact_id, phone_number_id)
                                     values ('{phone_number_contact_id}', '{secondary_phone_number_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

    print('Contacts phone numbers populated')


def populate_fax_numbers():
    print('Populating fax numbers')
    fax_numbers_csv = csv_folder + r'\fax_numbers.csv'
    with open(fax_numbers_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            fax_number = spline[1]      #.replace("'", "''")

            bda.execute_db_command(f"insert into fax_numbers (fax_number) values ('{fax_number}')")
    print('Fax numbers populated')


def populate_contacts_fax_numbers():
    print('Populating contacts fax numbers')
    contact_details_csv = csv_folder + r'\contacts.csv'
    with open(contact_details_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_id = spline[0]
            person_id = spline[1]
            fax_number_id = spline[4]

            if fax_number_id:
                if company_id:
                    query = rf'select contact_id from contacts where company_id = {company_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        fax_number_contact_id = results[0][0]
                        query = rf"""insert into contacts_fax_numbers(contact_id, fax_number_id)
                                     values ('{fax_number_contact_id}', '{fax_number_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

                if person_id:
                    query = rf'select contact_id from contacts where person_id = {person_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        fax_number_contact_id = results[0][0]
                        query = rf"""insert into contacts_fax_numbers(contact_id, fax_number_id)
                                     values ('{fax_number_contact_id}', '{fax_number_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

    print('Contacts fax numbers populated')


def populate_websites():
    print('Populating websites')
    websites_csv = csv_folder + r'\websites.csv'
    with open(websites_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            url = spline[1]     #.replace("'", "''")

            bda.execute_db_command(f"insert into websites (url) values ('{url}')")
    print('Websites populated')


def populate_contacts_websites():
    print('Populating contacts websites')
    contact_details_csv = csv_folder + r'\contacts.csv'
    with open(contact_details_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_id = spline[0]
            person_id = spline[1]
            website_id = spline[5]

            if website_id:
                if company_id:
                    query = rf'select contact_id from contacts where company_id = {company_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        website_contact_id = results[0][0]
                        query = rf"""insert into contacts_websites(contact_id, website_id)
                                     values ({website_contact_id}, '{website_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

                if person_id:
                    query = rf'select contact_id from contacts where person_id = {person_id}'
                    results = bda.execute_db_command(query)
                    if results:
                        website_contact_id = results[0][0]
                        query = rf"""insert into contacts_websites(contact_id, website_id)
                                     values ('{website_contact_id}', '{website_id}')
                                     on conflict do nothing"""
                        bda.execute_db_command(query)

    print('Contacts websites populated')


def populate_people_companies():
    print('Populating people companies')
    contact_details_csv = csv_folder + r'\contacts.csv'
    with open(contact_details_csv, 'r', newline='') as file:
        for line in file:
            spline = line.strip().replace("'", "''").split(',')
            company_id = spline[0]
            person_id = spline[1]

            if person_id:
                if company_id:
                    query = rf"""insert into people_companies(person_id, company_id)
                                 values ('{person_id}', '{company_id}')
                                 on conflict do nothing"""
                    bda.execute_db_command(query)

    print('People companies populated')


def main():
    bda.drop_database()
    ldb.load()

    populate_companies()
    populate_people()

    populate_addresses()
    populate_email_addresses()
    populate_phone_numbers()
    populate_fax_numbers()
    populate_websites()

    populate_people_companies()

    populate_contacts_addresses()
    populate_contacts_email_addresses()
    populate_contacts_phone_numbers()
    populate_contacts_fax_numbers()
    populate_contacts_websites()


if __name__ == "__main__":
    main()
