import controller
from datetime import datetime, timedelta
from dateutil.relativedelta import *

controller = controller.Controller()


def main_menu():
    print('\t\tMenu')
    print('[1] Generate data')
    print('[2] Add data')
    print('[3] Delete data')
    print('[4] Update data')
    print('[5] Compare amount of sold products in stores by category')
    print('[6] Compare average prices in stores by category')
    print('[7] Get the most popular products')
    print('[8] Get products which need more advertisements')
    print('[9] Search')
    print('[10] Exit')


def generation_menu():
    print('[1] Customer')
    print('[2] Purchase')
    print('[3] Review')


def crud_menu():
    print('[1] Customer')
    print('[2] Purchase')
    print('[3] Review')
    print('[4] Product')


def compare_menu():
    print('[1] Day')
    print('[2] Month')


def store_menu():
    print('[1] Prostor')
    print('[2] Watsons')
    print('[3] Brocard')
    print('[4] Kosmo')


def filter_menu():
    print('[1] rating')
    print('[2] amount of reviews and purchasing')


def search_menu():
    print('[1] Products by rating range')
    print('[2] Purchases by date range')


def generate(_table):
    try:
        number = int(input('Enter number of rows for generation: '))
    except ValueError:
        print('Incorrect value for number')
        return
    if _table == 1:
        controller.generate_customer(number)
    if _table == 2:
        controller.generate_purchase(number)
    if _table == 3:
        controller.generate_review(number)


def add(_table):
    if _table == 1:
        email = input('Enter email: ')
        if not email:
            print('Values cannot be empty')
            return
        first_name = input('Enter first name: ')
        if not first_name:
            print('Values cannot be empty')
            return
        last_name = input('Enter last name: ')
        if not last_name:
            print('Values cannot be empty')
            return
        controller.add_customer(email, first_name, last_name)
    if _table == 2:
        try:
            product_id = abs(int(input('Enter product id: ')))
        except ValueError:
            print('Incorrect value')
            return
        date_time = input('Enter date and time of purchase (YYYY-MM-DD HH:MM:SS): ')
        if validate_date(date_time):
            controller.add_purchase(product_id, date_time)
    if _table == 3:
        try:
            rating = abs(int(input('Enter rating (from 1 to 5): ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            product_id = abs(int(input('Enter product id: ')))
        except ValueError:
            print('Incorrect value')
            return
        customer_email = input('Enter customer\'s email: ')
        if not customer_email:
            print('Values cannot be empty')
            return
        controller.add_review(rating, product_id, customer_email)
    if _table == 4:
        name = input('Enter name: ')
        if not name:
            print('Values cannot be empty')
            return
        try:
            category_id = abs(int(input('Enter category id: ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            store_id = abs(int(input('Enter store id: ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            price = abs(int(input('Enter price: ')))
        except ValueError:
            print('Incorrect value')
            return
        controller.add_product(name, category_id, store_id, price)


def delete(_table):
    if _table == 1:
        customer_email = input('Enter customer\'s email: ')
        if not customer_email:
            print('Values cannot be empty')
            return
        controller.delete_customer(customer_email)
    if _table == 2:
        try:
            purchase_id = abs(int(input('Enter purchase id: ')))
        except ValueError:
            print('Incorrect value')
            return
        controller.delete_purchase(purchase_id)
    if _table == 3:
        try:
            review_id = abs(int(input('Enter review id: ')))
        except ValueError:
            print('Incorrect value')
            return
        controller.delete_review(review_id)
    if _table == 4:
        try:
            product_id = abs(int(input('Enter product id: ')))
        except ValueError:
            print('Incorrect value')
            return
        controller.delete_product(product_id)


def update(_table):
    if _table == 1:
        email = input('Enter new email: ')
        if not email:
            print('Values cannot be empty')
            return
        first_name = input('Enter new first name: ')
        if not first_name:
            print('Values cannot be empty')
            return
        last_name = input('Enter new last name: ')
        if not last_name:
            print('Values cannot be empty')
            return
        controller.update_customer(email, first_name, last_name)
    if _table == 2:
        try:
            purchase_id = abs(int(input('Enter purchase id: ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            product_id = abs(int(input('Enter new product id: ')))
        except ValueError:
            print('Incorrect value')
            return
        date_time = input('Enter new date and time of purchase (YYYY-MM-DD HH:MM:SS): ')
        if validate_date(date_time):
            controller.update_purchase(purchase_id, product_id, date_time)
    if _table == 3:
        try:
            review_id = abs(int(input('Enter review id: ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            rating = abs(int(input('Enter new rating (from 1 to 5): ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            product_id = abs(int(input('Enter new product id: ')))
        except ValueError:
            print('Incorrect value')
            return
        customer_email = input('Enter new customer\'s email: ')
        if not customer_email:
            print('Values cannot be empty')
            return
        controller.update_review(review_id, rating, product_id, customer_email)
    if _table == 4:
        try:
            product_id = abs(int(input('Enter product id: ')))
        except ValueError:
            print('Incorrect value')
            return
        name = input('Enter new name: ')
        if not name:
            print('Values cannot be empty')
            return
        try:
            category_id = abs(int(input('Enter new category id: ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            store_id = abs(int(input('Enter new store id: ')))
        except ValueError:
            print('Incorrect value')
            return
        try:
            price = abs(int(input('Enter new price: ')))
        except ValueError:
            print('Incorrect value')
            return
        controller.update_product(product_id, name, category_id, store_id, price)


def get_date_range(date_time):
    if date_time == 1:
        date_time_start = input('Enter date and time of the day (YYYY-MM-DD): ')
        date_time_start += ' 00:00:00'
        if validate_date(date_time_start):
            date_time_start = datetime.strptime(date_time_start, '%Y-%m-%d %H:%M:%S')
            date_time_end = date_time_start
            date_time_end += timedelta(days=1)
            return [date_time_start, date_time_end, True]
        else:
            return False
    if date_time == 2:
        month = input('Enter number of the year and month (YYYY-MM): ')
        month += '-01 00:00:00'
        if validate_date(month):
            date_time_start = datetime.strptime(month, '%Y-%m-%d %H:%M:%S')
            if date_time_start.month == datetime.now().month and date_time_start.year == datetime.now().year:
                date_time_end = datetime.now()
                return [date_time_start, date_time_end, False]
            else:
                date_time_end = date_time_start
                date_time_end += relativedelta(months=+1)
                return [date_time_start, date_time_end, False]
        else:
            return False
    else:
        return False


def compare_prices(store_1, store_2):
    controller.compare_prices(store_1, store_2)


def validate_date(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        min_date = datetime.strptime('2019-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        if date <= datetime.now() or date >= min_date:
            return True
        else:
            print('Entered datetime must be <= datetime now and >= 2019-01-01 00:00:00')
            return False
    except ValueError:
        print('Incorrect date format')
        return False


while True:
    main_menu()
    try:
        action = abs(int(input('Choose action: ')))
    except ValueError:
        print('Incorrect value for action')
        continue
    if action == 1:
        generation_menu()
        try:
            table = abs(int(input('Choose table: ')))
        except ValueError:
            print('Incorrect value for table')
            continue
        generate(table)
        continue
    if action == 2:
        crud_menu()
        try:
            table = abs(int(input('Choose table: ')))
        except ValueError:
            print('Incorrect value for table')
            continue
        add(table)
        continue
    if action == 3:
        crud_menu()
        try:
            table = abs(int(input('Choose table: ')))
        except ValueError:
            print('Incorrect value for table')
            continue
        delete(table)
        continue
    if action == 4:
        crud_menu()
        try:
            table = abs(int(input('Choose table: ')))
        except ValueError:
            print('Incorrect value for table')
            continue
        update(table)
        continue
    if action == 5:
        compare_menu()
        try:
            period_of_time = abs(int(input('Choose period of time for comparison: ')))
        except ValueError:
            print('Incorrect value')
            continue
        date_range = get_date_range(period_of_time)
        if date_range:
            if date_range[2]:
                controller.compare_amount_by_day(date_range)
            else:
                controller.compare_amount_by_month(date_range)
        continue
    if action == 6:
        store_menu()
        try:
            store1 = abs(int(input('Choose first store for comparison: ')))
            store2 = abs(int(input('Choose second store for comparison: ')))
        except ValueError:
            print('Incorrect value')
            continue
        if store1 == store2:
            print('Error! Stores must be different')
        else:
            compare_prices(store1, store2)
    if action == 7:
        filter_menu()
        try:
            data = abs(int(input('Choose parameter for getting products: ')))
        except ValueError:
            print('Incorrect value')
            continue
        print('These products will become even more popular then now')
        controller.get_popular_products(data)
    if action == 8:
        filter_menu()
        try:
            data = abs(int(input('Choose parameter for getting products: ')))
        except ValueError:
            print('Incorrect value')
            continue
        print('These products need more advertisements')
        controller.get_unpopular_products(data)
    if action == 9:
        search_menu()
        try:
            search = abs(int(input('Choose what to search: ')))
        except ValueError:
            print('Incorrect value')
            continue
        if search == 1:
            try:
                rating1 = abs(float(input('Input minimum rating: ')))
                rating2 = abs(float(input('Input maximum rating: ')))
            except ValueError:
                print('Incorrect value')
                continue
            if rating1 > rating2:
                print('Error! First rating must be smaller then second')
            else:
                controller.search_rating(rating1, rating2)
        if search == 2:
            date1 = input('Input minimum date (YYYY-MM): ')
            date2 = input('Input maximum date (YYYY-MM): ')
            date1 += ' 00:00:00'
            date2 += ' 00:00:00'
            if validate_date(date1) and validate_date(date2):
                controller.search_date(date1, date2)
    if action == 10:
        break
