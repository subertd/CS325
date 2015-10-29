from file_writer.file_writer import FileWriter
from problem4.problem4 import Problem4
from problem5.problem5 import Problem5
from problem6.problem6 import Problem6


time_out = FileWriter('Problem7Output.csv')

problem4 = Problem4(time_out)
problem5 = Problem5(time_out)
problem6 = Problem6(time_out)
problem8 = Promblem8()

problem4.run()
problem5.run()
problem6.run()
problem8.run()

time_out.close()
