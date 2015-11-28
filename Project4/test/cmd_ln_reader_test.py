import sys
from io.cmd_ln_reader import get_input_file_name
from mock import patch
from io.invalid_input_exception import InvalidInputException
import unittest


class CmdLnReaderTest(unittest.TestCase):

    EXTANT_FILE = '__init__.py'
    NONEXISTENT_FILE = 'bar'

    MOCK_EXTANT_FILES = [EXTANT_FILE]

    @patch('os.path.isfile')
    def test_returnsTheStringEnteredForFilenameInCommandLineArgumentsIfValid(self, mock_isfile):

        for opt_form in ['-f', '--file']:
            sys.argv[1] = opt_form
            sys.argv[2] = self.EXTANT_FILE
            mock_isfile.side_effect = self.MOCK_EXTANT_FILES
            mock_isfile.return_value = True
            self.assertEqual(self.EXTANT_FILE, get_input_file_name())

    def test_raisesExceptionForMissingOptargFilename(self):
        self.assertRaises(InvalidInputException, get_input_file_name)

    @patch('os.path.isfile')
    def test_raisesExceptionIfFileDoesNotExist(self, mock_isfile):

        for opt_form in ['-f', '--file']:
            sys.argv[1] = opt_form
            sys.argv[2] = self.NONEXISTENT_FILE
            mock_isfile.return_value = False
            self.assertRaises(InvalidInputException, get_input_file_name)


if __name__ == '__main__':
    unittest.main()
