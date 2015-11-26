import unittest
from mock import mock_open
from mock import patch
from io.file_writer import FileWriter


class FileWriterTest(unittest.TestCase):

    TEST_FILE_PATH = 'foo'
    TOUR_EXTENSION = '.tour'

    def test_opens_the_file_for_overwriting(self):

        mock = mock_open()
        with patch('io.file_writer.open', mock, create=True):
            FileWriter(self.TEST_FILE_PATH)

        mock.assert_called_once_with(self.TEST_FILE_PATH + self.TOUR_EXTENSION, 'w')


if __name__ == '__main__':
    unittest.main()
