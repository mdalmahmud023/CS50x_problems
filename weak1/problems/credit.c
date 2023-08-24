#include <cs50.h>
#include <stdio.h>

void card_type(long card);
int validity(long card);

int main(void)

{
    long card;
    do
    {
        card = get_long("Number: ");
    }
    while (card < 0);

    int s = validity(card);

    if (s % 10 == 0)
    {
        card_type(card);
    }
    else
    {
        printf("INVALID\n");
    }
}

int validity(long card)
{
    int sum = 0;
    for (int i = 1; card != 0; card /= 10, i++)
    {
        if (i % 2 == 0)
        {
            int d = 2 * (card % 10);
            sum += (d / 10 + d % 10);
        }
        else
        {
            sum += card % 10;
        }
    }
    return sum;
}

void card_type(long card)
{
    if ((card >= 34e13 && card < 35e13) || (card >= 37e13 && card < 38e13))
    {
        printf("AMEX\n");
    }

    else if (card >= 51e14 && card < 56e14)
    {
        printf("MASTERCARD\n");
    }

    else if ((card >= 4e12 && card < 5e12) || (card >= 4e15 && card < 5e15))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}