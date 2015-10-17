from algorithm1.algorithm1 import enumeration
from algorithm2.algorithm2 import better_enumeration
from algorithm3.algorithm3 import divide_and_conquer
from algorithm4.algorithm4 import dynamic_programming
from file_loader.file_loader import load_lists_from_file
from file_writer.file_writer import FileWriter


lists = load_lists_from_file('Problems/MSS_Problems.txt')

out = FileWriter('Output/MSS_Results.txt')

for list in lists:
    algorithm1_output = enumeration(list)
    algorithm2_output = better_enumeration(list)
    algorithm3_output = divide_and_conquer(list)
    algorithm4_output = dynamic_programming(list)

    out.write_line(list)
    out.write_line('enumeration: ')
    out.write_line(algorithm1_output)
    out.write_line('better enumeration: ')
    out.write_line(algorithm2_output)
    out.write_line('divide and conquer: ')
    out.write_line(algorithm3_output)
    out.write_line('dynamic programming: ')
    out.write_line(algorithm4_output)
    out.write_line('\n')

out.close()
