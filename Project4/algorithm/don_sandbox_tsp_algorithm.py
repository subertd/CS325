from algorithm.tsp_algorithm import TSPAlgorithm


class DonsSandboxTSPAlgorithm(TSPAlgorithm):
    def __init__(self):
        TSPAlgorithm.__init__(self)

    def solve(self, graph):

        (v, e) = graph

        best_so_far = {
            'total': float('infinity')
        }

        for starting_v in v:
            unvisited = list(v)
            cur_tour = [starting_v]
            cur_total = 0
            cur_v = starting_v

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
