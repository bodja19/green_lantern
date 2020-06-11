import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_succesful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}


class TestStores(Initializer):
    def test_create_new_store(self):
        resp = self.client.post(
            '/stores',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

        resp = self.client.post(
            '/stores',
            json={'name': 'Mad ',
                  'location': 'Kyiv',
                  'manager_id': 2}
        )
        assert resp.json == {'store_id': 2}

    def test_successful_get_store(self):
        resp = self.client.post(
            '/stores',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 1}
        )
        store_id = resp.json['store_id']
        resp = self.client.get(f'/stores/{store_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow',
                             'location': 'Lviv',
                             'manager_id': 1}

    def test_get_unexistent_store(self):
        resp = self.client.get(f'/stores/3')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 3'}

    def test_succesful_update_stores(self):
        resp = self.client.post(
            '/stores',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 2}
        )
        store_id = resp.json['store_id']
        resp = self.client.put(
            f'/stores/{store_id}',
            json={'name': 'Local Taste',
                  'location': 'Lviv',
                  'manager_id': 2}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}



    def test_unexistent_update_store_storeid(self):
        resp = self.client.put(
            f'/stores/1',
            json={'name': 'Local Taste',
                  'location': 'Lviv',
                  'manager_id': 3}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 1'}


class TestGoods(Initializer):
    def test_create_new_good(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar',
                  'price': 10}
        )
        assert resp.status_code == 201
        assert resp.json == {'good_id': 1}

    def test_successful_get_good(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar',
                  'price': 10}
        )
        good_id = resp.json['good_id']
        resp = self.client.get(f'/goods/{good_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Chocolate_bar',
                             'price': 10}

    def test_get_unexistent_good(self):
        resp = self.client.get(f'/goods/3')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such id in goods 3'}

    def test_succesful_update_good(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar',
                  'price': 10}
        )
        good_id = resp.json['good_id']
        resp = self.client.put(
            f'/goods/{good_id}',
            json={'name': 'Chocolate_ba',
                  'price': 11}
        )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 1}
