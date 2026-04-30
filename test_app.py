import unittest
from app import login, calculate_sum, is_even

class TestApp(unittest.TestCase):
    
    def test_login_success(self):
        result = login("admin", "secret")
        self.assertEqual(result["status"], "success")
    
    def test_login_failure(self):
        result = login("wrong", "wrong")
        self.assertEqual(result["status"], "failed")
    
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum([1, 2, 3]), 6)
        self.assertEqual(calculate_sum([]), 0)
    
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

if __name__ == '__main__':
    unittest.main()
