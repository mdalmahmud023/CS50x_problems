#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Enter Line Number: ");
    }

    while (n < 1 || n > 8);

    for (int i = 1; i <= n; i++)
    {

        for (int a = n - i; a > 0; a--)
        {
            printf(" ");
        }
        for (int j = 1; j <= i; j++)

        {

            printf("#");
        }

        printf("  ");

        for (int j = 1; j <= i; j++)

        {

            printf("#");
        }
        printf("\n");
    }
}
