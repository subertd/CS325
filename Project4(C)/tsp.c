#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define MAX_INPUT_LENGTH 256
#define MAX_PROBLEM_SIZE 16000

struct problem {
  int id[MAX_INPUT_LENGTH];
  int x[MAX_INPUT_LENGTH];
  int y[MAX_INPUT_LENGTH];
  int size;
};

void get_file_input(char *input_file_name, struct problem *p);

int main(int argc, char** argv) {

  struct problem p;
  get_file_input("test-input-1.txt", &p);

  return EXIT_SUCCESS;
}

void get_file_input(char *input_file_name, struct problem *p) {

  FILE *ifp;
  char line[MAX_INPUT_LENGTH];

  while ((c = getc(ifp)) != EOF) {

  }


  ifp = fopen(input_file_name, "r");
  if (ifp == NULL) {
    fprintf(stderr, "File not found\n");
    exit(EXIT_FAILURE);
  }

  while(fgets(line, sizeof line, ifp) != NULL) {
    printf("%s", line);



  }

  fclose(ifp);
}
