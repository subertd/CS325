from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp
from file_writer.file_writer import FileWriter


out = FileWriter("Problem5Output.csv")

V1 = [1, 2, 6, 12, 24, 48, 60]
V2 = [1, 6, 13, 37, 150]
A_list = range(2000, 2201, 1)

out.write_line(" , %s, %s" % (V1, V2))

out.write_line("CHANGEGREEDY")
for A in A_list:
    out.write("%d, " % A)
    (denominations, total) = changegreedy(V1, A)
    out.write("%d, " % total)
    (denominations, total) = changegreedy(V2, A)
    out.write_line("%d, " % total)

out.write_line("CHANGEDP")
for A in A_list:
    out.write("%d, " % A)
    (denominations, total) = changedp(V1, A)
    out.write("%d, " % total)
    (denominations, total) = changedp(V2, A)
    out.write_line("%d, " % total)

out.close()
