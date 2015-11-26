from io.cmd_ln_reader import CmdLnReader
from io.file_reader import FileReader
from io.file_writer import FileWriter
from io.graph_parser import GraphParser
from algorithm.collective_algorithm import TSPWithDP

graph_parser = GraphParser()

input_file_path = CmdLnReader().get_file_path()
input_string = FileReader(input_file_path).get_input()
graph = GraphParser().parse_input(input_string)
solution = TSPWithDP().solve(graph)
output_string = graph_parser.format_output(solution)
output_file_path = input_file_path
FileWriter(output_file_path).write_file(output_string)
