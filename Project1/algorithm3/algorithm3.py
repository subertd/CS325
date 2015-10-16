def divide_and_conquer(array_list):
    return recursive_mms(array_list, 0, len(array_list))


def recursive_mms(array_list, p, r):

    if p == r:
        return [p, r, array_list[p]]

    q = (r - p) // 2

    #prefix = recursive_mms(array_list, p, q)
    #suffix = recursive_mms(array_list, q, r)

    return max_crossing_subarray(array_list, p, q, r)


 def max_crossing_subarray(array_list, p, q, r):
     pass
