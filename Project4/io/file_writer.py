

class FileWriter:

    FILE_FORMAT = "%s.tour"

    file = None

    def __init__(self, path):
        self.file = open(self.FILE_FORMAT % path, 'w')

    def write_file(self, output_string):
        self.file.write(output_string)
