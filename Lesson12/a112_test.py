import unittest

from a112 import some_func

class TestAllTests(unittest.TestCase):
    def test_some_func(self):
        self.assertEqual(some_func(), 'Something!1')

if __name__ == '__main__':
    unittest.main()        