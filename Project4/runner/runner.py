from io.cmd_ln_reader import get_input_file_name
from io.file_reader import FileReader
from io.file_writer import FileWriter
from graph_formatter.graph_formatter import parse_input, format_output
from io.invalid_input_exception import InvalidInputException


class Runner:

    algorithm = None
    input_file_name = None
    graph = None

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def load(self):

        try:
            self.input_file_name = get_input_file_name()
        except InvalidInputException as e:
            print "Error: %s" % str(e)
            exit(1)

        input_dictionary = FileReader(self.input_file_name).get_input()
        self.graph = parse_input(input_dictionary)

    def run(self):
        solution = self.algorithm.solve(self.graph)
        output_string = format_output(solution)
        FileWriter(self.input_file_name).write_file(output_string)
