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
#define IMPROVEMENT_THRESHOLD 20

struct v {
  int id[MAX_INPUT_LENGTH];
  int x[MAX_INPUT_LENGTH];
  int y[MAX_INPUT_LENGTH];
  int size;
};

struct solution {
  int total;
  int order[MAX_INPUT_LENGTH];
  int size;
};

void get_file_input(char *input_file_name, struct v *v);
void print_solution(char *file_name, struct solution *s);
int get_distance(struct v *v, int uid, int vid);
void compute_total(struct solution *s, struct v *v);

struct solution nearest_neighbor(struct v *v);
struct solution two_opt(struct solution solution, struct v *v);
struct solution two_opt_swap(struct solution solution, struct v *v, int i, int j);

/*
 * The insertion point
 */
int main(int argc, char** argv) {

  struct timeval tval_before, tval_after, tval_result;

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
  get_file_input(file_name, &v);

  gettimeofday(&tval_before, NULL);

  struct solution s = nearest_neighbor(&v);
  s = two_opt(s, &v);

  gettimeofday(&tval_after, NULL);
  timersub(&tval_after, &tval_before, &tval_result);
  printf("started at %ld, ended at %ld, duration: %ld.%ld seconds\n",
      (long)tval_before.tv_sec, (long)tval_after.tv_sec,
      (long)tval_result.tv_sec, (long)tval_result.tv_usec);

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

void print_solution(char *file_name, struct solution *s) {

  strcat(file_name, ".tour");

  FILE *fp = fopen(file_name, "w");

  fprintf(fp, "%d\n", s->total);

  for (int i = 0; i < s->size; ++i) {
    fprintf(fp, "%d\n", s->order[i]);
  }

  fclose(fp);
}

int get_distance(struct v *v, int u, int t) {
  
  int ux = v->x[u];
  int uy = v->y[u];
  int tx = v->x[t];
  int ty = v->y[t];

  return (int)round(sqrt(pow(abs(ux - tx), 2) + pow(abs(uy - ty), 2)));
}

struct solution nearest_neighbor(struct v *v) {

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
      int cur_dist = get_distance(v, cur_vertex, unvisited[j]);

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

  s.total += get_distance(v, cur_vertex, s.order[0]); // add the distance between the last and first vertices

  return s;
}

struct solution two_opt(struct solution s, struct v *v) {

  int size = s.size;
  struct solution temp_s, better_s = s;
  int swap_limit =  (int)((0 - .00000045) * pow(size - 3700, 3)) + 1030;
  printf ("%d improvements attempted\n", swap_limit);
  int num_swaps = 0;

  for (int i = 0; i < size - 1; ++i) {
    for (int j = i + 1; j < size; ++j) {
      temp_s = two_opt_swap(better_s, v, i, j);

      if (temp_s.total < better_s.total) {
        better_s = temp_s;
        ++num_swaps;
      }

      if (num_swaps > swap_limit) {
        break;
      }
    }

    if (num_swaps > swap_limit) {
      break;
    }
  }
  return better_s;
}

struct solution two_opt_swap(struct solution s, struct v *v, int i, int j) {

  struct solution new_s;
  new_s.size = s.size;
  int size = s.size;

  for (int h = 0; h < i; ++h) {
    new_s.order[h] = s.order[h];
  }

  for (int h = i; h <= j; ++h) {
    new_s.order[h] = s.order[j - h + i];
  }

  for (int h = j + 1; h < size; ++h) {
    new_s.order[h] = s.order[h];
  }

  compute_total(&new_s, v);

  return new_s;
}

void compute_total(struct solution *s, struct v *v) {
  
  int size = s->size;
  int total = 0;
  int cur, next;

  for (int i = 0; i < size; ++i) {
    cur = s->order[i];
    next = s->order[(i + 1) % size];
    total += get_distance(v, cur, next);
  }

  s->total = total;
}
