import time
import psycopg2
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from purchase import Purchase


class PurchaseModel:
    def __init__(self, session):
        self.session = session

    def generate_purchase(self, number):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        conn.autocommit = True
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)
        cursor = conn.cursor()
        query = 'with r_date as (select (md5(random()::text)) as id, '\
                f'(timestamp \'2019-01-01 00:00:00\' + random() * (timestamp \'{str(dt_object)}\' - '\
                'timestamp \'2019-01-01 00:00:00\')) as date_time '\
                f'from generate_series(1,{number})), '\
                'g_date as (select date_time, row_number() over (order by d.id desc) as rn from r_date as d), '\
                f'r_product as (select p.id from generate_series(1,{number}), product as p '\
                f'order by random() limit {number}), '\
                'g_product as (select id, row_number() over (order by random()) as rn from r_product) '\
                'insert into purchase (date_time, product_id) '\
                'select d.date_time, p.id from g_date as d, g_product as p '\
                'where d.rn=p.rn'
        start = time.time()
        cursor.execute(query)
        finish = time.time()
        conn.close()
        return finish - start

    def select_purchase(self, _id):
        purchase = self.session.query(Purchase).filter(Purchase.id == _id).first()
        return purchase

    def select_purchase_by_product(self, product_id):
        purchase = self.session.query(Purchase).filter(Purchase.product_id == product_id).all()
        return purchase

    def insert_purchase(self, product_id, date_time):
        try:
            purchase = Purchase(product_id, date_time)
            self.session.add(purchase)
            self.session.commit()
            if id is not None or id != 0:
                return [True, purchase]
        except SQLAlchemyError as e:
            return [False, e]

    def update_purchase(self, _id, product_id, date_time):
        try:
            self.session.query(Purchase).filter(Purchase.id == _id). \
                update({Purchase.product_id: product_id, Purchase.date_time: date_time})
            self.session.commit()
            purchase = self.select_purchase(_id)
            return [True, purchase]
        except SQLAlchemyError as e:
            return [False, e]

    def delete_purchase(self, _id):
        purchase = self.session.query(Purchase).filter(Purchase.id == _id).first()
        self.session.query(Purchase).filter(Purchase.id == _id).delete()
        self.session.commit()
        return purchase

    def delete_purchase_by_product(self, product_id):
        self.session.query(Purchase).filter(Purchase.product_id == product_id).delete()
        self.session.commit()