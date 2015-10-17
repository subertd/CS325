__author__ = 'Don'

def better_enumeration(array_list):
    max_p = None
    max_r = None
    max_sum = None

    for i in range(0, len(array_list)):
        old_sum = None
        for j in range(i, len(array_list)):
            if old_sum == None:
                sub_sum = array_list[j]
            else:
                sub_sum = old_sum + array_list[j]

            if max_sum == None:
                max_sum = sub_sum
                max_p = i
                max_r = j + 1

            else:
                if sub_sum >= max_sum:
                    max_sum = sub_sum
                    max_p = i
                    max_r = j + 1

            old_sum = sub_sum

    return (max_p, max_r, max_sum)