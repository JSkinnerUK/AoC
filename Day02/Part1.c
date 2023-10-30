#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int determineWinner(char opp, char player) {
  switch (opp) {
  case 'A':
    if (player == 'X') {
      return 0;
    } else if (player == 'Y') {
      return 1;
    } else if (player == 'Z') {
      return -1;
    }
  case 'B':

    if (player == 'X') {
      return -1;
    } else if (player == 'Y') {
      return 0;
    } else if (player == 'Z') {
      return 1;
    }
  case 'C':
    if (player == 'X') {
      return 1;
    } else if (player == 'Y') {
      return -1;
    } else if (player == 'Z') {
      return 0;
    }
  default:
    return -2;
  }
}

int main() {
  FILE *fptr;
  fptr = fopen("adventofcode.com_2022_day_2_input.txt", "r");
  int score = 0;

  if (fptr != NULL) {
    char opp, player;
    while (fscanf(fptr, "%c %c\n", &opp, &player) != EOF) {
      int winner = determineWinner(opp, player);
      if (winner == 2)
        return 1;
      if (winner == 0) {
        score += 3;
      } else if (winner == 1) {
        score += 6;
      }

      if (player == 'X') {
        score += 1;
      } else if (player == 'Y') {
        score += 2;
      } else if (player == 'Z') {
        score += 3;
      }
    }
    printf("Total: %d\n", score);
  } else {
    printf("Not able to open the file.");
    return 1;
  }

  fclose(fptr);
}
