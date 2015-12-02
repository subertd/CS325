make clean
make
./main -f test-input-3.txt
python tsp-verifier.py test-input-3.txt test-input-3.txt.tour

