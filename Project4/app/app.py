from io.cmd_ln_reader import get_input_file_name
from io.file_reader import FileReader
from io.file_writer import FileWriter
from graph_formatter.graph_formatter import parse_input, format_output
from algorithm.collective_algorithm import RealTSPAlgorithm
from io.invalid_input_exception import InvalidInputException

input_file_name = None

try:
    input_file_name = get_input_file_name()
except InvalidInputException as e:
    print "Error: %s" % e.message
    exit(1)

input_dictionary = FileReader(input_file_name).get_input()
graph = parse_input(input_dictionary)
solution = RealTSPAlgorithm().solve(graph)
output_string = format_output(solution)
FileWriter(input_file_name).write_file(output_string)
