import unittest


class TestMethods(unittest.TestCase):
    def test_working_pwd(self):
        from Server import security

        pwd = "test123"

        h = security.get_hash(pwd)

        self.assertEqual(security.verify(pwd, h), True)

    def test_not_working_pwd(self):
        from Server import security

        pwd = "test123"

        h = security.get_hash(pwd)

        self.assertEqual(security.verify(pwd * 2, h), False)


if __name__ == "__main":
    unittest.main()
