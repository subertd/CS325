from console_reader.console_reader import ConsoleReader
from file_reader.file_reader import FileReader
from file_writer.file_writer import FileWriter
from algorithm1.algorithm1 import changeslow
from algorithm2.algorithm2 import changegreedy
from algorithm3.algorithm3 import changedp

consoleReader = ConsoleReader()
file_name = consoleReader.get_user_input_file_name()

fileReader = FileReader(file_name + ".txt")
data = fileReader.read_data()
fileReader.close()

fileWriter = FileWriter(file_name + "change.txt")

for i in data:
    V, A = i

    fileWriter.write_line("for problem:")
    fileWriter.write_result((V, A))
    fileWriter.write_line("results are: \n")

    result = changeslow(V, A)
    fileWriter.write("changeslow:\n")
    fileWriter.write_result(result)

    result = changegreedy(V, A)
    fileWriter.write("changegreedy:\n")
    fileWriter.write_result(result)

    result = changedp(V, A)
    fileWriter.write("changedp:\n")
    fileWriter.write_result(result)

    fileWriter.write_line("----------------------")

fileWriter.close()
