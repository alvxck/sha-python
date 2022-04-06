import unittest
from src.sha512 import *

class TestSHA512(unittest.TestCase):
    def test_hash(self):
        test = SHA512('hello world')
        self.assertEqual(test.hash(), '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f')

if __name__ == '__main__':
    unittest.main()