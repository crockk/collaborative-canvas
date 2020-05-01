import unittest
import requests
from create_tables import create
from drop_tables import drop
from database import User

API_URL = "http://127.0.0.1:5000"


class TestApi(unittest.TestCase):

    def setUp(self) -> None:
        drop()
        create()
        user = {'new_username':'test', 'new_password':'P@ssw0rd'}
        requests.post(API_URL + '/register', user)

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

    def test_profile(self):
        pass

    def test_register(self):
        pass

    def test_logout(self):
        pass


if __name__ == '__main__':
    unittest.main()
