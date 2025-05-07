#include "encoding.h"
#include "fec.h"
#include <stdio.h>
#include <stdlib.h>

#define BUFFERSIZE 65536

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <fec-file>\n", argv[0]);
        return 1;
    }

    FILE *handle = fopen(argv[1], "rb");
    if (!handle) {
        perror("fopen");
        return 1;
    }

    PERSISTENT_MEMORY_CONTEXT *pm = newPersistentMemoryContext();

    // hardcoded dummy values
    const char *fecId      = "FUZZ123";
    const char *outDir     = ".";        // random dir for parser to spit out csvs, useless for our testing
    int includeFilingId    = 0;
    int silent             = 1;          // ignore stdout
    int warn               = 0;

    FEC_CONTEXT *fec = newFecContext(pm, (BufferRead)&readBuffer, BUFFERSIZE, NULL, BUFFERSIZE, NULL, 1, handle, fecId, outDir, includeFilingId, silent, warn);

    parseFec(fec);

    freeFecContext(fec);
    freePersistentMemoryContext(pm);
    fclose(handle);
    return 0;
}