#include "file_reader.h"
#include <stdio.h>
#include <stdlib.h>

void read_file_lines(const char *fileName, LineHandler handler)
{
    FILE *fptr;
    size_t len = 100;
    char *line = NULL;

    fptr = fopen(fileName, "r");
    if (fptr != NULL)
    {
        line = (char *)malloc(len * sizeof(char));

        while (fgets(line, len, fptr))
        {
            handler(line);
        }

        free(line);
        fclose(fptr);
    }
    else
    {
        printf("Not able to open the file.");
        return;
    }
}
