import unittest
from mock import mock_open
from mock import patch
import random
from io.file_reader import FileReader


class FileReaderTest(unittest.TestCase):
    TEST_FILE_PATH = 'foo'
    TEST_LINE = "60 4568 8468"

    def test_errorsIfPassedNullParameter(self):
        try:
            self.assertRaises(Exception, FileReader(None))
        except:
            pass

    def test_errorsIfPassedEmtpyStringParameter(self):
        try:
            self.assertRaises(Exception, FileReader(''))
        except:
            pass

    def test_opens_the_file_for_reading(self):
        mock = mock_open()
        with patch('io.file_reader.open', mock, create=True):
            FileReader(self.TEST_FILE_PATH)

        mock.assert_called_once_with(self.TEST_FILE_PATH, 'r')

    def test_returns_empty_dictionary_for_emtpy_input(self):
        input_string = ''
        with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
            mock.return_value.__iter__.return_value = input_string.splitlines()
            actual = FileReader(self.TEST_FILE_PATH).get_input()
            expected = {}
            self.assertEquals(expected, actual)

    def test_returnsSize1DictionaryForASingleLineOfInput(self):
        input_string = self.TEST_LINE
        with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
            mock.return_value.__iter__.return_value = input_string.splitlines()
            input_list = FileReader(self.TEST_FILE_PATH).get_input()
            expected_size = 1
            actual_size = len(input_list)
            self.assertEquals(expected_size, actual_size)

    def test_returnsDictionaryOfSizeEqualToLinesOfInput(self):

        r = random.randrange
        input_string = ""

        for i in range(1, 100):
            input_string += "%d %d %d\n" % (r(16000), r(100000), r(100000))
            with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
                mock.return_value.__iter__.return_value = input_string.splitlines()
                input_list = FileReader(self.TEST_FILE_PATH).get_input()
                actual_size = len(input_list)
                expected_size = i
                self.assertEquals(expected_size, actual_size)

    def test_eachDictionaryElementContainsTheCorrespondingInput(self):

        r = random.randrange
        input_string = ""
        test_dictionary = {}

        # generate test input
        for i in range(0, 3):
            key = r(0, 16000)
            x_value = r(0, 100000)
            y_value = r(0, 100000)
            input_string += '%d %d %d\n' % (key, x_value, y_value)
            test_dictionary[key] = (x_value, y_value)

        # set up mock_open with test input
        with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
            mock.return_value.__iter__.return_value = input_string.splitlines()
            input_dictionary = FileReader(self.TEST_FILE_PATH).get_input()

        # verify that each element contains the expected value
        for (key, actual) in input_dictionary.iteritems():
            expected = test_dictionary[key]
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
