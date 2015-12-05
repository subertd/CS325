to run the program, first build it with the command:
  $ make

next, execute the program with*:
  $ ./main -f <filename>

*where <filename> is the name of a file in the same directory as the project files. For example, to use the file test-input-1.txt, use:
  $ ./main -f test-input-1.txt

The output will be contained in a file <filename>.tour, in the same directory.

To remove all generated files, use the command:
  $ make clean

To clean, compile, run, and verify all 10 of the provided files**, simply use:
  $ ./test_all.bat

** You will either need to verify that this script is valid or just take my word for it.
