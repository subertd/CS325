from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp
from file_writer.file_writer import FileWriter
import time


class Problem5:

    def __init__(self, time_out):
        self.time_out = time_out

    totals_out = FileWriter("Problem5Output.csv")

    def _delete__(self):
        self.totals_out.close()

    def run(self):

        V1 = [1, 2, 6, 12, 24, 48, 60]
        V2 = [1, 6, 13, 37, 150]
        A_list = range(2000, 2201, 1)
        A_list_string = ("%s" % A_list)[1:-1]


        # V1
        self.totals_out.write_line("V1")
        self.time_out.write_line("Problem5: V1")
        self.totals_out.write_line(" , " + A_list_string + ",")
        self.time_out.write_line(" , " + A_list_string + ",")

        # Changegreedy
        self.totals_out.write("CHANGEGREEDY, ")
        self.time_out.write("CHANGEGREEDY, ")
        for A in A_list:
            start_greedy = time.clock()
            (denominations_greedy, total_greedy) = changegreedy(V1, A)
            duration_greedy = time.clock() - start_greedy
            self.totals_out.write("%d, " % total_greedy)
            self.time_out.write("%f, " % duration_greedy)
        self.totals_out.write_line("")
        self.time_out.write_line("")

        # Changedp
        self.totals_out.write("CHANGEDP, ")
        self.time_out.write("CHANGEDP, ")
        for A in A_list:
            start_dp = time.clock()
            (denominations_dp, total_dp) = changedp(V1, A)
            duration_dp = time.clock() - start_dp
            self.totals_out.write("%d, " % total_dp)
            self.time_out.write("%f, " % duration_dp)
        self.totals_out.write_line("")
        self.time_out.write_line("")

        # V2
        self.totals_out.write_line("V2")
        self.time_out.write_line("Problem5: V2")
        self.totals_out.write_line(" , " + A_list_string + ",")
        self.time_out.write_line(" , " + A_list_string + ",")

        # Changegreedy
        self.totals_out.write("CHANGEGREEDY, ")
        self.time_out.write("CHANGEGREEDY, ")
        for A in A_list:
            start_greedy = time.clock()
            (denominations_greedy, total_greedy) = changegreedy(V2, A)
            duration_greedy = time.clock() - start_greedy
            self.totals_out.write("%d, " % total_greedy)
            self.time_out.write("%f, " % duration_greedy)
        self.totals_out.write_line("")
        self.time_out.write_line("")

        # Changedp
        self.totals_out.write("CHANGEDP, ")
        self.time_out.write("CHANGEDP, ")
        for A in A_list:
            start_dp = time.clock()
            (denominations_dp, total_dp) = changedp(V2, A)
            duration_dp = time.clock() - start_dp
            self.totals_out.write("%d, " % total_dp)
            self.time_out.write("%f, " % duration_dp)
        self.totals_out.write_line("")
        self.time_out.write_line("")

        self.totals_out.close()
