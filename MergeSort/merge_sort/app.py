from file_loader.file_loader import load_list_from_json_file
from merge_sort import merge_sort

__author__ = 'Don'


unsorted_list = load_list_from_json_file("../list1.json")

sorted_list = merge_sort(unsorted_list)

print sorted_list
