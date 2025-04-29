from core.dal import BreweryDBAccessor

def add_new_company(company_name):
    bda = BreweryDBAccessor()
    query = rf"insert into companies (name) values ('{company_name}')"
    bda.execute_db_command(query)

def create_new_contact(company_id = None, person_id = None):
    id = company_id if company_id is not None else person_id
    column = 'company_id' if company_id is not None else 'person_id'

    query = rf"insert into contacts ({column}) values ({id})"