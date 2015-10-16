__author__ = 'Don'

def enumeration(array_list):
    max_sum = 0

    for i in range(0, len(array_list)):
        for j in range(i, len(array_list)):
            sub_sum = sum(array_list[i:j + 1])
            if max_sum == None:
                max_sum = sub_sum
            else:
                if sub_sum > max_sum:
                    max_sum = sub_sum
                else:
                    pass

    return max_sum