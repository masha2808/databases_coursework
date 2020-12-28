from category import Category


class CategoryModel:
    def __init__(self, session):
        self.session = session

    def select_category(self, _id):
        category = self.session.query(Category).filter(Category.id == _id).first()
        return category
