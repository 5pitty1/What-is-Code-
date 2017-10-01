#include <stdio.h>

/*
 Practice working with loops and print statements.
 */
int main(void) {
    int height = 0;
    
    //asks user for height until positive num given
    do {
        printf("Height: ");
        scanf("%d\n", &height);
    } while (height < 0 || height > 23);
    
    for(int i = height-1; i >= 0; i--) {
        
        //prints spaces eqaual to height-1
        for(int j = i; j > 0; j--)
            printf(" ");
        
        //prints hashes eqaual to height-1-(current line num)
        for(int j = 0; j < height-i; j++)
            printf("#");
        
        printf("  ");
        
        //prints the other side of the climb
        for(int j = 0; j < height-i; j++)
            printf("#");
        
        printf("\n");
    }
    
}

