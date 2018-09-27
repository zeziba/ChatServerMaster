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
            from Server import compression
        finally:
            sys.stdout = std_out

        self.assertEqual(correct_out, str(out))

    def test_compression(self):
        from Server import compression

        data = "hello" * 800

        data_compressed = compression.encode(data)

        self.assertLessEqual(data, data_compressed)

    def test_decompression(self):
        from Server import compression

        data = "hello" * 800

        data_compressed = compression.encode(data)

        data_uncompressed = compression.decode(data_compressed)

        self.assertEqual(data, data_uncompressed)


if __name__ == "_main__":
    unittest.main()
