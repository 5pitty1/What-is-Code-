#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
    This is a cool little program that asks for an input of their credit
    card number and outputs what type of credit card they have.
*/

/*
    This function checks if the card is a valid card by applying some fancy
    function onto the number.
*/
void checkSum(unsigned long long cardNum) {

    int currentDigit;
    int count = 0;
    int oddSum = 0;
    int evenSum = 0;

    while (cardNum > 0) {

        currentDigit = cardNum % 10;

        if (count % 2 == 1){
            int doubled = currentDigit * 2;
            oddSum += doubled / 10 + doubled % 10;
        }
        else {
            evenSum += currentDigit;
        }

        count++;
        cardNum = cardNum / 10;

    }

    int total = oddSum + evenSum;
    if (total % 10 != 0) {
        printf("INVALID\n");
        exit(0);
    }

}

/* This part then returns the type of bank this card is from. */
char* findBank(unsigned long long cardNum) {
    char* bank = "";
    do {
        if (cardNum == 34 || cardNum == 37) {
            bank = "AMEX";
            break;
        } else if (51 <= cardNum && cardNum <= 55) {
            bank = "MASTERCARD";
            break;
        } else if (cardNum == 4) {
            bank = "VISA";
            break;
        } else {
            bank = "INVALID";
        }
        cardNum = cardNum / 10;
    } while (cardNum > 0);

    if(strcmp(bank, "INVALID") == 0){
        printf("INVALID\n");
        exit(0);
    }

    return bank;
}

/* This function makes sure the card is of valid length. */
void validCardLength(unsigned long long cardNum, char* bank) {

    int size = 0;

    while (cardNum > 0) {
        size ++;
        cardNum = cardNum / 10;
    }
    if (strcmp(bank, "AMEX") == 0){
        if (size == 15)
            printf("%s\n", bank);
    } else if (strcmp(bank, "MASTERCARD") == 0) {
        if (size == 16)
            printf("%s\n", bank);
    } else if (strcmp(bank, "VISA") == 0) {
        if (size == 13 || size == 16)
            printf("%s\n", bank);
    } else {
        printf("INVALID\n");
        exit(0);
    }
}

int main(void) {

    printf("Number: ");
    unsigned long long cardNum;
    scanf("%lld\n", &cardNum);
    checkSum(cardNum);
    char* bank = findBank(cardNum);
    validCardLength(cardNum, bank);
}
