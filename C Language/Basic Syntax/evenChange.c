#include <stdio.h>
#include <math.h>

/*
    Example of how modulus works. There are two use cases for it
    as of now, one is to get the left over of splitting a number into
    groups. And the other is to check whether a number is divisible by
    another.
*/
int main(void) {

    float money;
    printf("It's good to see you old chap!\n");

    //asks for change
    do {
        printf("How much change does thou need?\n");
        scanf("%f", &money);
    } while (money < 0);

    //converts the change from dollars pennies
    int pennies = (int)roundf(money*100.0);
    int coins = 0;

    //counts number of quarters and removes them
    coins += pennies / 25;
    printf("%d Quarters\n", pennies / 25);
    pennies = pennies % 25;

    //counts number of dimes and removes them
    coins += pennies / 10;
    printf("%d Dimes\n", pennies / 10);
    pennies = pennies % 10;

    //counts number of nickels and removes them
    coins += pennies / 5;
    printf("%d Nickels\n", pennies / 5);
    pennies = pennies % 5;

    //adds the rest in pennies
    coins += pennies;
    printf("%d Pennies\n", pennies);

    printf("%i\n", coins);
    if (coins % 2 == 0) {
        printf("Praise oden!!! Thou hath an even number of coins!!\n");
    }

}
