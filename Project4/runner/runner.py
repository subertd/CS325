from io.cmd_ln_reader import get_input_file_name
from io.file_reader import FileReader
from io.file_writer import FileWriter
from graph_formatter.graph_formatter import parse_input, format_output
from io.invalid_input_exception import InvalidInputException
import time


class Runner:

    algorithm = None
    input_file_name = None
    graph = None

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def load(self):
        io_start = time.clock()

        try:
            self.input_file_name = get_input_file_name()
        except InvalidInputException as e:
            print "Error: %s" % str(e)
            exit(1)

        input_dictionary = FileReader(self.input_file_name).get_input()

        io_stop = time.clock()
        print "%f seconds to do file input operations" % (io_stop - io_start)

        parse_start = time.clock()
        self.graph = parse_input(input_dictionary)
        parse_stop = time.clock()
        print "%f seconds to parse graph edges" % (parse_stop - parse_start)

    def run(self):
        solution = self.algorithm.solve(self.graph)
        output_string = format_output(solution)
        FileWriter(self.input_file_name).write_file(output_string)
