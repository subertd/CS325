import json

__author__ = 'Don'


def load_list_from_json_file(file_path):

    list_file = open(file_path, 'r')

    json_list = ''

    for line in list_file:
        json_list += line

    list_file.close()

    unsorted_list = json.loads(json_list)

    return unsorted_list
