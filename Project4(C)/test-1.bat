make clean
make
./main -f test-input-1.txt
python tsp-verifier.py test-input-1.txt test-input-1.txt.tour

