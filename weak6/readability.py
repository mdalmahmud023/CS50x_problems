from cs50 import get_string

text = get_string("Text: ")


def count_letter(text):
    count = 0
    for i in text:
        if i.isalpha():
            count += 1
    return count


def count_word(text):
    return len(text.split())


def sentences_count(text):
    s_count = 0
    for i in text:
        if i in [".", "?", "!"]:
            s_count += 1
    return s_count


L = (count_letter(text) / count_word(text)) * 100
S = (sentences_count(text) / count_word(text)) * 100

index = 0.0588 * L - 0.296 * S - 15.8
x = round(index)
if x < 1:
    print("Before Grade 1")
elif x >= 16:
    print("Grade 16+")
else:
    print(f"Grade {x}")
