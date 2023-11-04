#include <stdio.h>
#include <string.h>

typedef enum
{
    Rock,
    Paper,
    Scissors,
} MoveEnum;

enum Outcome
{
    Lose = 'X',
    Draw = 'Y',
    Win = 'Z',
};

typedef struct
{
    char inputChar;
    MoveEnum choice;
    int value;
    MoveEnum beats;
    MoveEnum loses;
} Move;

Move getMoveByChar(char inputChar, Move moves[])
{
    for (int i = 0; i < 3; i++)
    {
        if (moves[i].inputChar == inputChar)
        {
            return moves[i];
        }
    }
};

Move getMoveByEnum(int moveEnum, Move moves[])
{
    for (int i = 0; i < 3; i++)
    {
        if (moves[i].choice == moveEnum)
        {
            return moves[i];
        }
    }
};

int main()
{
    FILE *fptr;
    fptr = fopen("adventofcode.com_2022_day_2_input.txt", "r");
    int score = 0;

    Move moves[] = {
        {'A', Rock, 1, Scissors, Paper},
        {'B', Paper, 2, Rock, Scissors},
        {'C', Scissors, 3, Paper, Rock},
    };

    if (fptr != NULL)
    {
        char move, outcome;
        while (fscanf(fptr, "%c %c\n", &move, &outcome) != EOF)
        {
            Move m = getMoveByChar(move, moves);

            if (outcome == Win)
            {
                score += 6;
                score += getMoveByEnum(m.loses, moves).value;
            }
            else if (outcome == Draw)
            {
                score += 3;
                score += m.value;
            }
            else
            {
                score += getMoveByEnum(m.beats, moves).value;
            }
        }
        printf("Total: %d\n", score);
    }
    else
    {
        printf("Not able to open the file.");
        return 1;
    }

    fclose(fptr);
    return 0;
}
