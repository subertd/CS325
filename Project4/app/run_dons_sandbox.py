from io.file_reader import FileReader
from graph_formatter.graph_formatter import parse_input, format_output
from algorithm.don_sandbox_tsp_algorithm import DonsSandboxTSPAlgorithm

input_dictionary = FileReader('tsp_example_1.txt').get_input()
graph = parse_input(input_dictionary)
solution = DonsSandboxTSPAlgorithm().solve(graph)
print format_output(solution)
