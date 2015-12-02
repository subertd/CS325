make clean
make
./main -f test-input-5.txt
python tsp-verifier.py test-input-5.txt test-input-5.txt.tour

