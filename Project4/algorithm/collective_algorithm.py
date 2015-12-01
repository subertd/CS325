from distance_calculator.distance_calculator import get_distance
from algorithm.tsp_algorithm import TSPAlgorithm
import time


class RealTSPAlgorithm(TSPAlgorithm):

    IMPROVEMENT_THRESHOLD = 2

    graph = None

    time_spent_calculating_euclidean_distance = 0

    def __init__(self):
        TSPAlgorithm.__init__(self)

    def get_distance(self, a, b):
        (v, e) = self.graph
        dist_start = time.clock()
        dist = e[(a, b)]
        dist_stop = time.clock()
        dist_duration = dist_stop - dist_start
        if dist_duration > 0.000000001:
            self.time_spent_calculating_euclidean_distance += (dist_stop - dist_start)
        return dist

    def solve(self, (v, e)):
        self.graph = (v, e)

        nn_start = time.clock()
        solution = self.get_nearest_neighbor_solution()
        nn_stop = time.clock()
        print "%f seconds to get a nearest neighbor path of distance: %d" % ((nn_stop - nn_start), solution['total'])

        e.start_caching()

        algorithm_start = time.clock()
        solution = self.greedy_two_opt(solution)
        algorithm_stop = time.clock()

        print "%f seconds computing Euclidean distances" % self.time_spent_calculating_euclidean_distance
        print "%f seconds doing pure algorithmic operations, improving the distance to: %d" % (
            (algorithm_stop - algorithm_start - self.time_spent_calculating_euclidean_distance),
            solution['total'])

        return solution

    def greedy_two_opt(self, solution):
        (v, e) = self.graph

        best_distance = solution['total']
        existing_route = list(solution['order'])

        improvement_made = 0
        while improvement_made < self.IMPROVEMENT_THRESHOLD:
            # print "current OFV: %d" % solution['total']

            i = 0  # counter for i outer loop
            while i < len(existing_route) - 1:
                for j in xrange(i + 1, len(existing_route)):
                    new_route = self.two_opt_swap(existing_route, i, j)
                    new_distance = self.calculate_total_distance(new_route)

                    if new_distance < best_distance:
                        existing_route = new_route
                        best_distance = new_distance
                        improvement_made = 0
                        i = j
                        break

                e.clear_cache()
                i += 1

            improvement_made += 1

        return {
            'total': best_distance,
            'order': existing_route
        }

    def two_opt(self, solution):
        best_distance = solution['total']
        existing_route = list(solution['order'])

        improvement_made = 0
        while improvement_made < self.IMPROVEMENT_THRESHOLD:
            for i in range(len(existing_route) - 1):
                for k in range(i + 1, len(existing_route)):
                    new_route = self.two_opt_swap(existing_route, i, k)
                    new_distance = self.calculate_total_distance(new_route)

                    if new_distance < best_distance:
                        #print "Found distance %d, better than %d" % (new_distance, best_distance)
                        existing_route = new_route
                        best_distance = new_distance
                        improvement_made = 0

            improvement_made += 1

        return {
            'total': best_distance,
            'order': existing_route
        }

    @staticmethod
    def two_opt_swap(existing_route, i, k):
        #print("entering two_opt_swap(%d, %d)" % (i, k))

        new_tour = []

        for c in range(i):
            new_tour.append(existing_route[c])

        for t in range(k - 1, i - 1, -1):
            new_tour.append(existing_route[t])

        for r in range(k, len(existing_route)):
            new_tour.append(existing_route[r])

        return new_tour

    def calculate_total_distance(self, order):
        (v, e) = self.graph

        running_total = 0

        for i in range(len(order)):
            cur_v = order[i]
            next_v = order[(i + 1) % len(order)]
            running_total += self.get_distance(cur_v, next_v)

        return running_total

    def get_nearest_neighbor_solution(self):

        (v, e) = self.graph

        best_so_far = {
            'total': float('infinity'),
            'order': []
        }

        # get the best path of any possible starting vertex
        for starting_v in v:
            unvisited = list(v)
            cur_tour = [starting_v]
            cur_total = 0
            cur_v = starting_v

            # while there are unvisited vertexes
            while len(cur_tour) < len(v):
                unvisited.remove(cur_v)
                closest_neighbor = None
                closest_neighbor_dist = float('infinity')
                for neighbor in unvisited:
                    dist = self.get_distance(cur_v, neighbor)
                    if dist < closest_neighbor_dist:
                        closest_neighbor = neighbor
                        closest_neighbor_dist = dist

                assert closest_neighbor is not None

                cur_tour.append(closest_neighbor)
                cur_total += closest_neighbor_dist
                cur_v = closest_neighbor

            cur_total += self.get_distance(cur_v, starting_v)  # add the distance from the final vertex to the first

            if cur_total < best_so_far:
                best_so_far['total'] = cur_total
                best_so_far['order'] = cur_tour

            assert best_so_far['total'] != float('infinity')

        return best_so_far
