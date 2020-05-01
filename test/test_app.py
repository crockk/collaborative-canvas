import unittest
import requests
from create_tables import create
from drop_tables import drop

API_URL = "http://127.0.0.1:5000"


class TestApi(unittest.TestCase):

    def setUp(self) -> None:
        drop()
        create()
        user = {'new_username':'test', 'new_password':'P@ssw0rd'}
        requests.post(API_URL + '/register', user)

        self.user = {'username':'test', 'password':'P@ssw0rd'}

    def test_default(self):
        r = requests.get(API_URL + '/')
        self.assertEqual(r.status_code, 200)

    def test_home(self):
        r = requests.get(API_URL + '/home')
        self.assertEqual(r.status_code, 200)

    def test_login(self):
        r = requests.get(API_URL + '/login')
        self.assertEqual(r.status_code, 200)

        data = {'username':'test', 'password':'P@ssw0rd'}
        r = requests.post(API_URL + '/login', data)
        self.assertEqual(r.status_code, 200)

        data = {'username':'test', 'password':'wrong_password'}
        r = requests.post(API_URL + '/login', data)
        self.assertEqual(r.status_code, 400)

        data = {'username':'doesnot', 'password':'exist'}
        r = requests.post(API_URL + '/login', data)
        self.assertEqual(r.status_code, 400)

    def test_profile(self, ):
        r = requests.get(API_URL + '/profile')
        self.assertEqual(r.status_code, 200)

        requests.post(API_URL + '/login', self.user)

        r = requests.get(API_URL + '/profile')
        self.assertEqual(r.status_code, 200)

    def test_register(self):
        r = requests.get(API_URL + '/register')
        self.assertEqual(r.status_code, 200)

        new_user = {'new_username': 'jimmy', 'new_password':'P@ssw0rd'}
        r = requests.post(API_URL + '/register', new_user)
        self.assertEqual(r.status_code, 200)

        new_user = {'new_username': 'test', 'new_password':'P@ssw0rd'}
        r = requests.post(API_URL + '/register', new_user)
        self.assertEqual(r.status_code, 400)

        new_user = {'new_username': 'jimmy', 'new_password':'bad'}
        r = requests.post(API_URL + '/register', new_user)
        self.assertEqual(r.status_code, 400)

    def test_logout(self):
        r = requests.get(API_URL + '/logout')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
