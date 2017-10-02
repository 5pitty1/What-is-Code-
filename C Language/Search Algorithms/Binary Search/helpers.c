/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <stdio.h>

#include "helpers.h"

/**
 * Does a binary search
**/

int found;

void binary_search(int value, int values[], int start, int end) {
    if(start > end) {
        found = 0;
        return;
    }
    
    int middle = (start + end) / 2;
    
    if(value == values[middle]) {
        found = 1;
        printf("\n%d is at position %d!!!", value, middle);
    } 
    else if(value > values[middle])
        binary_search(value, values, middle+1, end);
    else
        binary_search(value, values, start, middle-1);
}


/**
 * Returns true if value is in array of n values, else false.
 */
int search(int value, int values[], int n)
{
/*    for(int i = 0; i < n; i++) {
        if(values[i] == value)
            return true;
    }
    return false;
*/
    binary_search(value, values, 0, n);
    
    return found;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    for(int i = 0; i < n; i++) {
        printf("%d, ", values[i]);
    }
    printf("\n");
    int smallest;
    int temp;
    for(int i = 0; i < n; i++) {
        smallest = i;
        for(int j = i; j < n; j++) {
            if(values[j] < values[smallest])
                smallest = j;
        }
        temp = values[i];
        values[i] = values[smallest];
        values[smallest] = temp;
    }
    for(int i = 0; i < n; i++) {
        printf("%d, ", values[i]);
    }
    return;
}
