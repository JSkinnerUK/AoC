#include <stdio.h>
#include <string.h>
#include "../common/file_reader.h"

char queue[5] = {'\0'};
int count = 0;
int found = 0;

void enqueue(char *queue, char inp) {
    int length = strlen(queue);
    queue[length] = inp;

}

char dequeue(char *queue) {
    char first = queue[0];
    int i = 0;
    while (queue[i] != '\0') {
        queue[i] = queue[i + 1];
        i++;
    }
    return first;
}

int check_marker(char *queue) {
    for(int i = 0; i < 3; i++) {
        for(int j = i + 1; j < 4; j++) {
            if(queue[i] == queue[j]) {
                return 0;
            }
        }
    }
    return 1;
}

void handle_line(const char *line) {
    if(found) return;
    for (int i = 0; line[i] != '\0'; i++) {
        enqueue(queue, line[i]);
        if(count >= 4) {
            dequeue(queue);
            if(check_marker(queue)) {
                found = 1;
                return;
            }
        }
        count++;   
    }
}




int main(int argc, char *argv[])
{
    const char *fileName = "input_files/adventofcode.com_2022_day_6_input.txt"; // Name of the file to read

    // Call the function from the file_reader.c file
    read_file_lines(fileName, handle_line);

    printf("%d", count + 1);
    return 0;
}
