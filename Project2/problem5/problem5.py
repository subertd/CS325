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
        self.totals_out.write_line(V1)

        self.totals_out.write_line(", CHANGEGREEDY, CHANGEDP,")
        self.time_out.write_line(" , CHANGEGREEDY, CHANGEDP,")

        self.totals_out.write_line("V1")
        self.time_out.write_line("V1")

        for A in A_list:
            start_greedy = time.clock()
            (denominations_greedy, total_greedy) = changegreedy(V1, A)
            duration_greedy = time.clock() - start_greedy
            start_dp = time.clock()
            (denominations_dp, total_dp) = changedp(V1, A)
            duration_dp = time.clock() - start_dp

            self.totals_out.write_line("%d, %d, %d," % (A, total_greedy, total_dp))
            self.time_out.write_line("%d, %f, %f," % (A, duration_greedy, duration_dp))

        self.totals_out.write_line("V2")
        self.time_out.write_line("V2")

        for A in A_list:
            start_greedy = time.clock()
            (denominations_greedy, total_greedy) = changegreedy(V2, A)
            duration_greedy = time.clock() - start_greedy
            start_dp = time.clock()
            (denominations_dp, total_dp) = changedp(V2, A)
            duration_dp = time.clock() - start_dp

            self.totals_out.write_line("%d, %d, %d," % (A, total_greedy, total_dp))
            self.time_out.write_line("%d, %f, %f," % (A, duration_greedy, duration_dp))

        self.totals_out.write_line("__end Results")
        self.time_out.write_line("__end Results")

        self.totals_out.close()
