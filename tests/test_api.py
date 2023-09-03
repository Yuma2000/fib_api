import unittest

from app import MAX_N_VALUE, app

CONTENT_TYPE_JSON = "application/json"


class TestFibonacciAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", data)
        self.assertIn("Welcome to the Fibonacci API!", data["message"])

    def test_valid_fib_request(self):
        response = self.app.get('/fib?n=10', headers={"Content-Type": CONTENT_TYPE_JSON})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 55)

    def test_missing_content_type(self):
        response = self.app.get('/fib?n=10')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], f"Invalid header. Expected Content-Type: {CONTENT_TYPE_JSON}.")

    def test_missing_parameter(self):
        response = self.app.get('/fib', headers={"Content-Type": CONTENT_TYPE_JSON})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], "Parameter 'n' is missing.")

    def test_invalid_n_value(self):
        response = self.app.get('/fib?n=abc', headers={"Content-Type": CONTENT_TYPE_JSON})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], "Parameter 'n' should be a positive integer.")

    def test_negative_n_value(self):
        response = self.app.get('/fib?n=-5', headers={"Content-Type": CONTENT_TYPE_JSON})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], "Parameter 'n' should be a positive integer.")

    def test_0_n_value(self):
        response = self.app.get('/fib?n=0', headers={"Content-Type": CONTENT_TYPE_JSON})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], "Parameter 'n' should be a positive integer.")

    def test_large_n_value(self):
        response = self.app.get(f'/fib?n={MAX_N_VALUE + 1}', headers={"Content-Type": CONTENT_TYPE_JSON})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        expected_message = f"Value too large. Maximum allowed is {MAX_N_VALUE}."
        self.assertEqual(data['message'], expected_message)

    def test_fibonacci_values(self):
        test_cases = [
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
        ]
        for n, expected in test_cases:
            response = self.app.get(f'/fib?n={n}', headers={"Content-Type": CONTENT_TYPE_JSON})
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['result'], expected, f"Failed for n={n}")


if __name__ == '__main__':
    unittest.main()
