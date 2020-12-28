from product import Product


class ProductModel:
    def __init__(self, session):
        self.session = session

    def select_product(self, _id):
        product = self.session.query(Product).filter(Product.id == _id).first()
        return product

    def insert_product(self, name, category_id, store_id, price):
        product = Product(name, category_id, store_id, price)
        self.session.add(product)
        self.session.commit()
        if id is not None or id != 0:
            return product

    def update_product(self, _id, name, category_id, store_id, price):
        self.session.query(Product).filter(Product.id == _id). \
            update({Product.name: name, Product.category_id: category_id,
                    Product.store_id: store_id, Product.price: price})
        self.session.commit()
        product = self.select_product(_id)
        return product

    def delete_product(self, _id):
        product = self.session.query(Product).filter(Product.id == _id).first()
        self.session.query(Product).filter(Product.id == _id).delete()
        self.session.commit()
        return product
