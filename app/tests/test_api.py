import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        response = requests.post(f"{BASE_URL}/auth/token", json={"user": "testuser"})
        self.token = response.json()["token"]

    def test_create_book(self):
        headers = {"Authorization": self.token}
        data = {"title": "1984", "author": "George Orwell", "published_date": "1949-06-08"}
        response = requests.post(f"{BASE_URL}/books", json=data, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        headers = {"Authorization": self.token}
        response = requests.get(f"{BASE_URL}/books", headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
