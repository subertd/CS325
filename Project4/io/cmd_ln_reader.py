from io.invalid_input_exception import InvalidInputException
from os.path import isfile
from optparse import OptionParser


def get_input_file_name():

    parser = OptionParser()
    parser.add_option('-f', '--file', dest='filename',
                      help='the name of the input file (with extension)', metavar='FILE')

    (options, args) = parser.parse_args()
    input_file_name = options.__dict__['filename']

    if input_file_name is None:
        raise InvalidInputException('The input filename must be specified on the command line [-f or --file]')

    if not isfile(input_file_name):
        raise InvalidInputException("The specified filename is not valid '%s'" % input_file_name)

    return input_file_name
