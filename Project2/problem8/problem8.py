from algorithm1.algorithm1 import changeslow
from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp
from file_writer.file_writer import FileWriter
import time


class Problem8:

    def __init__(self):
        self.time_out = FileWriter("Problem8Output.csv")

    def __delete__(self):
        self.time_out.close()

    def run(self):

        slow_modifier = 3
        greedy_modifier = 100000
        dp_modifier = 100

        # V_slow = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        V_slow = []
        V_greedy = []
        V_dp = []

        self.time_out.write(", ")

        for i in range(10, 510, 10):
            self.time_out.write("%d, " % i)
            V_slow.append(self.get_V_of_length_for_modifier(i, slow_modifier))
            V_greedy.append(self.get_V_of_length_for_modifier(i, greedy_modifier))
            V_dp.append(self.get_V_of_length_for_modifier(i, dp_modifier))

        self.time_out.write_line("")

        A_slow = 10 * slow_modifier
        A_greedy = 10 * greedy_modifier
        A_dp = 10 * dp_modifier

        self.time_out.write("CHANGESLOW, ")

        for V in V_slow:
            start_slow = time.clock()
            (denominations_slow, total_slow) = changeslow(V, A_slow)
            duration_slow = time.clock() - start_slow
            self.time_out.write("%f, " % duration_slow)

        self.time_out.write("\nCHANGEGREEDY, ")

        for V in V_greedy:
            start_greedy = time.clock()
            (denominations_greedy, total_greedy) = changegreedy(V, A_greedy)
            duration_greedy = time.clock() - start_greedy
            self.time_out.write("%f, " % duration_greedy)

        self.time_out.write("\nCHANGEDP, ")

        for V in V_dp:
            start_dp = time.clock()
            (denominations_dp, total_dp) = changedp(V, A_dp)
            duration_dp = time.clock() - start_dp
            self.time_out.write("%f, " % duration_dp)

        self.time_out.write_line("")

        self.time_out.close()

    def get_V_of_length_for_modifier(self, length, modifier):

        V = [1]

        for i in range(1, length):
            V.append(V[i - 1] + i * modifier)

        return V
