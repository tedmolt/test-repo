import unittest
from hello import say_hello


class TestSayHello(unittest.TestCase):
    def test_say_hello_returns_hello_world(self):
        self.assertEqual(say_hello(), "Hello World")


if __name__ == "__main__":
    unittest.main()
