import time
import psycopg2
from sqlalchemy.exc import SQLAlchemyError

from review import Review


class ReviewModel:
    def __init__(self, session):
        self.session = session

    def generate_review(self, number):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        conn.autocommit = True
        cursor = conn.cursor()
        query = 'with r_review as (select (md5(random()::text)) as id, '\
				f'(trunc(1+random()*5)) as rating from generate_series(1,{number})) , '\
                'g_review as (select rating, row_number() over (order by id desc) '\
                'as rn from r_review), '\
                f'r_product as (select p.id from generate_series(1,{number}), product as p '\
                f'order by random() limit {number}), '\
                'g_product as (select id, row_number() over (order by random()) as rn from r_product), '\
				f'r_customer as (select c.email from generate_series(1,{number}), customer as c '\
                f'order by random() limit {number}), '\
                'g_customer as (select email, row_number() over (order by random()) as rn from r_customer) '\
                'insert into review (rating, product_id, customer_email) '\
                'select r.rating, p.id, c.email from g_review as r, g_product as p, g_customer as c '\
				'where r.rn=p.rn and c.rn=r.rn'
        start = time.time()
        cursor.execute(query)
        finish = time.time()
        conn.close()
        return finish - start

    def select_review(self, _id):
        review = self.session.query(Review).filter(Review.id == _id).first()
        return review

    def select_review_by_product(self, product_id):
        review = self.session.query(Review).filter(Review.product_id == product_id).all()
        return review

    def select_review_by_customer(self, customer_email):
        review = self.session.query(Review).filter(Review.customer_email == customer_email).all()
        return review

    def insert_review(self, rating, product_id, customer_email):
        try:
            review = Review(rating, product_id, customer_email)
            self.session.add(review)
            self.session.commit()
            if id is not None or id != 0:
                return [True, review]
        except SQLAlchemyError as e:
            return [False, e]

    def update_review(self, _id, rating, product_id, customer_email):
        try:
            self.session.query(Review).filter(Review.id == _id). \
                update({Review.rating: rating, Review.product_id: product_id, Review.customer_email: customer_email})
            self.session.commit()
            review = self.select_review(_id)
            return [True, review]
        except SQLAlchemyError as e:
            return [False, e]

    def delete_review(self, _id):
        purchase = self.session.query(Review).filter(Review.id == _id).first()
        self.session.query(Review).filter(Review.id == _id).delete()
        self.session.commit()
        return purchase

    def delete_review_by_product(self, product_id):
        self.session.query(Review).filter(Review.product_id == product_id).delete()
        self.session.commit()

    def delete_review_by_customer(self, customer_email):
        self.session.query(Review).filter(Review.customer_email == customer_email).delete()
        self.session.commit()
