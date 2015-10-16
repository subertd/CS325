import csv
import StringIO


def load_lists_from_file(file_path):

    list_file = open(file_path, 'r')

    list_of_csvs = []

    for line in list_file:
        list_of_csvs.append(line[1:-2])

    list_file.close()

    list_of_lists = []


    for csv_string in list_of_csvs:

        cur_list = []

        csv_reader = csv.reader(StringIO.StringIO(csv_string), delimiter=',', quotechar='|')
        for row in csv_reader:
            for element in row:
                try:
                    num_format_element = int(element)
                    cur_list.append(num_format_element)
                except ValueError:
                    pass
                finally:
                    pass

        if len(cur_list) > 0:
            list_of_lists.append(cur_list)

    return list_of_lists
