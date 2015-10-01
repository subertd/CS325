__author__ = 'Don'


def merge_sort(unsorted_list):

    length = len(unsorted_list)

    if length <= 1:
        return unsorted_list

    middle = get_middle(length)

    a = merge_sort(unsorted_list[0:middle])
    b = merge_sort(unsorted_list[middle:length])

    return merge(a, b)


def get_middle(length):

    return length // 2


def merge(a, b):

    i = 0
    j = 0
    merged = []

    while i < len(a) or j < len(b):
        if i == len(a):
            merged.append(b[j])
            j += 1
        elif j == len(b):
            merged.append(a[i])
            i += 1
        else:
            a_top = a[i]
            b_top = b[j]
            if a_top < b_top:
                merged.append(a_top)
                i += 1
            else:
                merged.append(b_top)
                j += 1

    return merged
