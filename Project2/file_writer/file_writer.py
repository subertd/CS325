import sys


class FileWriter:

    output_file = None

    def __init__(self, output_file_path):
        self.output_file = open(output_file_path, 'w')

    def __delete__(self):
        if self.output_file:
            self.output_file.close()

    def write(self, output):
        self.output_file.write(output)
        sys.stdout.write(output)
        sys.stdout.flush()

    def flush(self):
        self.output_file.flush()
        sys.stdout.flush()

    def write_line(self, output):
        self.write(str(output))
        self.write('\n')
        self.flush()

    def close(self):
        self.output_file.close()
