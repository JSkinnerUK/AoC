#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const int *a, const int *b)
{
    int int_a = *a;
    int int_b = *b;

    return (int_a > int_b) - (int_a < int_b);
}

int main()
{
    FILE *fptr;
    fptr = fopen("adventofcode.com_2022_day_1_input.txt", "r");
    char line[16];

    int currentCalories = 0;
    int calories[3] = {0, 0, 0};

    if (fptr != NULL)
    {
        while (fgets(line, sizeof(line), fptr))
        {
            if (line[0] == '\n')
            {
                qsort(calories, sizeof(calories) / sizeof(calories[0]), sizeof(calories[0]), comp);

                if (calories[0] < currentCalories)
                {
                    calories[0] = currentCalories;
                }

                currentCalories = 0;
            }
            else
            {
                line[strcspn(line, "\n")] = 0;
                int number = atoi(line);
                currentCalories += number;
            }
        }
    }
    else
    {
        printf("Not able to open the file.");
        return 1;
    }

    fclose(fptr);

    int total = 0;
    for (int i = 0; i < 3; i++)
    {
        total += calories[i];
    }
    printf("%d\n", total);

    return 0;
}
