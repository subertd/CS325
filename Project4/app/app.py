from io.cmd_ln_reader import get_input_file_name
from io.file_reader import FileReader
from io.file_writer import FileWriter
from graph_formatter.graph_formatter import parse_input, format_output
from algorithm.collective_algorithm import RealTSPAlgorithm

input_file_name = get_input_file_name()
input_dictionary = FileReader(input_file_name).get_input()
graph = parse_input(input_dictionary)
solution = RealTSPAlgorithm().solve(graph)
output_string = format_output(solution)
output_file_path = input_file_name
FileWriter(output_file_path).write_file(output_string)
