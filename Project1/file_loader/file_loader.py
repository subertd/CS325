import json
import csv
import StringIO

__author__ = 'Don'


def load_list_from_json_file(file_path):

    list_file = open(file_path, 'r')

    json_list = ''

    for line in list_file:
        json_list += line

    list_file.close()

    unsorted_list = json.loads(json_list)

    return unsorted_list


def load_list_from_csv(file_path):

    list_file = open(file_path, 'r')

    list_of_csvs = []

    for line in list_file:
        list_of_csvs.append(line[1:-2])

    list_file.close()

    list_of_lists = []


    for csv_string in list_of_csvs:

        cur_list = []

        csv_reader = csv.reader(StringIO.StringIO(csv_string), delimiter=',', quotechar='|')
        #while csv_reader.next():
         #   print csv_reader[0]
        for row in csv_reader:
            #cur_list.append((list(row), row[0]))
            for element in row:
                try:
                    num_format_element = int(element)
                    cur_list.append(num_format_element)
                except ValueError:
                    pass
                finally:
                    pass

        list_of_lists.append(cur_list)

    return list_of_lists
