from console_reader.console_reader import ConsoleReader
from file_reader.file_reader import FileReader
from file_writer.file_writer import FileWriter
from algorithm3.algorithm3 import changedp

consoleReader = ConsoleReader()
file_name = consoleReader.get_user_input_file_name()

fileReader = FileReader(file_name + ".txt")
data = fileReader.read_data()
fileReader.close()

fileWriter = FileWriter(file_name + "change.txt")

for i in data:
    V, A = i
    result = changedp(V, A)
    fileWriter.write_line(result)

fileWriter.close()
