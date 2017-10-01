#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/*
    This guy just prints out the first letter of every word
    given as input. Note that this also capitalizes the letter
    and also grabs the first letter too.
*/
int main(void) {

    char name[80];
    fgets(name, 80, stdin);

    //prints the very first letter as an uppercase
    if(isalpha(name[0]))
        printf("%c", toupper(name[0]));

    //finds every letter that comes after a space and prints them
    for(int i = 1; i < strlen(name); i++) {
        if(name[i] == ' ' && isalpha(name[i+1])){
            printf("%c", toupper(name[i+1]));
        }
    }
    printf("\n");
}
