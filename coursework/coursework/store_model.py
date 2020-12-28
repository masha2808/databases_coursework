from store import Store


class StoreModel:
    def __init__(self, session):
        self.session = session

    def select_store(self, _id):
        store = self.session.query(Store).filter(Store.id == _id).first()
        return store
