

class FileReader:

    file = None

    def __init__(self, path):
        if path is None or path == '':
            raise Exception()

        self.file = open(path, 'r')

    def get_input(self):
        input_data = []

        for line in self.file:
            input_data.append(line.split())

        return input_data
