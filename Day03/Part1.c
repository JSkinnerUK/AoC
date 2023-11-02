#include <stdio.h>
#include <string.h>
#include "file_reader.h"

void handle_line(const char* line) {
    printf("%s", line);
}

int main() {
    read_file_lines("input.txt", handle_line);
}