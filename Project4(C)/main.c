#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define MAX_INPUT_LENGTH 16000

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

  FILE *fp;
  char *line = NULL;
  
  fp = fopen(input_file_name, "r");
  if (fp == NULL) {
    fprintf(stderr, "File not found%s\n", input_file_name);
    exit(EXIT_FAILURE);
  }

  int id, x, y, i = 0;
  while(fscanf(fp, "%d %d %d\n", &id, &x, &y) != EOF) {
    // printf("Vertex %d, is at (%d, %d)\n", id, x, y);
    p->id[i] = id;
    p->x[i] = x;
    p->y[i] = y;
    ++i;
  }
  p->size = i;

  fclose(fp);
  if (line)
    free(line);
}
