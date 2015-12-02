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


#ifndef max
// citation: forums.devshed.com/programming-42/max-function-436555.html
#define max(a, b) ( ((a) > (b)) ? (a) : (b) )
#endif


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
void compute_total(struct solution *s, struct v *v, struct e *e);


struct solution nearest_neighbor(struct v *v, struct e *e);
struct solution two_opt(struct solution solution, struct v *v, struct e *e);
struct solution two_opt_swap(struct solution solution, struct v *v, struct e *e, int i, int j);

//void set_edge(struct e *e, int u, int v, int distance);
//int get_edge(struct e *e, int u, int v);

void print_solution(char *file_name, struct solution *s) {

  //printf("entering print_solution(%s)\n", file_name);
 
  strcat(file_name, ".tour");

  //printf("successfully concatenated file name\n");

  FILE *fp = fopen(file_name, "w");

  fprintf(fp, "%d\n", s->total);

  //printf("successfully printed the total, %d\n", s->total);

  for (int i = 0; i < s->size; ++i) {
    fprintf(fp, "%d\n", s->order[i]);
    //printf("successfully printed s->order[%d], %d\n", i, s->order[i]);
  }

  fclose(fp);

  //printf("exiting print_solution()\n");
}

/*
 * The insertion point
 */
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
  s = two_opt(s, &v, &e);

  stop_time = time(NULL);
  printf("started at %ld, ended at %ld, duration: %lf seconds\n",
    (long)start_time, (long)stop_time, difftime(stop_time, start_time));

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

struct solution two_opt(struct solution s, struct v *v, struct e *e) {

  int size = s.size;
  struct solution temp_s, better_s = s;

  int improvement_made = 0;
  //int swap_threshold = max(5001 -  size, 0);
  int swap_threshold = 30;
  int num_swaps = 0;

  for (int i = 0; i < size - 1; ++i) {
    for (int j = i + 1; j < size; ++j) {
      temp_s = two_opt_swap(better_s, v, e, i, j);

      if (temp_s.total < better_s.total) {
        better_s = temp_s;
        ++num_swaps;
      }

      if (num_swaps > swap_threshold) {
        break;
      }
    }

    if (num_swaps > swap_threshold) {
      break;
    }
  }
  return better_s;
}

struct solution two_opt_swap(struct solution s, struct v *v, struct e *e, int i, int j) {

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

  compute_total(&new_s, v, e);

  //print_solution("TEST.txt", &new_s);
  //exit(EXIT_SUCCESS);
 
  return new_s;
}

void compute_total(struct solution *s, struct v *v, struct e *e) {
  
  int size = s->size;
  int total = 0;
  int cur, next;

  for (int i = 0; i < size; ++i) {
    cur = s->order[i];
    next = s->order[(i + 1) % size];
    total += get_distance(v, e, cur, next);
  }

  s->total = total;
}

void set_edge(struct e *e, int u, int v, int distance) {

  
}
