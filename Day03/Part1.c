#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>
#include "../common/file_reader.h"

int total = 0;

char find_errors(char *comp1, char *comp2, int maxSize) {

    for(int i = 0; i < strlen(comp1); i++) {
        for(int j = 0; j < strlen(comp2); j++) {
            if(comp1[i] == comp2[j]) {
                return comp1[i];
            }    
        }
    }
    return '\0';
}

// Implement the line handler function
void handle_line(const char *line)
{
    size_t length = strlen(line) - 1;

    char *comp1 = (char *)malloc(length / 2 + 1);
    char *comp2 = (char *)malloc(length / 2 + 1);

    strncpy(comp1, line, length / 2);
    comp1[length / 2] = '\0';

    strncpy(comp2, line + length / 2, length / 2);
    comp2[length / 2] = '\0';
    char x = find_errors(comp1, comp2, length / 2);

    int asciiVal = x;
    if (asciiVal >= 97) {
        asciiVal -= 96;
    } else {
        asciiVal -= 64 - 26;
    }

    total+=asciiVal;

    free(comp1);
    free(comp2);
}

int main(int argc, char *argv[])
{
    const char *fileName = "input_files/adventofcode.com_2022_day_3_input.txt"; // Name of the file to read

    // Call the function from the file_reader.c file
    read_file_lines(fileName, handle_line);

    printf("%d\n", total);
    return 0;
}
