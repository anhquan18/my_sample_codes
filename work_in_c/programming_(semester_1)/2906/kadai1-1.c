#include <stdio.h>

int main (void) {
    char str [] = "Hello, World";
    int i=0;
    char *p =str;
 
    while (*p != '\0') 
    {
        //while (str[i] != '\0') { 
        printf ("%c\n", *(p+i));
        //wait(2);
        //p++;
        i++;
    }
 
    return 0;

