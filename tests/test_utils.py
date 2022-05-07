import unittest

from utils import hello

class TestUtils(unittest.TestCase):

    def test_hello_should_return_hello_world(self):
        # Arrange
        # Acts
        self.assertEqual('hello world', hello())



if __name__ == '__main__':
    unittest.main()
