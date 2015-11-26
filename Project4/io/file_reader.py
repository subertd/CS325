

class FileReader:

    file = None

    def __init__(self, path):
        if path is None or path == '':
            raise Exception()

        self.file = open(path, 'r')

    def get_input(self):
        input_data = {}

        for line in self.file:
            tokens = line.split()
            input_data[int(tokens[0])] = (int(tokens[1]), int(tokens[2]))

        return input_data
