#include <stdio.h>
#include "../common/file_reader.h"

// Implement the line handler function
void handle_line(const char *line)
{
    printf("%s", line);
}

int main(int argc, char *argv[])
{
    const char *fileName = "input.txt"; // Name of the file to read

    // Call the function from the file_reader.c file
    read_file_lines(fileName, handle_line);

    return 0;
}