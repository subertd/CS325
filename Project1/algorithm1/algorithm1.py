__author__ = 'Don'

def enumeration(array_list):
    max_p = None
    max_r = None
    max_sum = None

    for i in range(0, len(array_list)):
        for j in range(i, len(array_list)):
            sub_sum = sum(array_list[i:j + 1])
            if max_sum == None:
                max_sum = sub_sum
                max_p = i
                max_r = j + 1
            else:
                if sub_sum > max_sum:
                    max_sum = sub_sum
                    max_p = i
                    max_r = j + 1
                else:
                    pass

    return (max_p, max_r, max_sum)
