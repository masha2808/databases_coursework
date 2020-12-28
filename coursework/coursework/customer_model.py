import names
import psycopg2
import time
from random import randint
from customer import Customer


class CustomerModel:
    def __init__(self, session):
        self.session = session

    def generate_customer(self, number):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        conn.autocommit = True
        n = 0
        start = time.time()
        while n < number:
            firstname = names.get_first_name()
            lastname = names.get_last_name()
            email = firstname + lastname + str(randint(0, 10000)) + '@gmail.com'
            cursor = conn.cursor()
            query = 'insert into customer (email, first_name, last_name) '\
                f'values(\'{email}\', \'{firstname}\', \'{lastname}\')'
            cursor.execute(query)
            n += 1
        finish = time.time()
        conn.close()
        return finish - start

    def select_customer(self, email):
        customer = self.session.query(Customer).filter(Customer.email == email).first()
        return customer

    def insert_customer(self, email, first_name, last_name):
        customer = Customer(email, first_name, last_name)
        self.session.add(customer)
        self.session.commit()
        return customer

    def update_customer(self, email, first_name, last_name):
        self.session.query(Customer).filter(Customer.email == email). \
            update({Customer.email: email, Customer.first_name: first_name, Customer.last_name: last_name})
        self.session.commit()
        customer = self.select_customer(email)
        return customer

    def delete_customer(self, email):
        customer = self.session.query(Customer).filter(Customer.email == email).first()
        self.session.query(Customer).filter(Customer.email == email).delete()
        self.session.commit()
        return customer
