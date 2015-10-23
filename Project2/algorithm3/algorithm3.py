counter = []

def changedp(V, A):
    global counter
    counter = [None] * (A + 1)
    counter[0] = [0] * len(V), 0

    return recursive_changedp(V, A)


def recursive_changedp(V, K):
    global counter

    for i in range(1, K + 1):
        q = float("inf")
        q_denominations = [0] * len(V)

        for v in range(0, len(V)):
            if V[v] <= i:
                counter_denominations, counter_total = counter[i - V[v]]
                if counter_total + 1 < q:
                    q = counter_total + 1
                    q_denominations = increment(counter_denominations, v)

        counter[i] = (q_denominations, q)

    return counter[K]

def increment(denominations, v):
    new_denom = [0] * len(denominations)
    for i in range(0, len(denominations)):
        new_denom[i] = denominations[i]
        if i == v:
            new_denom[i] += 1
    return new_denom
