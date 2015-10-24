from file_writer.file_writer import FileWriter
from problem4.problem4 import Problem4
from problem5.problem5 import Problem5
from problem6.problem6 import Problem6


time_out = FileWriter('Problem7Output.csv')

problem4 = Problem4(time_out)
problem5 = Problem5(time_out)
problem6 = Problem6(time_out)

problem4.run()
problem5.run()
problem6.run()

time_out.close()

"""
out.write("CHANGESLOW, ")
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

out.write("CHANGEGREEDY, ")
for i in range(0, len(a2_list_lengths)):
    a2_random_lists = random_list_gen.get_lists(100, a2_list_lengths[i])
    start = time.clock()
    for random_list in a2_random_lists:
        better_enumeration(random_list)
    elapsed = time.clock() - start
    out.write("%f, " % elapsed)
out.write_line('')

out.write("CHANGEDP, ")
for i in range(0, len(a3_list_lengths)):
    a3_random_lists = random_list_gen.get_lists(100, a3_list_lengths[i])
    start = time.clock()
    for random_list in a3_random_lists:
        divide_and_conquer(random_list)
    elapsed = time.clock() - start
    out.write("%f, " % elapsed)
out.write_line('')

out.close()
"""