import sqlite3
from os.path import join
from time import sleep

from Server import security

_path_ = ""
database_name = "user_data"
table_name = "USER_DATA"
user_name = "user"
pwd_name = "password"


def create_database(_path, db_name, table1, item1, item2):
    try:
        with sqlite3.connect(join(_path, '{}.sqlite'.format(db_name))) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SQLITE_VERSION()')
            data = cursor.fetchone()
            print("SQLite Version: %s" % data)
            cursor.execute('CREATE TABLE IF NOT EXISTS "%s" ("%s" TEXT NOT NULL , '
                           '"TIMESTAMP" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, "%s" TEXT)' %
                           (table1, item1, item2))
    except Exception as error:
        print("Failed to load Database")
        print(error)
        print(Exception)


class UserManager:
    """
    This module will allow usernames and passwords to be stored and recovered from a database.

    TODO: Check security level of storage to ensure that it is not easy to break.
    """

    def __init__(self, path: str = _path_):
        self._path = path
        self._database = None
        self._cmd_list = []
        self._alive = False

    @property
    def path(self):
        return self._path

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, item: object):
        self._database = item

    @property
    def cmd_list(self):
        return self._cmd_list

    @cmd_list.setter
    def cmd_list(self, _data=None):
        if _data is None:
            self._cmd_list = []
        else:
            self._cmd_list = _data

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, state: bool):
        self._alive = state

    def __enter__(self):
        self.open(database=self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database.commit()
        self.close()

    def open(self, database=None):
        if database is None:
            database = self.path
        if not self.alive:
            self.database = sqlite3.connect(database=join(database, "server.sqlite"))
            self.alive = True
        else:
            print("Database is not active!")

    def close(self):
        if self.alive:
            self.commit()
            self.database.close()
            self.alive = False
        else:
            print("Database is not active.")

    def _give_cmd(self, command: list or dict, args: list or dict = None):
        c = self.database.cursor()
        c.execute(command, args)

    def _insert_many(self, timeout=2):
        c = self.database.cursor()
        for _ in range(timeout * 10):
            try:
                c.executemany("INSERT INTO {} ({}, {}) VALUES(?, ?)".format(table_name, user_name, pwd_name),
                              self.cmd_list)
            except Exception:
                sleep(timeout / 10)
            finally:
                break
        self.cmd_list = None

    def commit(self):
        self._insert_many()
        self.database.commit()

    def _rollback(self):
        self.database.rollback()

    def add_user(self, user, pwd_hash):
        self.cmd_list.append((user, pwd_hash))

    def check_user_cred(self, username: str, pwd: str) -> bool:
        with self.database.cursor as c:
            try:
                c.execute("SELECT {} FROM '{}'".format(username, table_name))
            except sqlite3.OperationalError as error:
                print("{} does not exist in the database\n{}".format(username, error))
                return False
            _data = sorted(c.fetchall())
            while _data:
                yield security.verify(pwd, _data.pop())

