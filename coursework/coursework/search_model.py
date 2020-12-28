import psycopg2
import pandas


class SearchModel:

    def search_rating(self, rating1, rating2):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = f'select * from product where rating>{rating1} and rating<{rating2}'
        pandas.set_option("display.max_rows", None, "display.max_columns", None)
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        return data_frame

    def search_date(self, date1, date2):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = f'select * from purchase where date_time>\'{date1}\' and date_time<\'{date2}\''
        pandas.set_option("display.max_rows", None, "display.max_columns", None)
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        return data_frame
