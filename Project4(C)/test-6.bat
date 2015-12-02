make clean
make
./main -f test-input-6.txt
python tsp-verifier.py test-input-6.txt test-input-6.txt.tour

