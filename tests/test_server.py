import asyncio
import sys
import unittest


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    return wrapper


class TestMethods(unittest.TestCase):

    @async_test
    def test_handeler(self):
        # TODO: Fix this test method to work on the handler
        return

        from Server import server

        class MyOut(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)

        class ws:
            def recv(self):
                return "apple"

            def send(self, data):
                pass

        std_out = sys.stdout

        out = MyOut()
        try:
            sys.stdout = out
            handle = server.handle(ws(), None)
        finally:
            sys.stdout = std_out

        self.assertEquals(str(out), "Received: apple")


if __name__ == "__main__":
    unittest.main()
