import psycopg2
import pandas
from random import randint
import matplotlib.pyplot as plt
from datetime import datetime

class ComparisonModel:
    def compare_amount_by_day(self, date_range):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = 'select p2.id as purchase_id, c.name as category, s.name as store, p1.name as product, ' \
                'p2.date_time from category as c, store as s, product as p1, purchase as p2 ' \
                'where c.id=p1.category_id and s.id=p1.store_id and p1.id=p2.product_id '\
                f'and date_time>=\'{date_range[0]}\' and date_time<=\'{date_range[1]}\''
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        pandas.set_option('display.expand_frame_repr', False)
        df = data_frame.groupby(['store', 'category']).size().unstack(fill_value=0)
        df.to_excel(f'files/purchases_by_categories({str(date_range[0]).split(" ")[0]})' + str(randint(0, 10000)) + '.xlsx')
        data_frame.groupby(['category', 'store']).count()['purchase_id'].unstack().plot(kind='bar', rot=0)
        plt.title(f'Amount of purchases by categories in stores ({str(date_range[0]).split(" ")[0]})')
        yint = []
        locs, labels = plt.yticks()
        for each in locs:
            yint.append(int(each))
        plt.yticks(yint)
        plt.ylabel('Sold products')
        plt.savefig(f'images/purchases_by_categories({str(date_range[0]).split(" ")[0]})' + str(randint(0, 10000)) + '.png')
        return [plt, df]

    def compare_amount_by_month(self, date_range):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = 'select p2.id as purchase_id, c.name as category, s.name as store, p1.name as product, ' \
                'p2.date_time from category as c, store as s, product as p1, purchase as p2 ' \
                'where c.id=p1.category_id and s.id=p1.store_id and p1.id=p2.product_id '\
                f'and date_time>=\'{date_range[0]}\' and date_time<=\'{date_range[1]}\''
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        for index in data_frame.index:
            date_str = str(data_frame.loc[index, 'date_time'])
            date_str = date_str.split(' ')
            data_frame.loc[index, 'date_time'] = datetime.strptime(date_str[0], '%Y-%m-%d')
        pandas.set_option('display.expand_frame_repr', False)
        categories = data_frame['category'].unique()
        df1 = data_frame[data_frame['category'] == categories[0]].\
            groupby(['date_time', 'store']).size().unstack(fill_value=0)
        df2 = data_frame[data_frame['category'] == categories[1]].\
            groupby(['date_time', 'store']).size().unstack(fill_value=0)
        df3 = data_frame[data_frame['category'] == categories[2]].\
            groupby(['date_time', 'store']).size().unstack(fill_value=0)
        df4 = data_frame[data_frame['category'] == categories[3]].\
            groupby(['date_time', 'store']).size().unstack(fill_value=0)
        random_int = randint(0, 10000)
        date_array = str(date_range[0]).split("-")
        date = date_array[0] + '-' + date_array[1]
        path = f'files/purchases_by_categories({date})' + str(random_int) + '.xlsx'
        writer = pandas.ExcelWriter(path, engine='xlsxwriter')
        df1.to_excel(writer, sheet_name=f'{categories[0]}')
        df2.to_excel(writer, sheet_name=f'{categories[1]}')
        df3.to_excel(writer, sheet_name=f'{categories[2]}')
        df4.to_excel(writer, sheet_name=f'{categories[3]}')
        writer.save()
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(5, 4))
        df1.plot(ax=axes[0, 0], title=f'{categories[3]} in stores ({date})')
        df4.plot(ax=axes[1, 1], title=f'{categories[0]} in stores ({date})')
        df2.plot(ax=axes[0, 1], title=f'{categories[1]} in stores ({date})')
        df3.plot(ax=axes[1, 0], title=f'{categories[2]} in stores ({date})')
        yint = []
        locs, labels = plt.yticks()
        for each in locs:
            yint.append(int(each))
        plt.yticks(yint)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.get_current_fig_manager().window.state('zoomed')
        plt.savefig(f'images/purchases_by_categories({date})' + str(randint(0, 10000)))
        return [plt, df1, df2, df3, df4, categories]

    def compare_prices(self, store1, store2):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = 'select s.name as store, c.name as category, p.price as price from store as s, category as c, ' \
                f'product as p where p.category_id=c.id and p.store_id=s.id and (store_id={store1} or store_id={store2})'
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        df = data_frame.groupby(['store', 'category']).mean().unstack(fill_value=0)
        stores = data_frame['store'].unique()
        df.to_excel(f'files/average_prices_in_{stores[0]}_and_{stores[1]}' + str(randint(0, 10000)) + '.xlsx')
        df1 = data_frame[data_frame['store'] == stores[0]]. \
            groupby(['category']).mean()
        df2 = data_frame[data_frame['store'] == stores[1]]. \
            groupby(['category']).mean()
        categories = df1.index
        df1 = df1['price']
        df2 = df2['price']
        i = 0
        differences = []
        while i < 4:
            if df1[i] > df2[i]:
                dif = df1[i] * 100 / df2[i]
                differences.append([dif, 0])
            else:
                dif = df2[i] * 100 / df1[i]
                differences.append([dif, 1])
            i += 1
        data_frame.groupby(['category', 'store']).mean().unstack().plot(kind='bar', rot=0)
        plt.title(f'Average prices in {stores[0]} and {stores[1]}')
        plt.ylabel('Average prices')
        plt.savefig(f'images/average_prices_in_{stores[0]}_and_{stores[1]}' + str(randint(0, 10000)) + '.png')
        return [differences, stores, categories, df, plt]

    def get_popular_products(self, data):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = 'with count_review as (select p.id, count(*) as review_count from product as p, review as r '\
        'group by p.id, r.product_id having r.product_id=p.id order by p.id), '\
        'count_purchase as (select p.id, count(*) as purchase_count from product as p, purchase as p1 '\
        'group by p.id, p1.product_id having p1.product_id=p.id order by p.id), '\
        'p_count as (select count_review.id, review_count, purchase_count from count_review, ' \
        'count_purchase where review_count>(select avg(review_count) from count_review) and '\
        'purchase_count>(select avg(purchase_count) from count_purchase) and count_review.id=count_purchase.id) '\
        'select product.id, product.name, rating, review_count, purchase_count from product, ' \
        'p_count where p_count.id=product.id and rating>=4'
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        if data == 1:
            pandas.set_option("display.max_rows", None, "display.max_columns", None)
            df = data_frame[['id', 'name', 'rating']]
            df.to_excel(f'files/most_popular_products_rating' + str(randint(0, 10000)) + '.xlsx')
            df1 = data_frame[['id', 'rating']]
            df1.set_index('id', inplace=True)
            df1['rating'].plot(kind='bar', rot=0, figsize=(10, 5), title='The most popular products rating')
            plt.savefig(f'images/most_popular_products_rating' + str(randint(0, 10000)) + '.png')
            return [plt, df]
        else:
            pandas.set_option("display.max_rows", None, "display.max_columns", None)
            df = data_frame[['id', 'name', 'review_count', 'purchase_count']]
            df.to_excel(f'files/most_popular_products_review_purchase' + str(randint(0, 10000)) + '.xlsx')
            df2 = data_frame[['id', 'review_count', 'purchase_count']]
            df2.set_index('id', inplace=True)
            df2[['review_count', 'purchase_count']].plot(kind='bar', rot=0, figsize=(10, 5),
                                                         title='Reviews and purchases of the most popular products')
            plt.savefig(f'images/most_popular_products_review_purchase' + str(randint(0, 10000)) + '.png')
            return [plt, df]

    def get_unpopular_products(self, data):
        conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
        query = 'with count_review as (select p.id, count(*) as review_count from product as p, review as r '\
        'group by p.id, r.product_id having r.product_id=p.id order by p.id), '\
        'count_purchase as (select p.id, count(*) as purchase_count from product as p, purchase as p1 '\
        'group by p.id, p1.product_id having p1.product_id=p.id order by p.id), '\
        'p_count as (select count_review.id, review_count, purchase_count from count_review, ' \
        'count_purchase where review_count<(select avg(review_count) from count_review) and '\
        'purchase_count<(select avg(purchase_count) from count_purchase) and count_review.id=count_purchase.id) '\
        'select product.id, product.name, rating, review_count, purchase_count from product, ' \
        'p_count where p_count.id=product.id and rating>=4.2'
        data_frame = pandas.read_sql(query, conn)
        conn.close()
        if data == 1:
            pandas.set_option("display.max_rows", None, "display.max_columns", None)
            df = data_frame[['id', 'name', 'rating']]
            df.to_excel(f'files/unpopular_products_rating' + str(randint(0, 10000)) + '.xlsx')
            df1 = data_frame[['id', 'rating']]
            df1.set_index('id', inplace=True)
            df1['rating'].plot(kind='bar', rot=0, figsize=(10, 5), title='Unpopular products rating')
            plt.savefig(f'images/unpopular_products_rating' + str(randint(0, 10000)) + '.png')
            return [plt, df]
        else:
            pandas.set_option("display.max_rows", None, "display.max_columns", None)
            df = data_frame[['id', 'name', 'review_count', 'purchase_count']]
            df.to_excel(f'files/unpopular_products_review_purchase' + str(randint(0, 10000)) + '.xlsx')
            df2 = data_frame[['id', 'review_count', 'purchase_count']]
            df2.set_index('id', inplace=True)
            df2[['review_count', 'purchase_count']].plot(kind='bar', rot=0, figsize=(10, 5),
                                                         title='Reviews and purchases of unpopular products')
            plt.savefig(f'images/unpopular_products_review_purchase' + str(randint(0, 10000)) + '.png')
            return [plt, df]
