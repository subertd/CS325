from algorithm1.algorithm1 import enumeration
from algorithm2.algorithm2 import better_enumeration
from algorithm3.algorithm3 import divide_and_conquer
from file_loader.file_loader import load_list_from_csv


test = load_list_from_csv('Problems/MSS_TestProblems-1.txt')

#print test
for list in test:
    print enumeration(list)
    print better_enumeration(list)
    print divide_and_conquer(list)