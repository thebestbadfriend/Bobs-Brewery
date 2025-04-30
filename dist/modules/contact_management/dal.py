from core.dal import BreweryDBAccessor

bda = BreweryDBAccessor()


def insert_company(company_name):
    query = rf"insert into companies (name) values ('{company_name}')"
    bda.execute_db_command(query)

    company_id = get_company_id_by_name(company_name)
    insert_contact(company_id=company_id)
    sync_contact_id_to_contact(company_id=company_id)


def insert_person(first_name, last_name, nickname, suffix):
    query = rf"""insert into people(first_name, last_name, nickname, suffix)
                 values('{first_name}', '{last_name}', '{nickname}', '{suffix}')"""
    bda.execute_db_command(query)

    person_id = get_person_id_by_name(first_name, last_name, nickname, suffix)
    insert_contact(person_id=person_id)
    sync_contact_id_to_contact(person_id=person_id)


def insert_contact(company_id = None, person_id = None):
    id = company_id if company_id is not None else person_id
    column = 'company_id' if company_id is not None else 'person_id'

    query = rf"insert into contacts ({column}) values ({id})"
    bda.execute_db_command(query)


def get_company_id_by_name(company_name):
    query = rf"select id from companies where name = '{company_name}'"
    return bda.execute_db_command(query)[0][0]


def get_person_id_by_name(first_name, last_name, nickname, suffix):
    query = rf"""select id
                 from people
                 where first_name = '{first_name}'
                 and last_name = '{last_name}'
                 and nickname = '{nickname}'
                 and suffix = '{suffix}'"""
    return bda.execute_db_command(query)[0][0]


def get_contact_id_by_person_id(person_id):
    query = rf"select id from contacts where person_id = {person_id}"
    return bda.execute_db_command(query)[0][0]


def get_contact_id_by_company_id(company_id):
    query = rf"select id from contacts where company_id = {company_id}"
    return bda.execute_db_command(query)[0][0]


def sync_contact_id_to_contact(person_id = None, company_id = None):
    if person_id is not None:
        contact_id = get_contact_id_by_person_id(person_id)
        query = rf'''update people
                     set contact_id = {contact_id}
                     where id = {person_id}'''
    elif company_id is not None:
        contact_id = get_contact_id_by_company_id(company_id)
        query = rf'''update companies
                     set contact_id = {contact_id}
                     where id = {company_id}'''
    else:
        raise Exception('person_id or company_id must be specified')

    bda.execute_db_command(query)
