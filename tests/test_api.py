import unittest
from app import app, fibonacci


class TestFibonacciAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_fibonacci_function(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_api_valid_request(self):
        response = self.app.get('/fib?n=10')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 55)

    def test_api_invalid_request(self):
        response = self.app.get('/fib?n=-1')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Bad request.')


if __name__ == '__main__':
    unittest.main()
