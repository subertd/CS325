make clean
make

echo "tsp_example_1.txt\n"
./main -f tsp_example_1.txt
python tsp-verifier.py tsp_example_1.txt tsp_example_1.txt.tour

echo "tsp_example_2.txt\n"
./main -f tsp_example_2.txt
python tsp-verifier.py tsp_example_2.txt tsp_example_2.txt.tour

echo "tsp_example_3.txt\n"
./main -f tsp_example_3.txt
python tsp-verifier.py tsp_example_3.txt tsp_example_3.txt.tour

echo "test-input-1.txt"
./main -f test-input-1.txt
python tsp-verifier.py test-input-1.txt test-input-1.txt.tour

echo "test-input-2.txt"
./main -f test-input-2.txt
python tsp-verifier.py test-input-2.txt test-input-2.txt.tour

echo "test-input-3.txt"
./main -f test-input-3.txt
python tsp-verifier.py test-input-3.txt test-input-3.txt.tour

echo "test-input-4.txt"
./main -f test-input-4.txt
python tsp-verifier.py test-input-4.txt test-input-4.txt.tour

echo "test-input-5.txt"
./main -f test-input-5.txt
python tsp-verifier.py test-input-5.txt test-input-5.txt.tour

echo "test-input-6.txt"
./main -f test-input-6.txt
python tsp-verifier.py test-input-6.txt test-input-6.txt.tour

echo "test-input-7.txt"
./main -f test-input-7.txt
python tsp-verifier.py test-input-7.txt test-input-7.txt.tour
