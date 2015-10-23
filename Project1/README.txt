This file contains instructions for running the executable application files of Project1. There are many files which drive unit tests. Running these files is not in the scope of this document.

The app.py file does the following:
 * loads a file Problems/MSS_Problems.txt
 * parses each of the provided lists
 * for each list, solves for max subarray with each of the 4 algorithms
 * outputs the solutions to the console
 * outputs the solutions to the file Output/MSS_Results.txt

This file is run from the project root directory with the command:
  $ python app.py




The experiment.py file does the following:
 * generates a series of 100 test arrays for each of 10 n (where n is customized for each algorithm)
 * solves each list for maximum subarray for each algorithm
 * determines the collective execution time for 100 runs for each algorithm, for each value of n
 * output the execution times in csv format to the console
 * outputs the execution times in csv format to the file Output/ExperimentalData.txt

This file is run from the project root directory with the command:
  $ python experiment.py




The clean.bat file does the following:
 * deletes the file Output/MSS_Results.txt
 * deletes the file Output/ExperimentalData.txt

This file is run from the project root directory with the command:
  $ ./clean.bat
