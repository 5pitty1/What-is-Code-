/**
 * find.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Prompts user for as many as MAX values until EOF is reached,
 * then proceeds to search that "haystack" of values for given needle.
 *
 * Usage: ./find needle [size]
 *
 * where needle is the value to find in a haystack of values
 */

#include <stdio.h>
#include <stdlib.h>

#include "helpers.h"

// maximum amount of hay
int MAX = 65536;

int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc < 2 || argc > 3)
    {
        printf("Usage: ./find needle [size]\n");
        return -1;
    }

    // remember needle
    int needle = atoi(argv[1]);

    // fill haystack
    int size;

    if (argc == 3) {
        MAX = atoi(argv[2]);
    }
    int haystack[MAX];
    for (size = 0; size < MAX; size++)
    {
        // wait for hay until EOF
 //       printf("\nhaystack[%i] = ", size);
        int straw;
        scanf("%d", &straw);
        if (straw == MAX)
        {
            break;
        }

        // add hay to stack
        haystack[size] = straw;
    }
    printf("\n");

    // sort the haystack
    sort(haystack, size);

    // try to find needle in haystack
    if (search(needle, haystack, size))
    {
        printf("\nFound needle in haystack!\n\n");
        return 0;
    }
    else
    {
        printf("\nDidn't find needle in haystack.\n\n");
        return 1;
    }
}
