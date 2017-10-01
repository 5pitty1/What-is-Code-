#include <stdio.h>

/*
    So turns out, scanf takes in a pointer as a parameter.
    &min - Address of min
*/
int main(void) {

    int mins;
    //Gets number of minutes
    do {
        printf("minutes: \n");
        scanf("%d\n", &mins);
    } while (mins <= 0);

    //converts minutes to bottles of water
    printf("bottles: %i\n", mins * 12);

}
