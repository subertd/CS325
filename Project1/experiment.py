from random_list_gen.random_list_gen import RandomListGen
from file_writer.file_writer import FileWriter
from algorithm1.algorithm1 import enumeration
from algorithm2.algorithm2 import better_enumeration
from algorithm3.algorithm3 import divide_and_conquer
from algorithm4.algorithm4 import dynamic_programming
import time


# The values of n to test each algorithm for each step
a1_list_lengths = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
a2_list_lengths = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
a3_list_lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
a4_list_lengths = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

random_list_gen = RandomListGen()
out = FileWriter('Output/ExperimentalData.txt')

out.write_line(" , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

out.write("Enumeration, ")
# For each possible list length of algorithm1
for i in range(0, len(a1_list_lengths)):
    a1_random_lists = random_list_gen.get_lists(100, a1_list_lengths[i])
    start = time.clock()

    # For each of the random lists of the current size
    for random_list in a1_random_lists:
        enumeration(random_list)
    elapsed = time.clock() - start
    out.write("%f, " % elapsed)
out.write_line('')

out.write("Better Enumeration, ")
for i in range(0, len(a2_list_lengths)):
    a2_random_lists = random_list_gen.get_lists(100, a2_list_lengths[i])
    start = time.clock()
    for random_list in a2_random_lists:
        better_enumeration(random_list)
    elapsed = time.clock() - start
    out.write("%f, " % elapsed)
out.write_line('')

out.write("Divide and Conquer, ")
for i in range(0, len(a3_list_lengths)):
    a3_random_lists = random_list_gen.get_lists(100, a3_list_lengths[i])
    start = time.clock()
    for random_list in a3_random_lists:
        divide_and_conquer(random_list)
    elapsed = time.clock() - start
    out.write("%f, " % elapsed)
out.write_line('')

out.write("Dynamic Programming, ")
for i in range(0, len(a4_list_lengths)):
    a4_random_lists = random_list_gen.get_lists(100, a4_list_lengths[i])
    start = time.clock()
    for random_list in a4_random_lists:
        dynamic_programming(random_list)
    elapsed = time.clock() - start
    out.write("%f, " % elapsed)
out.write_line('')

out.close()
