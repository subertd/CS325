from algorithm.tsp_algorithm import TSPAlgorithm


class RealTSPAlgorithm(TSPAlgorithm):

    IMPROVEMENT_THRESHOLD = 10

    graph = None

    def __init__(self):
        TSPAlgorithm.__init__(self)

    def solve(self, graph):

        self.graph = graph

        solution = self.get_nearest_neighbor_solution()

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
            running_total += e[(cur_v, next_v)]

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
                    dist = e[(cur_v, neighbor)]
                    if dist < closest_neighbor_dist:
                        closest_neighbor = neighbor
                        closest_neighbor_dist = dist

                assert closest_neighbor is not None

                cur_tour.append(closest_neighbor)
                cur_total += closest_neighbor_dist
                cur_v = closest_neighbor

            cur_total += e[(cur_v, starting_v)]

            if cur_total < best_so_far:
                best_so_far['total'] = cur_total
                best_so_far['order'] = cur_tour

            assert best_so_far['total'] != float('infinity')

        return best_so_far
