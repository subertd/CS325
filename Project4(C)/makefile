CC = gcc

CFLAGS = -std=c99
CFLAGS += -g
CFLAGS += -Wall

PROGS = main


all: $(PROGS)

main: main.c
	$(CC) $(CFLAGS) -o main main.c

clean:
	rm -f $(PROGS) *.0 *.tour
