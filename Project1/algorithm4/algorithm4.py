def dynamic_programming(array_list):
    max_sum = float('-inf')
    ending_here_sum = float('-inf')
    low = None
    high = None
    ending_here_low = None
    ending_here_high = None

    for i in range(0, len(array_list)):
        ending_here_high = i
        if ending_here_sum > 0:
            ending_here_sum += array_list[i]
        else:
            ending_here_low = i
            ending_here_sum = array_list[i]

        if ending_here_sum > max_sum:
            max_sum = ending_here_sum
            low = ending_here_low
            high = ending_here_high

    return low, high + 1, max_sum
