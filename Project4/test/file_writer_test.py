import unittest
from mock import mock_open
from mock import patch
from io.file_writer import FileWriter


class FileWriterTest(unittest.TestCase):

    TEST_FILE_PATH = 'foo'
    TOUR_EXTENSION = '.tour'
    TEST_OUTPUT_STRING = 'bar'

    def test_opensAFileWithTheAppendedExtensionForOverwriting(self):

        mock = mock_open()
        with patch('io.file_writer.open', mock, create=True):
            FileWriter(self.TEST_FILE_PATH)
            mock.assert_called_once_with(self.TEST_FILE_PATH + self.TOUR_EXTENSION, 'w')

    def test_writesTheStringToTheFile(self):
        with patch('io.file_writer.open', mock_open(), create=True) as mock:
            FileWriter(self.TEST_FILE_PATH).write_file(self.TEST_OUTPUT_STRING)
            file_handle = mock.return_value.__enter__.return_value
            file_handle.write.assert_called_with(self.TEST_OUTPUT_STRING)

if __name__ == '__main__':
    unittest.main()
