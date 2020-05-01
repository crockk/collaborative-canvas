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
        user = User.create(username='test', password='password')

    def test_default(self):
        r = requests.get(API_URL + '/')
        self.assertEqual(r.status_code, 200)

    def test_home(self):
        r = requests.get(API_URL + '/home')
        self.assertEqual(r.status_code, 200)

    def test_profile(self):
        pass

    def test_login(self):
        r = requests.get(API_URL + '/login')


if __name__ == '__main__':
    unittest.main()
