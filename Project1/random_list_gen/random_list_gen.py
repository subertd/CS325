import random


class RandomListGen:

    min = -100
    max = 100

    def __init__(self):
        pass

    def get_list(self, len_list):

        cur_list = []

        for j in range(0, len_list):
            cur_list.append(random.randrange(self.min, self.max))

        return cur_list

    def get_lists(self, num_lists, len_lists):

        list_of_lists = []

        for i in range(0, num_lists):
            list_of_lists.append(self.get_list(len_lists))

        return list_of_lists
