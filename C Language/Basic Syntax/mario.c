#include <stdio.h>

/*
    Practice working with loops and print statements.
*/
int main(void) {
    int height = 0; 

    //asks user for height until positive num given
    do {
        printf("height: ");
        scanf("%d", &height);
    } while (height < 0 || height > 23);

    for(int i = height-1; i >= 0; i--) {

        //prints spaces eqaual to height-1
        for(int j = i; j > 0; j--)
            printf(" ");

        //prints spaces eqaual to height-1-(current line num)
        for(int j = 0; j < height-1-i; j++)
            printf("#");

        //adds final 2 blocks and starts new line
        printf("##\n");

    }

}
