#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/*
    A basic caesar cipher algorithm that takes in a command line
    argument with a given
*/
int main(int argc, char* argv[]) {

    //checks whether there is more or less than 1 argument
    if(argc != 2) {
        printf("Give me only 1 key");
        return 1;
    }

    int key = atoi(argv[1]);

    char unciphered[80];
    printf("What do you want to convert? (Max 80 characters)\n");
    fgets(unciphered, 80, stdin);

    //goes through each letter in the unciphered text
    for(int i = 0, n = strlen(unciphered); i < n; i++) {
        char cipher = unciphered[i];

        //checks if the letter is alphabetical else it just prints the character
        if(isalpha(cipher)) {

            //ciphers an uppercase or lowercase version of the letter
            if(isupper(cipher))
                printf("%c", (cipher - 'A' + key) % 26 + 'A');
            else
                printf("%c", (cipher - 'a' + key) % 26 + 'a');

        } else {
            printf("%c", cipher);
        }
    }
}
