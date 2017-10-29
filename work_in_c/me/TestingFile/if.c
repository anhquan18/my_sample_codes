/*
 File Name: if.c
 Author: Nguyen Anh Quan
 Date: 18/09/2017
*/

#include<stdio.h>
#include<string.h>

int main()
{ char name[20];
  int a;

 /* printf("input a: ");
  scanf("%d",&a);
  if (a) printf("a is True\n");
  else printf("a is False\n");*/
  printf("Input the name: ");
  scanf("%s", name);
  if (strcmp(name, "Quan") == 0)
  printf("Hello Quan\n");
  else
  printf("It is False\n");

  return 0;
}
