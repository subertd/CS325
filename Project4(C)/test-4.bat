make clean
make
./main -f test-input-4.txt
python tsp-verifier.py test-input-4.txt test-input-4.txt.tour

