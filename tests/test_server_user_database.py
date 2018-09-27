import sys
import unittest


class TestMethods(unittest.TestCase):
    def test_import(self):
        correct_out = ""

        class MyOut(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)

        std_out = sys.stdout
        out = MyOut()
        try:
            sys.stdout = out
            from Server import user_database
        finally:
            sys.stdout = std_out

        self.assertEqual(correct_out, str(out))

    def test_creation(self):
        correct_out = "SQLite Version: "

        class MyOut(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)

        std_out = sys.stdout
        out = MyOut()
        try:
            sys.stdout = out
            from Server import user_database
            from os import path
            from os import getcwd
            from os import remove
            path = path.join(getcwd())
            user_database.create_database(path, "user", "stuff", "things", "others")
        finally:
            sys.stdout = std_out

        self.assertIn(correct_out, str(out))


if __name__ == "_main__":
    unittest.main()
