from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp
from file_writer.file_writer import FileWriter


out = FileWriter("Problem6Output.csv")

V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
A_list = range(2000, 2201)
out.write_line(V)

out.write_line("CHANGEGREEDY")
for A in A_list:
    (denominations, total) = changegreedy(V, A)
    out.write("%d, " % A)
    out.write_line("%d, " % total)

out.write_line("CHANGEDP")
for A in A_list:
    (denominations, total) = changedp(V, A)
    out.write("%d, " % A)
    out.write_line("%d, " % total)

out.write_line("__end Results")

out.close()
