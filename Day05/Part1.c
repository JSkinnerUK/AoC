#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../common/file_reader.h"

char stacks[9][128];

void setup_stacks(FILE *fptr) {
    char **lines = NULL;
    char line[256];
    size_t line_count = 0;
    while (fgets(line, sizeof(line), fptr)) {
        lines = realloc(lines, (line_count + 1) * sizeof(char *));
        lines[line_count] = strdup(line);
        line_count++;
        if (line[1] == '1') {
            break;
        }
    } 

    for(int i = 1; i < line_count; i++) {
        char *currentLine = lines[line_count -1 - i];
        int j = 0;
        while (currentLine[j] != '\0') {
            if(j % 4 == 1) {
                if(currentLine[j] != ' ') {
                    stacks[j / 4][i-1] = currentLine[j];
                } else {
                    stacks[j / 4][i-1] = '\0';
                }
            }
            j++;
        }
        for(int l = 0; l < 7; l++) {
            stacks[l][i] = '\0';
        }
    }

}

char* get_result(char stacks[][128], int stack_count) {
    char *res = (char *)malloc(stack_count +1);
    for(int i = 0; i < stack_count; i++) {
        int length = strlen(stacks[i]);
        res[i] = stacks[i][length-1];
    }
    res[stack_count] = '\0';
    return res;
}

char pop(char *stack) {
    int length = strlen(stack);
    char last = stack[length - 1];
    stack[length - 1] = '\0';
    return last;
}

void push(char chr, char *stack) {
    int length = strlen(stack);
    stack[length] = chr;
    stack[length+1] = '\0';
}


int main(int argc, char *argv[])
{
    const char *fileName = "input_files/adventofcode.com_2022_day_5_input.txt"; 
    FILE *fptr;
    fptr = fopen(fileName, "r");
    char line[256];

    if (fptr != NULL)
    {
        setup_stacks(fptr);

        int amount, from, to;
        int count = 0;
        while ((count = fscanf(fptr, "move %d from %d to %d", &amount, &from, &to)) != EOF) {
            if (count == 3) {
                for(int i = 0; i < amount; i++) {
                    push(pop(stacks[from -1]), stacks[to - 1]);
                }
            } else {
                fgets(line, sizeof(line), fptr);
            }
        }

        printf("%s", get_result(stacks, sizeof(stacks) / sizeof(stacks[0])));
    }
    else
    {
        printf("Not able to open the file.");
        return 1;
    }

    fclose(fptr);
    return 0;
}
