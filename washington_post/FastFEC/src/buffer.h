#pragma once
#include "memory.h"

typedef size_t (*BufferRead)(char *buffer, int want, void *data);

struct buffer
{
  char *buffer;
  int bufferSize;
  int bufferPos;
  int streamStarted;
  BufferRead bufferRead;
};
typedef struct buffer BUFFER;

BUFFER *newBuffer(int bufferSize, BufferRead bufferRead);

// Original Code
// size_t readBuffer(char *buffer, int want, FILE *file);

// Fixed Code
size_t readBuffer(char *buffer, int want, void *data);

size_t fillBuffer(BUFFER *buffer, void *data);

int readLine(BUFFER *buffer, STRING *string, void *data);

void freeBuffer(BUFFER *buffer);
