class FileWriter:

    output_file_path = 'Output/MSS_Results.txt'
    output_file = None

    def __init__(self):
        self.output_file = open(self.output_file_path, 'w')

    def __delete__(self, instance):
        if self.output_file:
            self.output_file.close()

    def write_line(self, output):
        self.output_file.write(str(output))
        self.output_file.write('\n')
