import sqlite3
from os.path import join
from time import sleep

_path_ = "\\"
table_name = "CHAT_DATA"
item_name = "IP_ADDR"
chat = "chat_data"


def create_database(_path, table1, item1, item2):
    try:
        with sqlite3.connect(join(_path, 'server.sqlite')) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT SQLITE_VERSION()')
            data = cursor.fetchone()
            print("SQLite Version: %s" % data)
            cursor.execute('CREATE TABLE IF NOT EXISTS "%s" ("%s" TEXT NOT NULL , '
                           '"TIMESTAMP" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, "%s" TEXT)' %
                           (table1, item1, item2))
            global table_name
            global item_name
            global chat
            table_name = table1
            item_name = item1
            chat = item2
    except Exception as error:
        print("Failed to load Database")
        print(error)
        print(Exception)


class DatabaseManager:
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
                c.executemany("INSERT INTO {} ({}, {}) VALUES(?, ?)".format(table_name, item_name, chat), self.cmd_list)
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

    def add_chat(self, table, _data):
        self.cmd_list.append((table, _data))

    def get_chats(self, override: str = chat):
        with self.database.cursor as c:
            _data = sorted(c.fetchall())
            while _data:
                yield _data.pop()


if __name__ == "__main__":
    create_database(_path_, table_name, item_name, chat)
