from cs50 import get_float
while True:
    change = get_float("Change: ")
    if change > 0:
        break

cents = int(change * 100)

quarters = 0
while cents >= 25:
    cents -= 25
    quarters += 1

dimes = 0
while cents >= 10:
    cents -= 10
    dimes += 1

nickel = 0
while cents >= 5:
    cents -= 5
    nickel += 1

pennies = 0
while cents >= 1:
    cents -= 1
    pennies += 1


c = quarters + dimes + nickel + pennies

print(c)
