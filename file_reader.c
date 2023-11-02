#include <stdio.h>
#include "file_reader.h"

void read_file_lines(const char* fileName, LineHandler handler) {
    FILE *fptr;
    fptr = fopen(fileName, "r");
    if (fptr != NULL) {
        char *line = NULL;

        while (fgets(line, sizeof(line), fptr)) {
            handler(line);
        }
    } else {
        printf("Not able to open the file.");
    }

    fclose(fptr);
}
