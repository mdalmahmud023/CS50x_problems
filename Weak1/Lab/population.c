#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int year = 0 ;
    int i ;
    int s ;
    do
    {
        s = get_int("Start Size: ");
    }
    while (s < 9);

    int e;
    do
    {
        e = get_int("End Size: ");
    }
    while (e<=s);


    while (s < e)
    {
        i = s/3 - s/4 ;
        s = s + i ;

        year = year + 1;

    }
    printf("%i\n",year);

}