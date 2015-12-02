make clean
make
./main -f test-input-7.txt
python tsp-verifier.py test-input-7.txt test-input-7.txt.tour

