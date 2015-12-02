#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>
#include <sys/time.h>
#include <time.h>
#define MAX_INPUT_LENGTH 16000

struct v {
  int id[MAX_INPUT_LENGTH];
  int x[MAX_INPUT_LENGTH];
  int y[MAX_INPUT_LENGTH];
  int size;
};

struct e {

};

struct solution {
  int total;
  int order[MAX_INPUT_LENGTH];
  int size;
};

void get_file_input(char *input_file_name, struct v *v);
int get_distance(struct v *v, struct e *e, int uid, int vid);

struct solution nearest_neighbor(struct v *v, struct e *e);
struct solution two_opt(struct solution solution, struct v *v, struct e *e);
struct solution two_opt_swap(struct solution solution, struct v *v, struct e *e);

void set_edge(struct e *e, int u, int v, int distance);
int get_edge(struct e *e, int u, int v);

void print_solution(char *file_name, struct solution *s) {

  strcat(file_name, ".tour");

  FILE *fp = fopen(file_name, "w");

  fprintf(fp, "%d\n", s->total);
  for (int i = 0; i < s->size; ++i) {
    fprintf(fp, "%d\n", s->order[i]);
  }

  fclose(fp);
}

int main(int argc, char** argv) {

  time_t start_time, stop_time;

  char *file_name = NULL;
  char c;

  while (( c = getopt (argc, argv, "f:")) != -1) {
    switch(c) {
    case 'f':
      file_name = optarg;
      break;
    }
  } 

  struct v v; // the set of all vertices
  struct e e; // the set of all edges
  get_file_input(file_name, &v);

  start_time = time(NULL);

  struct solution s = nearest_neighbor(&v, &e);

  stop_time = time(NULL);
  printf("completed in %f seconds\n", difftime(start_time, stop_time));

  print_solution(file_name, &s);

  return EXIT_SUCCESS;
}

void get_file_input(char *input_file_name, struct v *v) {

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
    v->id[i] = id;
    v->x[i] = x;
    v->y[i] = y;
    ++i;
  }
  v->size = i;

  fclose(fp);
  if (line)
    free(line);
}

int get_distance(struct v *v, struct e *e, int u, int t) {
  
  int ux = v->x[u];
  int uy = v->y[u];
  int tx = v->x[t];
  int ty = v->y[t];

  return (int)round(sqrt(pow(abs(ux - tx), 2) + pow(abs(uy - ty), 2)));
}

struct solution nearest_neighbor(struct v *v, struct e *e) {

  struct solution s; // the solution
  s.total = 0; // the total distance in the solution
  s.size = v->size;
  int size = v->size; // the number of vertices
  int unvisited[size]; // the id of each unvisited vertex, or -1 if visited

  // initialize a structure for unvisited vertices
  for (int i = 0; i < size; ++i) {
    unvisited[i] = v->id[i];
  }

  // start with the first vertex
  int cur_vertex = unvisited[0]; 
  s.order[0] = unvisited[0];
  unvisited[0] = -1; // mark the first vertex as visited

  // loop until the entire order is filled
  for (int i = 1; i < size; ++i) { // For each vertex after the first
    int nearest_so_far = -1;
    int nearest_so_far_dist = INT_MAX;
    int nearest_so_far_index = -1;

    // check every unvisited vertex to see if it is the nearest neighbor
    for (int j = 0; j < size; ++j) { // for each vertex
      if (unvisited[j] == -1) { // If the vertex is already visited, don't bother
        continue;
      }

      // get the distance between the current vertex and this neighbor
      int cur_dist = get_distance(v, e, cur_vertex, unvisited[j]);

      // if this is the nearest neighbor yet found, update
      if (cur_dist < nearest_so_far_dist) {
        nearest_so_far_dist = cur_dist;
        nearest_so_far = unvisited[j];
        nearest_so_far_index = j;
      }
    }

    unvisited[nearest_so_far_index] = -1;
    s.order[i] = nearest_so_far; // the nearest neighbor becomes the next vertex in the tour
    cur_vertex = nearest_so_far; // the next vertex to find a neighbor for is the nearest neighbor
    s.total += nearest_so_far_dist; // add the distance between the current vertex and its 
                                    // nearest neighbor to total for the solution
  }

  s.total += get_distance(v, e, cur_vertex, s.order[0]); // add the distance between the last and first vertices

  return s;
}

struct solution two_opt(struct solution solution, struct v *v, struct e *e) {

}

struct solution two_opt_swap(struct solution solution, struct v *v, struct e *e) {

}

void set_edge(struct e *e, int u, int v, int distance) {

  
}
