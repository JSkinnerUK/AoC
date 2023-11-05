#include <stdio.h>
#include <string.h>
#include "../common/file_reader.h"

int total = 0;

void handle_line(const char *line) {
    int elf1S, elf1E, elf2S, elf2E;

    sscanf(line, "%d-%d,%d-%d", &elf1S, &elf1E, &elf2S, &elf2E);

    if(elf1S <= elf2E && elf2S <= elf1E) {
        total += 1;
    }
}

int main(int argc, char *argv[])
{
    const char *fileName = "input_files/adventofcode.com_2022_day_4_input.txt"; // Name of the file to read

    // Call the function from the file_reader.c file
    read_file_lines(fileName, handle_line);

    printf("%d\n", total);
    return 0;
}
