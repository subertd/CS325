import unittest
from mock import mock_open
from mock import patch
import random
from io.file_reader import FileReader


class MyTestCase(unittest.TestCase):
    TEST_FILE_PATH = 'foo'

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

    def test_returns_empty_array_for_emtpy_input(self):
        input_string = ''
        with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
            mock.return_value.__iter__.return_value = input_string.splitlines()
            actual = FileReader(self.TEST_FILE_PATH).get_input()
            expected = []
            self.assertEquals(expected, actual)

    def test_returnsSize1ListForASingleLineOfInput(self):
        input_string = self.getRandomLine()
        with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
            mock.return_value.__iter__.return_value = input_string.splitlines()
            input_list = FileReader(self.TEST_FILE_PATH).get_input()
            expected_size = 1
            actual_size = len(input_list)
            self.assertEquals(expected_size, actual_size)

    def test_returnsListOfSizeEqualToLinesOfInput(self):

        input_string = ""

        for i in range(1, 100):
            input_string += self.getRandomLine()
            with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
                mock.return_value.__iter__.return_value = input_string.splitlines()
                input_list = FileReader(self.TEST_FILE_PATH).get_input()
                actual_size = len(input_list)
                expected_size = i
                self.assertEquals(expected_size, actual_size)

    def test_eachListElementContainsAsManyStringsAsWhitespaceSeparatedCharacterBlocksInTheInput(self):

        input_string = ""

        # generate test input
        for i in range(1, 100):
            input_string += '%d' % random.randrange(0, 16000)
            for j in range(1, i):
                input_string += ' %d' % random.randrange(0, 100000)
            input_string += '\n'

        # set up mock_open with test input
        with patch('io.file_reader.open', mock_open(read_data=input_string)) as mock:
            mock.return_value.__iter__.return_value = input_string.splitlines()
            input_list = FileReader(self.TEST_FILE_PATH).get_input()

        expected_size = 0
        for line in input_list:

            # verify that each line has the expected number of elements
            expected_size += 1
            actual_size = len(line)
            message = "For line: '\n%s\n', expecting: %d, but was: %d" % (line, expected_size, actual_size)
            self.assertEquals(expected_size, actual_size, message)

            # verify that each element is the expected string
            expected_element_index = 0
            for actual_element in line:
                expected_element = input_string.splitlines()[expected_size - 1].split()[expected_element_index]
                self.assertEquals(expected_element, actual_element)
                expected_element_index += 1

    def getRandomLine(self):
        r = random.randrange
        return "%d %d %d\n" % (r(0, 16000), r(0, 100000), r(0, 100000))


if __name__ == '__main__':
    unittest.main()
