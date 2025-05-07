#include "encoding.h"
#include "fec.h"
#include "cli.h"
#include <unistd.h>

#define BUFFERSIZE 65536


int main(int argc, char *argv[])
{
  if (argc < 2) {
    fprintf(stderr, "Usage: %s <fec-file>\n", argv[0]);
    return 1;
  }
    
  // Create fake CLI context
  CLI_CONTEXT *cli = newCliContext();
  cli->outputDirectory = "./csv_output"; // garbage output we don't need for fuzzing
  cli->fecId = argv[1]; 
  cli->fecName = argv[1]; 
  cli->silent = 1; // dont waste time trying to print anything
  cli->warn = 0; // dont waste time trying to print warnings
  cli->piped = 0;
  cli->includeFilingId = 0;
  cli->printUrl = 0;
  cli->shouldPrintUsage = 0;
  cli->shouldPrintSpecifyFilingId = 0;
  cli->shouldPrintUrlOnly = 0;


  // Open File
  FILE *handle = fopen(argv[1], "rb");
  if (!handle) {
    perror("fopen");
    return 1;
  }

  // Initialize persistent memory context
  PERSISTENT_MEMORY_CONTEXT *persistentMemory = newPersistentMemoryContext();

  // Initialize FEC context
  FEC_CONTEXT *fec = newFecContext(persistentMemory, ((BufferRead)(&readBuffer)), BUFFERSIZE, NULL, BUFFERSIZE, NULL, 1, handle, cli->fecId, cli->outputDirectory, cli->includeFilingId, cli->silent, cli->warn);

  // Parse the fec file
  parseFec(fec);

  // Clean up
  freeFecContext(fec);
  freePersistentMemoryContext(persistentMemory);
  freeCliContext(cli);
  fclose(handle);

  return 0; /* all done */
}