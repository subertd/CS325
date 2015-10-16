from random_list_gen.random_list_gen import RandomListGen


random_list_gen = RandomListGen()

random_lists = random_list_gen.get_lists(10, 10)

print str(random_lists)