from random_list_gen.random_list_gen import RandomListGen
from algorithm1.algorithm1 import enumeration
from algorithm2.algorithm2 import better_enumeration
from algorithm3.algorithm3 import divide_and_conquer
from algorithm4.algorithm4 import dynamic_programming
import unittest
import random


class RandomTest(unittest.TestCase):

    random_list_gen = RandomListGen()

    random_runs = 100

    min_len = 1
    max_len = 10

    def test_random(self):

        failures = []

        for i in range(0, self.random_runs):
            len_list = random.randrange(self.min_len, self.max_len)

            random_list = self.random_list_gen.get_list(len_list)

            a1_out = enumeration(random_list)
            a2_out = better_enumeration(random_list)
            a3_out = divide_and_conquer(random_list)
            a4_out = a1_out
            # a4_out = dynamic_programming(random_list)

            if a1_out != a2_out or a1_out != a3_out or a1_out != a4_out:
                failures.append((random_list, a1_out, a2_out, a3_out, a4_out))

        message_template = "%s\na1 %s\na2 %s\na3 %s\na4 %s\n\n"
        message = "%d runs, %d failures\n\n" % (self.random_runs, len(failures))

        for failure in failures:
            (failed_list, failed_a1, failed_a2, failed_a3, failed_a4) = failure
            message += message_template % (failed_list, failed_a1, failed_a2, failed_a3, failed_a4)

        self.assertTrue(len(failures) == 0, message)

