import sys


class FileWriter:

    output_file = None

    def __init__(self, output_file_path):
        self.output_file = open(output_file_path, 'w')

    def __delete__(self):
        if self.output_file:
            self.output_file.close()

    def write(self, output):
        self.output_file.write(str(output))
        sys.stdout.write(str(output))
        sys.stdout.flush()

    def write_line(self, output):
        self.write(str(output))
        self.write('\n')

    def write_result(self, output):
        self.write(str(output[0]))
        self.write('\n')
        self.write(str(output[1]))
        self.write('\n')

    def close(self):
        self.output_file.close()
