#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/*
    This was a cooler implementation of the caesar cipher, called the
    vigenere cipher. Instead of just taking an integer as the encryption
    key, it takes an entire word and uses the ascii value of each letter
    as an encryption key.
*/
int main(int argc, char* argv[]) {

    //checks whether there is more or less than 1 argument
    if(argc != 2) {
        printf("Give me only 1 key");
        return 1;
    }

    char* keyword = argv[1];
    int keylen = strlen(keyword);
    int j = 0;

    //checks if only letters are in keyword
    for(int i = 0; i < keylen; i++) {
        if(!isalpha(keyword[i])) {
            printf("Only letters in ur keyword!!\n");
            return 1;
        }
    }

    char unciphered[80];
    fgets(unciphered, 80, stdin);


    //goes through each letter in the unciphered text
    for(int i = 0, n = strlen(unciphered); i < n; i++) {
        char cipher = unciphered[i];

        //checks if the letter is alphabetical else it just prints the character
        if(isalpha(cipher)) {

            //turns the letter into a key
            int key = toupper(keyword[j % keylen])-'A';
            j++;

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
