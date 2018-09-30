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
            from ConfigManager import manager
        finally:
            sys.stdout = std_out

        self.assertEqual(correct_out, str(out))

    def test_create_ini(self):
        import os.path
        _dir = os.path.join(os.path.expanduser("~"), "Chat Server", "default_config.ini")

        from ConfigManager import manager

        manager.create_config(_dir)
        exists = os.path.isfile(_dir)

        self.assertTrue(exists)

    def test_open_ini(self):
        from ConfigManager import manager
        import os.path
        _dir = os.path.join(os.path.expanduser("~"), "Chat Server", "default_config.ini")

        manager.create_config(_dir)

        import configparser

        self.assertIsInstance(manager.open_config(_dir), configparser.ConfigParser)

    def test_selection_ini(self):
        from ConfigManager import manager
        import os.path
        _dir = os.path.join(os.path.expanduser("~"), "Chat Server", "default_config.ini")

        manager.create_config(_dir)

        self.assertEqual(manager.config_selection(_dir), manager.default_config)


if __name__ == "_main__":
    unittest.main()
