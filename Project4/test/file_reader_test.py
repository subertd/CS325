import unittest
from mock import mock_open
from mock import patch
from io.file_reader import FileReader


class MyTestCase(unittest.TestCase):
    TEST_FILE_PATH = 'foo'

    def test_opens_the_file_for_overwriting(self):

        mock = mock_open()
        with patch('io.file_reader.open', mock, create=True):
            FileReader(self.TEST_FILE_PATH)

        mock.assert_called_once_with(self.TEST_FILE_PATH, 'r')

if __name__ == '__main__':
    unittest.main()
