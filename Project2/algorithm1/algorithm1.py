def changeslow(V, K):

    possibilities = []

    for i in range(0, len(V)):
        if K == V[i]:
            denominations = [0] * len(V)
            denominations[i] = 1
            return denominations, 1

    for i in range(0, len(V)):
        if V[i] < K:
            coins_i = changeslow(V, V[i])
            coins_K_less_i = changeslow(V, K - V[i])

            possibilities.append(sum_coins(coins_i, coins_K_less_i))

    return min_coins(possibilities)

def sum_coins(a, b):
    a_denominations, a_total = a
    b_denominations, b_total = b

    sum_denominations = [0] * len(a_denominations)
    sum_total = a_total + b_total

    for i in range(0, len(a_denominations)):
        sum_denominations[i] = a_denominations[i] + b_denominations[i]

    return sum_denominations, sum_total

def min_coins(possibilities):
    min_so_far = float("inf")
    min_so_far_index = None

    if (possibilities == []):
        print("TEST TEST TEST")

    for i in range(0, len(possibilities)):
        cur_denominations, cur_total = possibilities[i]
        if cur_total < min_so_far:
            min_so_far = cur_total
            min_so_far_index = i

    return possibilities[min_so_far_index]
