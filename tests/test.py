import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class Testing(unittest.TestCase):
    """
    Main Sample testing class for FastAPI example
    """
    def test_main_route(self):
        """
        Simple test case to check if a 200 is returned
        """
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json(), {"Goodeye": "World"})

    def test_main_route_payload(self):
        """
        Simple test case to check if a Goodeye is returned
        """
        response = client.get("/")
        self.assertEqual(response.json(), {"GoodBYE": "World"})


if __name__ == '__main__':
    unittest.main()
    