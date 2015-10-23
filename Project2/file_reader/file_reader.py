import csv
import StringIO


class FileReader:

    input_file = None

    def __init__(self, input_file_path):
        self.input_file = open(input_file_path, 'r')

    def __delete__(self):
        if self.input_file:
            self.input_file.close()

    def read_data(self):
        list_of_tuples = []
        line_count = 0

        for line in self.input_file:
            # Even-numbered lines are lists of coins
            if line_count % 2 == 0:
                list_of_coins = line[1:-2].split(',')
                list_of_int_coins = []

                for coin in list_of_coins:
                    coin = int(coin)
                    list_of_int_coins.append(coin)

                list_of_tuples.append(list_of_int_coins)

            # Odd-numbered lines are target numbers
            else:
                int_line = line.rstrip('\n')
                int_line = int(int_line)
                list_of_tuples[len(list_of_tuples) - 1] = (list_of_tuples[len(list_of_tuples) - 1], int_line)

            line_count += 1

        return list_of_tuples

    def close(self):
        self.input_file.close()
