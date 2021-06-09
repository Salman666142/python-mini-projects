import unittest


def displays_storage():
    file2 = open("conversion storage.txt", "r+")
    # print(file2.read())
    # file2.close()
    return file2.read()


class BasicTests(unittest.TestCase):

    def test_storage(self):
        given_length = len(displays_storage())
        get_file = open("conversion storage.txt", "r+")
        actual_length = len(get_file.read())
        self.assertEqual(given_length, actual_length)


if __name__ == '__main__':
    unittest.main()
