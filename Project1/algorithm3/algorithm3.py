def divide_and_conquer(array_list):
    (p, r, max_sum) = recursive_mms(array_list, 0, len(array_list))
    return p, r, max_sum


def recursive_mms(array_list, p, r):

    if p == r - 1:
        return [p, r, array_list[p]]

    q = (r + p) / 2

    (left_low, left_high, left_sum) = recursive_mms(array_list, p, q)
    (right_low, right_high, right_sum) = recursive_mms(array_list, q, r)
    (cross_low, cross_high, cross_sum) = max_crossing_subarray(array_list, p, q, r)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum

    elif right_sum > left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum

    else:
        return cross_low, cross_high, cross_sum


def max_crossing_subarray(array_list, p, q, r):

    max_left = None
    left_sum = float('-inf')

    for i in range(p, q):

        current_sum = sum(array_list[i:q])

        if current_sum > left_sum:
            max_left = i
            left_sum = current_sum

    max_right = None
    right_sum = float('-inf')

    for i in range(q, r):

        current_sum = sum(array_list[q:i + 1])

        if current_sum > right_sum:
            max_right = i + 1
            right_sum = current_sum

    return [max_left, max_right, left_sum + right_sum]
