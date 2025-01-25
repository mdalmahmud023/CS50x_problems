#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    float L = ((count_letters(text) * 100.00 / count_words(text)));
    float S = ((count_sentences(text) * 100.00 / count_words(text)));

    float index = 0.0588 * L - 0.296 * S - 15.8;

    int grade = round(index);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

    // Print the grade level
}

int count_letters(string text)
{
    int l = 0;
    // Return the number of words in text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] >= 65 && text[i] <= 122)
        {
            l += 1;
        }
    }
    return l;
}

int count_words(string text)
{
    int space = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 32)
        {
            space += 1;
        }
    }
    return space + 1;
}

int count_sentences(string text)
{
    int sentence = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentence += 1;
        }
    }
    return sentence;
}
