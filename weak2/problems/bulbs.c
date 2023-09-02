#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    int binary[BITS_IN_BYTE];
    int ascii;
    string messege = get_string("Message: ");
    for (int i = 0, n = strlen(messege); i < n; i++)
    {
        ascii = messege[i];

        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            binary[j] = ascii % 2;
            ascii /= 2;
        }
        for (int k = 0; k < BITS_IN_BYTE; k++)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}