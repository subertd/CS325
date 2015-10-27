from algorithm1.algorithm1 import changeslow
from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp
from file_writer.file_writer import FileWriter
import time


class Problem6:

    def __init__(self, time_out):
        self.time_out = time_out

    totals_out = FileWriter("Problem6Output.csv")

    def __delete__(self):
        self.totals_out.close()

    def run(self):

        V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        A_list = range(2000, 2201)

        self.time_out.write_line("Problem6")

        A_list_string = ("%s" % A_list)[1:-1]
        self.totals_out.write_line(" , " + A_list_string + ",")
        self.time_out.write_line(" , " + A_list_string + ",")

        self.totals_out.write("CHANGESLOW, ")
        self.time_out.write("CHANGESLOW, ")

        for A in A_list:
            start_slow = time.clock()
            (denominations_slow, total_slow) = changeslow(V, A - 1999)
            duration_slow = time.clock() - start_slow
            self.totals_out.write("%d, " % total_slow)
            self.time_out.write("%f, " % duration_slow)

        self.totals_out.write_line("")
        self.time_out.write_line("")

        self.totals_out.write("CHANGEGREEDY, ")
        self.time_out.write("CHANGEGREEDY, ")

        for A in A_list:
            start_greedy = time.clock()
            (denominations_greedy, total_greedy) = changegreedy(V, A)
            duration_greedy = time.clock() - start_greedy
            self.totals_out.write("%d, " % total_greedy)
            self.time_out.write("%f, " % duration_greedy)

        self.totals_out.write_line("")
        self.time_out.write_line("")

        self.totals_out.write("CHANGEDP, ")
        self.time_out.write("CHANGEDP, ")

        for A in A_list:
            start_dp = time.clock()
            (denominations_dp, total_dp) = changedp(V, A)
            duration_dp = time.clock() - start_dp
            self.totals_out.write("%d, " % total_dp)
            self.time_out.write("%f, " % duration_dp)

        self.totals_out.write_line("")
        self.time_out.write_line("")

        self.totals_out.close()
