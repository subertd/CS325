#!/usr/bin/python

import math, re, sys
import ModifiedTSPAllVisited as visit
from algorithm.don_sandbox_tsp_algorithm import DonsSandboxTSPAlgorithm
from algorithm.collective_algorithm import RealTSPAlgorithm
from runner.runner import Runner
import time
import unittest

# usage: python system_test.py inputfilename solutionfilename


class SystemTest(unittest.TestCase):

    TESTS_TO_RUN = range(1, 4)

    EXAMPLE_FILES = [
        '../tsp_trivial.txt',
        '../tsp_example_1.txt',
        '../tsp_example_2.txt',
        '../tsp_example_3.txt'
    ]

    EXPECTED_TIMES = [
        1.0,
        345600.0,
        345600.0,
        345600.0,
        180.0,
        180.0,
        180.0,
        180.0
    ]

    EXPECTED_TOTALS = [
        2 * 1.25,
        108159 * 1.25,
        2579 * 1.25,
        1573084 * 1.25
    ]

    def test_collective_algorithm(self):
        self.do_test_example_sets(RealTSPAlgorithm())

    def do_test_example_sets(self, algorithm):
        runner = Runner(algorithm)

        for i in self.TESTS_TO_RUN:
            input_file = self.EXAMPLE_FILES[i]
            output_file = "%s.tour" % input_file
            expected_total = self.EXPECTED_TOTALS[i]
            expected_time = self.EXPECTED_TIMES[i]

            # Run the algorithm and generate output file
            sys.argv[1] = '-f'
            sys.argv[2] = input_file
            runner.load()
            start_time = time.clock()
            runner.run()
            elapsed_time = time.clock() - start_time

            # verify that all cities are visited
            (all_match, problems) = visit.main(input_file, output_file)
            message = "For %s, possible problems include:\n" % output_file[3:]
            for each in problems:
                message = "%s%s\n" % (message, problems[each])
            self.assertTrue(all_match, message)

            # verify correct solution length
            cities = self.readinstance(input_file)
            solution = self.readsolution(output_file)
            self.checksolution(cities, solution[0][0], solution[1])

            # verify that the solution is reasonably optimal
            message = "For %s, the total distance %f exceeded the allowed %f" % (output_file[3:],
                                                                                 solution[0][0], expected_total)
            self.assertTrue(solution[0][0] <= expected_total, message)

            # verify that the problem was solved within the allotted time frame
            message = "For %s, execution time of %f exceeded allotted time of %f" % (output_file[3:],
                                                                                     elapsed_time, expected_time)
            self.assertTrue(elapsed_time < expected_time, message)

            print "%s passed all tests with distance %d out of possible %d" % (self.EXAMPLE_FILES[i][3:],
                                                                               solution[0][0], expected_total)

    def distance(self, a,b):
        # a and b are integer pairs (each representing a point in a 2D, integer grid)
        # Euclidean distance rounded to the nearest integer:
        dx = a[0]-b[0]
        dy = a[1]-b[1]
        #return int(math.sqrt(dx*dx + dy*dy)+0.5) # equivalent to the next line
        return int(round(math.sqrt(dx*dx + dy*dy)))

    def readinstance(self, filename):
        # each line of input file represents a city given by three integers:
        # identifier x-coordinate y-coordinate (space separated)
        # city identifiers are always consecutive integers starting with 0
        # (although this is not assumed here explicitly,
        #    it will be a requirement to match up with the solution file)
        f = open(filename,'r')
        line = f.readline()
        cities = []
        while len(line) > 1:
            lineparse = re.findall(r'[^,;\s]+', line)
            cities.append([int(lineparse[1]),int(lineparse[2])])
            line = f.readline()
        f.close()
        return cities

    def readsolution(self, filename):
        # first line is the length of the solution
        # remaining lines are the cities in the order they are visited
        # each city is listed once
        # cities are identified by integers from 0 to n-1

        # read in tour length
        f = open(filename,'r')
        value = int(f.readline())

        # read in cities
        solution = []
        line = f.readline()
        while len(line) > 1:
            lineparse = re.findall(r'[^,;\s]+', line)
            solution.append(int(lineparse[0]))
            line = f.readline()
        f.close()

        return [[value], solution]

    def checksolution(self, cities, value, cityorder):
        # calculate the length of the tour given by cityorder:
        n = len(cities)
        dist = 0
        for i in range(n):
            dist = dist + self.distance(cities[cityorder[i]],cities[cityorder[i - 1]])

        message = "solution length given as %d but computed as %d" % (value, dist)
        self.assertEqual(value, dist, message)

        '''
        # check value of solution
        if dist == value:
            print('solution found of length ', value)
        else:
            print('solution length given as ', value)
            print('but computed as ', dist)
        '''

        # check all n cities here
        n = len(cities)
        cityorder.sort()
        for i in range(n):
            message = "city not found: %d" % i
            self.assertEqual(cityorder[i], i, message)


if __name__ == '__main__':
    unittest.main()
