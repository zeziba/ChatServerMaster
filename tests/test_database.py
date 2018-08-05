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
        finally:
            sys.stdout = std_out

        self.assertEqual(correct_out, str(out))

    def test_create_database(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        correct_out = "SQLite Version: "
        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

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

            from Server import database_server
            database_server.create_database(_dir, "head", "middle", "end")
        finally:
            sys.stdout = std_out

        self.assertIn(correct_out, str(out))

    def test_database_path_property(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        self.assertEqual(_dir, database.path)

    def test_database_database_property(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        self.assertEqual(type(database.database), type(None))

    def test_database_cmd_property(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        self.assertEqual(database.cmd_list, [])

    def test_database_alive_property(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        self.assertEqual(type(database.alive), bool)

    def test_database_database_setter(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)
        database.database = 10

        self.assertEqual(database.database, 10)

    def test_database_cmd_setter(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)
        database.cmd_list = None

        self.assertEqual(database.cmd_list, [])

        database.cmd_list = []

        self.assertEqual(database.cmd_list, [])

        database.cmd_list = [1, 2, 3]

        self.assertEqual(database.cmd_list, [1, 2, 3])

    def test_database_alive_setter(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)
        database.alive = False

        self.assertEqual(database.alive, False)

        database.alive = True

        self.assertEqual(database.alive, True)

    def test_database_open(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        self.assertEqual(database.alive, False)

        database.open()

        self.assertEqual(database.alive, True)

    def test_database_close(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        self.assertEqual(database.alive, False)

        database.open()

        self.assertEqual(database.alive, True)

        database.close()

        self.assertEqual(database.alive, False)

    def test_database_context_manager_basic(self):
        from os import getcwd, makedirs, remove
        from os.path import join

        _dir = join(getcwd(), "test_data")

        remove(join(_dir, "server.sqlite"))

        try:
            makedirs(_dir)
        except FileExistsError:
            pass

        from Server import database_server
        database_server.create_database(_dir, "head", "middle", "end")

        database = database_server.DatabaseManager(_dir)

        with database as db:
            self.assertEqual(database.alive, True)
        self.assertEqual(database.alive, False)


if __name__ == "_main__":
    unittest.main()
