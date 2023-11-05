#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>
#include "../common/file_reader.h"

int total = 0;

char find_badge(const char *elf1, const char *elf2, const char *elf3) {
    char matching;
    int count = 0;

    for(int i = 0; i < strlen(elf1); i++) {
        for (int j = 0; j < strlen(elf2); j++) {
            for (int k = 0; k < strlen(elf3); k++) {
                if(elf1[i] == elf2[j] && elf2[j] == elf3[k]) {
                    return elf1[i];
                }
            }
        }
    }
    printf("Not found: %s, %s, %s", elf1, elf2, elf3);
    return matching;
}

int char_to_val(char inp) {

    if (inp >= 'a') {
        return inp - 'a' + 1;
    } else {
        return inp - 'A' + 27;
    }
}

void handle_line(const char *line) {
}

int main(int argc, char *argv[])
{
    const char *fileName = "input_files/adventofcode.com_2022_day_3_input.txt"; 
    FILE *fptr;
    fptr = fopen(fileName, "r");
    char lines[3][128];
    int count = 0;
    int total = 0;

    if (fptr != NULL)
    {
        while (fgets(lines[count % 3], sizeof(lines[count % 3]), fptr))
        {
            if(count % 3 == 2) {
                char badge = find_badge(lines[0], lines[1], lines[2]);
                total += char_to_val(badge);
            }
            count++;
        }
    }
    else
    {
        printf("Not able to open the file.");
        return 1;
    }

    printf("%d", total);
    fclose(fptr);
    return 0;
}
