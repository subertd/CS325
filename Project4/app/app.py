from io.cmd_ln_reader import CmdLnReader
from io.file_reader import FileReader
from io.file_writer import FileWriter
from io.graph_parser import GraphParser
from algorithm.tsp_dynamic_programming import TSPWithDP

graph_parser = GraphParser()

input_file_path = "%s.txt" % CmdLnReader().get_file_path()
input_string = FileReader(input_file_path).get_string()
graph = GraphParser().parse_input(input_string)
solution = TSPWithDP().solve(graph)
output_string = graph_parser.format_output(solution)
output_file_path = "%sx.txt" % input_file_path
FileWriter(output_file_path).write_file(output_string)
