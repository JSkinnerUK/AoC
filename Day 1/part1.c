#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *fptr;
    fptr = fopen("adventofcode.com_2022_day_1_input.txt", "r");
    char line[16];

    int maxCalories = 0;
    int currentCalories = 0;

    if (fptr != NULL)
    {
        while (fgets(line, sizeof(line), fptr))
        {
            if (line[0] == '\n')
            {
                if (maxCalories < currentCalories)
                {
                    maxCalories = currentCalories;
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
    printf("Max Calories: %d\n", maxCalories);
    return 0;
}
