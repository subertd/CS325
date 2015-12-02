make clean
make
./main -f test-input-2.txt
python tsp-verifier.py test-input-2.txt test-input-2.txt.tour

