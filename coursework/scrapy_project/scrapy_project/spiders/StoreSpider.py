import psycopg2

from scrapy_project.items import ProductItem

import scrapy


class ProstorLipsSpider(scrapy.Spider):
    name = "prostor_lips"
    page = 1
    start_urls = [
        'https://prostor.ua/ua/dekorativnaya-kosmetika/dlya-gub/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) "\
                    f"values (\'{item['title']}\', {item['price']}, 1, 2)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://prostor.ua/ua/dekorativnaya-kosmetika/dlya-gub/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class ProstorFaceSpider(scrapy.Spider):
    name = "prostor_face"
    page = 1
    start_urls = [
        'https://prostor.ua/ua/dekorativnaya-kosmetika/dlya-litsa/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 1, 1)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://prostor.ua/ua/dekorativnaya-kosmetika/dlya-litsa/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class ProstorEyesAndEyebrowsSpider(scrapy.Spider):
    name = "prostor_eyes"
    page = 1
    start_urls = [
        'https://prostor.ua/ua/dekorativnaya-kosmetika/dlya-glaz-brovej/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 1, 3)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://prostor.ua/ua/dekorativnaya-kosmetika/dlya-glaz-brovej/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class ProstorPerfumerySpider(scrapy.Spider):
    name = "prostor_perfumery"
    page = 1
    start_urls = [
        'https://prostor.ua/ua/parfumeriya/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 1, 4)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://prostor.ua/ua/parfumeriya/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


####################################################


class WatsonsLipsSpider(scrapy.Spider):
    name = "watsons_lips"
    page = 0
    start_urls = [
        'https://www.watsons.ua/uk/krasa/gubi/c/H700?page=0&startPage=0',
    ]

    def parse(self, response):
        is_end = False
        content = response.css('div.js-plp-product-grid__item')
        if not content:
            is_end = True
        for a in content:
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('p.product-tile__product-name-link__description-overflow::text').get()
            price = a.css('div.product-tile__price--original::text').get()
            if not price:
                price = a.css('div.product-tile__price--discounted::text').get()
            if not price:
                price = a.css('div.product-tile__price--tpr::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 2, 2)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.watsons.ua/uk/krasa/gubi/c/H700?page={self.page}&startPage={self.page}'
        if next_page is not None and is_end is False:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class WatsonsFaceSpider(scrapy.Spider):
    name = "watsons_face"
    page = 0
    start_urls = [
        'https://www.watsons.ua/uk/krasa/ton-oblichchya-ta-rumyana/c/H1001?page=0&startPage=0',
    ]

    def parse(self, response):
        is_end = False
        content = response.css('div.js-plp-product-grid__item')
        if not content:
            is_end = True
        for a in content:
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('p.product-tile__product-name-link__description-overflow::text').get()
            price = a.css('div.product-tile__price--original::text').get()
            if not price:
                price = a.css('div.product-tile__price--discounted::text').get()
            if not price:
                price = a.css('div.product-tile__price--tpr::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 2, 1)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.watsons.ua/uk/krasa/ton-oblichchya-ta-rumyana/c/H1001?page={self.page}&startPage={self.page}'
        if next_page is not None and is_end is False:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class WatsonsEyesAndEyebrowsSpider(scrapy.Spider):
    name = "watsons_eyes"
    page = 0
    start_urls = [
        'https://www.watsons.ua/uk/krasa/ochi-ta-brovi/c/H800?page=0&startPage=0',
    ]

    def parse(self, response):
        is_end = False
        content = response.css('div.js-plp-product-grid__item')
        if not content:
            is_end = True
        for a in content:
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('p.product-tile__product-name-link__description-overflow::text').get()
            price = a.css('div.product-tile__price--original::text').get()
            if not price:
                price = a.css('div.product-tile__price--discounted::text').get()
            if not price:
                price = a.css('div.product-tile__price--tpr::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 2, 3)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.watsons.ua/uk/krasa/ochi-ta-brovi/c/H800?page={self.page}&startPage={self.page}'
        if next_page is not None and is_end is False:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class WatsonsPerfumerySpider(scrapy.Spider):
    name = "watsons_perfumery"
    page = 0
    start_urls = [
        'https://www.watsons.ua/uk/krasa/parfumi/c/L?page=0&startPage=0',
    ]

    def parse(self, response):
        is_end = False
        content = response.css('div.js-plp-product-grid__item')
        if not content:
            is_end = True
        for a in content:
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('p.product-tile__product-name-link__description-overflow::text').get()
            price = a.css('div.product-tile__price--original::text').get()
            if not price:
                price = a.css('div.product-tile__price--discounted::text').get()
            if not price:
                price = a.css('div.product-tile__price--tpr::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 2, 4)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.watsons.ua/uk/krasa/parfumi/c/L?page={self.page}&startPage={self.page}'
        if next_page is not None and is_end is False:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


####################################################


class BrocardLipsSpider(scrapy.Spider):
    name = "brocard_lips"
    page = 1
    start_urls = [
        'https://www.brocard.ua/ua/category/gubi/page-1',
    ]

    def parse(self, response):
        for a in response.css('li.product'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            brand = a.css('strong.product-item-brand::text').get()
            name = a.css('strong.product-item-name::text').get()
            p_type = a.css('span.item-type::text').get()
            p_type = p_type.title()
            title = f'{p_type} {brand} {name}'
            price = a.css('span.price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 3, 2)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.brocard.ua/ua/category/gubi/page-{self.page}'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class BrocardFaceSpider(scrapy.Spider):
    name = "brocard_face"
    page = 1
    start_urls = [
        'https://www.brocard.ua/ua/category/oblichchya/page-1',
    ]

    def parse(self, response):
        for a in response.css('li.product'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            brand = a.css('strong.product-item-brand::text').get()
            name = a.css('strong.product-item-name::text').get()
            p_type = a.css('span.item-type::text').get()
            p_type = p_type.title()
            title = f'{p_type} {brand} {name}'
            price = a.css('span.price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 3, 1)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.brocard.ua/ua/category/oblichchya/page-{self.page}'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class BrocardEyesAndEyebrowsSpider(scrapy.Spider):
    name = "brocard_eyes"
    page = 1
    start_urls = [
        'https://www.brocard.ua/ua/category/ochi-i-brovi/page-1',
    ]

    def parse(self, response):
        for a in response.css('li.product'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            brand = a.css('strong.product-item-brand::text').get()
            name = a.css('strong.product-item-name::text').get()
            p_type = a.css('span.item-type::text').get()
            p_type = p_type.title()
            title = f'{p_type} {brand} {name}'
            price = a.css('span.price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 3, 3)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.brocard.ua/ua/category/ochi-i-brovi/page-{self.page}'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class BrocardPerfumerySpider(scrapy.Spider):
    name = "brocard_perfumery"
    page = 1
    start_urls = [
        'https://www.brocard.ua/ua/category/parfumeriya/page-1',
    ]

    def parse(self, response):
        for a in response.css('li.product'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            brand = a.css('strong.product-item-brand::text').get()
            name = a.css('strong.product-item-name::text').get()
            p_type = a.css('span.item-type::text').get()
            p_type = p_type.title()
            title = f'{p_type} {brand} {name}'
            price = a.css('span.price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(',')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 3, 4)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://www.brocard.ua/ua/category/parfumeriya/page-{self.page}'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


####################################################


class KosmoLipsSpider(scrapy.Spider):
    name = "kosmo_lips"
    page = 1
    start_urls = [
        'https://kosmo.ua/ua/dekorativnaya-kosmetika/dlya-gub/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 4, 2)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://kosmo.ua/ua/dekorativnaya-kosmetika/dlya-gub/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class KosmoFaceSpider(scrapy.Spider):
    name = "kosmo_face"
    page = 1
    start_urls = [
        'https://kosmo.ua/ua/dekorativnaya-kosmetika/dlya-litsa/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 4, 1)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://kosmo.ua/ua/dekorativnaya-kosmetika/dlya-litsa/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class KosmoEyesAndEyebrowsSpider(scrapy.Spider):
    name = "kosmo_eyes"
    page = 1
    start_urls = [
        'https://kosmo.ua/ua/dekorativnaya-kosmetika/dlya-glaz-brovej/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 4, 3)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://kosmo.ua/ua/dekorativnaya-kosmetika/dlya-glaz-brovej/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class KosmoPerfumerySpider(scrapy.Spider):
    name = "kosmo_perfumery"
    page = 1
    start_urls = [
        'https://kosmo.ua/ua/parfumeriya/filter/page=1/',
    ]

    def parse(self, response):
        for a in response.css('li.catalog-grid__item'):
            conn = psycopg2.connect(dbname='course_work', user='postgres', password='masha2001', host='localhost')
            conn.autocommit = True
            cursor = conn.cursor()
            item = ProductItem()
            title = a.css('div.catalogCard-title a::text').get()
            price = a.css('div.catalogCard-price::text').get()
            new_title = ' '.join(title.split())
            new_price = ' '.join(price.split())
            new_price = new_price.split(' ')[0]
            if '\'' in new_title:
                new_title = new_title.replace('\'', '\'\'')
            item['title'] = new_title
            item['price'] = new_price
            self.log(item['title'])
            self.log(item['price'])
            query = "insert into product (name, price, store_id, category_id) " \
                    f"values (\'{item['title']}\', {item['price']}, 4, 4)"
            try:
                cursor.execute(query)
            except Exception as e:
                print(e)
                continue
            conn.close()
            yield item

        self.page += 1
        next_page = f'https://kosmo.ua/ua/parfumeriya/filter/page={self.page}/'
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
