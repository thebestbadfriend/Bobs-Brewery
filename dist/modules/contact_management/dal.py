from core.dal import BreweryDBAccessor

bda = BreweryDBAccessor()


def insert_company(company_name):
    query = rf"insert into companies (name) values ('{company_name}')"
    bda.execute_db_command(query)

    insert_contact(company_id=_get_company_id_by_name(company_name))


def insert_person(first_name, last_name, nickname, suffix):
    query = rf"""insert into people(first_name, last_name, nickname, suffix)
                 values({first_name}, {last_name}, {nickname}, {suffix})"""
    bda.execute_db_command(query)

    insert_contact(person_id=_get_person_id_by_name(first_name, last_name, nickname, suffix))


def insert_contact(company_id = None, person_id = None):
    id = company_id if company_id is not None else person_id
    column = 'company_id' if company_id is not None else 'person_id'

    query = rf"insert into contacts ({column}) values ({id})"
    bda.execute_db_command(query)


def _get_company_id_by_name(company_name):
    query = rf"select id from companies where name = '{company_name}'"
    return bda.execute_db_command(query)[0][0]


def _get_person_id_by_name(first_name, last_name, nickname, suffix):
    query = rf"""select id
                 from people
                 where first_name = '{first_name}'
                 and last_name = '{last_name}'
                 and nickname = '{nickname}'
                 and suffix = '{suffix}'"""
    return bda.execute_db_command(query)[0][0]