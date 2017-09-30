#include <stdio.h>

/*
    So turns out, scanf takes in a pointer as a parameter.
    &min - Address of min
*/
int main(void) {

    //Gets number of minutes
    printf("minutes: \n");
    int mins;
    scanf("%d\n", &mins);

    //converts minutes to bottles of water
    printf("bottles: %i\n", mins * 12);

}
