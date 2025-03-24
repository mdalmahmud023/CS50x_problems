while True:
    c = int(input("Number: "))
    if c > 0:
        break


def validity(c):
    sum = 0
    n = 1
    while c > 0:
        if n % 2 == 0:
            x = (c % 10) * 2
            sum += x % 10 + x // 10
        else:
            sum += c % 10
        c //= 10
        n += 1
    return sum


def card_type(number):
    if (number >= 34e13 and number < 35e13) or (number >= 37e13 and number < 38e13):
        print("AMEX")
    elif number >= 51e14 and number < 56e14:
        print("MASTERCARD")
    elif (number >= 4e12 and number < 5e12) or (number >= 4e15 and number < 5e15):
        print("VISA")
    else:
        print("INVALID")


if validity(c) % 10 == 0:
    card_type(c)
else:
    print("INVALID")
