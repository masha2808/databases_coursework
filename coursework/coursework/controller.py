from sqlite3 import IntegrityError
import view
import customer_model
import review_model
import purchase_model
import product_model
import store_model
import category_model
import comparison_model
import search_model

from base import Session


class Controller:
    session = Session()

    def __init__(self):
        self.CustomerModel = customer_model.CustomerModel(self.session)
        self.ReviewModel = review_model.ReviewModel(self.session)
        self.PurchaseModel = purchase_model.PurchaseModel(self.session)
        self.ProductModel = product_model.ProductModel(self.session)
        self.StoreModel = store_model.StoreModel(self.session)
        self.CategoryModel = category_model.CategoryModel(self.session)
        self.ComparisonModel = comparison_model.ComparisonModel()
        self.SearchModel = search_model.SearchModel()
        self.view = view.View()

    def generate_customer(self, number):
        try:
            time = self.CustomerModel.generate_customer(number)
            self.view.generation_message(time, number)
        except IntegrityError as e:
            self.view.generation_error_message(number)

    def generate_review(self, number):
        try:
            time = self.ReviewModel.generate_review(number)
            self.view.generation_message(time, number)
        except IntegrityError as e:
            self.view.generation_error_message(number)

    def generate_purchase(self, number):
        try:
            time = self.PurchaseModel.generate_purchase(number)
            self.view.generation_message(time, number)
        except IntegrityError as e:
            self.view.generation_error_message(number)

    def add_customer(self, email, first_name, last_name):
        customer = self.CustomerModel.select_customer(email)
        if customer:
            self.view.customer_error(email)
        else:
            customer = self.CustomerModel.insert_customer(email, first_name, last_name)
            columns = ['email', 'first_name', 'last_name']
            values = [customer.email, customer.first_name, customer.last_name]
            self.view.print_added_item('Customer', values, columns)

    def add_purchase(self, product_id, date_time):
        product = self.ProductModel.select_product(product_id)
        if product:
            purchase_arr = self.PurchaseModel.insert_purchase(product_id, date_time)
            if purchase_arr[0]:
                purchase = purchase_arr[1]
                columns = ['id', 'product_id', 'date_time']
                values = [purchase.id, purchase.product_id, purchase.date_time]
                self.view.print_added_item('Purchase', values, columns)
            else:
                self.view.database_error(purchase_arr[1])
        else:
            self.view.foreign_key_error('Product', 'id', product_id)

    def add_review(self, rating, product_id, customer_email):
        product = self.ProductModel.select_product(product_id)
        customer = self.CustomerModel.select_customer(customer_email)
        if product and customer:
            review_arr = self.ReviewModel.insert_review(rating, product_id, customer_email)
            if review_arr[0]:
                review = review_arr[1]
                columns = ['id', 'rating', 'product_id', 'customer_email']
                values = [review.id, review.rating, review.product_id, review.customer_email]
                self.view.print_added_item('Review', values, columns)
            else:
                self.view.database_error(review_arr[1])
        else:
            if not product:
                self.view.foreign_key_error('Product', 'id', product_id)
            if not customer:
                self.view.foreign_key_error('Customer', 'email', customer_email)

    def add_product(self, name, category_id, store_id, price):
        store = self.StoreModel.select_store(store_id)
        category = self.CategoryModel.select_category(category_id)
        if store and category:
            product = self.ProductModel.insert_product(name, category_id, store_id, price)
            columns = ['id', 'name', 'category_id', 'store_id', 'rating', 'price']
            values = [product.id, product.name, product.category_id, product.store_id, product.rating, product.price]
            self.view.print_added_item('Product', values, columns)
        else:
            if not store:
                self.view.foreign_key_error('Store', 'id', store_id)
            if not category:
                self.view.foreign_key_error('Category', 'id', category_id)

    def delete_customer(self, email):
        customer = self.CustomerModel.select_customer(email)
        if customer:
            self.ReviewModel.delete_review_by_customer(email)
            deleted_customer = self.CustomerModel.delete_customer(email)
            columns = ['email', 'first_name', 'last_name']
            values = [deleted_customer.email, deleted_customer.first_name, deleted_customer.last_name]
            self.view.print_deleted_item('Customer', values, columns)
        else:
            self.view.item_error('Customer', 'email', email)

    def delete_purchase(self, _id):
        purchase = self.PurchaseModel.select_purchase(_id)
        if purchase:
            deleted_purchase = self.PurchaseModel.delete_purchase(_id)
            columns = ['id', 'product_id', 'date_time']
            values = [deleted_purchase.id, deleted_purchase.product_id, deleted_purchase.date_time]
            self.view.print_deleted_item('Purchase', values, columns)
        else:
            self.view.item_error('Purchase', 'id', _id)

    def delete_review(self, _id):
        review = self.ReviewModel.select_review(_id)
        if review:
            deleted_review = self.ReviewModel.delete_review(_id)
            columns = ['id', 'rating', 'product_id', 'customer_email']
            values = [deleted_review.id, deleted_review.rating,
                      deleted_review.product_id, deleted_review.customer_email]
            self.view.print_deleted_item('Review', values, columns)
        else:
            self.view.item_error('Review', 'id', _id)

    def delete_product(self, _id):
        product = self.ProductModel.select_product(_id)
        if product:
            self.ReviewModel.delete_review_by_product(_id)
            self.PurchaseModel.delete_purchase_by_product(_id)
            deleted_product = self.ProductModel.delete_product(_id)
            columns = ['id', 'name', 'category_id', 'store_id', 'rating', 'price']
            values = [deleted_product.id, deleted_product.name, deleted_product.category_id,
                      deleted_product.store_id, deleted_product.rating, deleted_product.price]
            self.view.print_deleted_item('Product', values, columns)
        else:
            self.view.item_error('Product', 'id', _id)

    def update_customer(self, email, first_name, last_name):
        customer = self.CustomerModel.select_customer(email)
        if customer:
            updated_customer = self.CustomerModel.update_customer(email, first_name, last_name)
            columns = ['email', 'first_name', 'last_name']
            values = [updated_customer.email, updated_customer.first_name, updated_customer.last_name]
            self.view.print_updated_item('Customer', values, columns)
        else:
            self.view.item_error('Customer', 'email', email)

    def update_purchase(self, _id, product_id, date_time):
        purchase = self.PurchaseModel.select_purchase(_id)
        if purchase:
            product = self.ProductModel.select_product(product_id)
            if product:
                purchase_arr = self.PurchaseModel.update_purchase(_id, product_id, date_time)
                if purchase_arr[0]:
                    updated_purchase = purchase_arr[1]
                    columns = ['id', 'product_id', 'date_time']
                    values = [updated_purchase.id, updated_purchase.product_id, updated_purchase.date_time]
                    self.view.print_updated_item('Purchase', values, columns)
                else:
                    self.view.database_error(purchase_arr[1])
            else:
                self.view.foreign_key_error('Product', 'id', product_id)
        else:
            self.view.item_error('Purchase', 'id', _id)

    def update_review(self, _id, rating, product_id, customer_email):
        review = self.ReviewModel.select_review(_id)
        if review:
            product = self.ProductModel.select_product(product_id)
            customer = self.CustomerModel.select_customer(customer_email)
            if product and customer:
                review_arr = self.ReviewModel.update_review(_id, rating, product_id, customer_email)
                if review_arr[0]:
                    updated_review = review_arr[1]
                    columns = ['id', 'rating', 'product_id', 'customer_email']
                    values = [updated_review.id, updated_review.rating,
                              updated_review.product_id, updated_review.customer_email]
                    self.view.print_updated_item('Review', values, columns)
                else:
                    self.view.database_error(review_arr[1])
            else:
                if not product:
                    self.view.foreign_key_error('Product', 'id', product_id)
                if not customer:
                    self.view.foreign_key_error('Customer', 'email', customer_email)
        else:
            self.view.item_error('Review', 'id', _id)

    def update_product(self, _id, name, category_id, store_id, price):
        product = self.ProductModel.select_product(_id)
        if product:
            store = self.StoreModel.select_store(store_id)
            category = self.CategoryModel.select_category(category_id)
            if store and category:
                updated_product = self.ProductModel.update_product(_id, name, category_id, store_id, price)
                columns = ['id', 'name', 'category_id', 'store_id', 'rating', 'price']
                values = [updated_product.id, updated_product.name, updated_product.category_id,
                          updated_product.store_id, updated_product.rating, updated_product.price]
                self.view.print_updated_item('Review', values, columns)
            else:
                if not store:
                    self.view.foreign_key_error('Store', 'id', store_id)
                if not category:
                    self.view.foreign_key_error('Category', 'id', category_id)
        else:
            self.view.item_error('Product', 'id', _id)

    def compare_amount_by_day(self, date_range):
        values = self.ComparisonModel.compare_amount_by_day(date_range)
        self.view.print_table(values[1])
        self.view.print_plot(values[0])

    def compare_amount_by_month(self, date_range):
        values = self.ComparisonModel.compare_amount_by_month(date_range)
        self.view.print_tables(values[1], values[2], values[3], values[4], values[5])
        self.view.print_plot(values[0])

    def compare_prices(self, store_1, store_2):
        values = self.ComparisonModel.compare_prices(store_1, store_2)
        self.view.print_table(values[3])
        self.view.print_prices(values[0], values[1], values[2])
        self.view.print_plot(values[4])

    def get_popular_products(self, data):
        values = self.ComparisonModel.get_popular_products(data)
        self.view.print_table(values[1])
        self.view.print_plot(values[0])

    def get_unpopular_products(self, data):
        values = self.ComparisonModel.get_unpopular_products(data)
        self.view.print_table(values[1])
        self.view.print_plot(values[0])

    def search_rating(self, rating1, rating2):
        table = self.SearchModel.search_rating(rating1, rating2)
        self.view.print_table(table)

    def search_date(self, date1, date2):
        table = self.SearchModel.search_date(date1, date2)
        self.view.print_table(table)
