

class FileWriter:

    FILE_FORMAT = "%s.tour"

    def __init__(self, path):
        open(self.FILE_FORMAT % path, 'w')

    def write_file(self, output_string):
        pass
