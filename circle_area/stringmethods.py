import unittest


class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("JOEL", "joel".upper())

    def test_isupper(self):
        self.assertTrue("JOEL".isupper())
        self.assertFalse("joel".isupper())

    def test_split(self):
        s = "hello world"
        self.assertListEqual(["hello", "world"], s.split())
        self.assertListEqual(["hello world"], s.split(','))
        self.assertRaises(TypeError, s.split, 2)
        self.assertRaises(TypeError, s.split, False)


if __name__ == '__main__':
    unittest.main()
