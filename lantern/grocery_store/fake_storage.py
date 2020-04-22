from itertools import count
from store_app import NoSuchUserError, NoSuchStoreID, NoSuchManagerID, NoSuchInGoods


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._stores = FakeStores()
        self._goods = FakeGoods()
    @property
    def users(self):
        return self._users

    @property
    def stores(self):
        return self._stores

    @property
    def goods(self):
        return self._goods


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, store):
        store_id = next(self._id_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreID(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            if store_id not in self._stores:
                raise NoSuchStoreID(store_id)
            else:
                raise NoSuchManagerID



class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, good):
        good_id = next(self._id_counter)
        self._goods[good_id] = good
        return good_id

    def get_good_by_id(self, good_id):
        try:
            return self._goods[good_id]
        except KeyError:
            raise NoSuchInGoods(good_id)

    def update_good_by_id(self, good_id, good):
        if good_id in self._goods:
            self._goods[good_id] = good
        else:
            pass
