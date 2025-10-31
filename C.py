units = int(input())


if units <= 100:
    bill = units * 4
elif units <= 200:
    bill = 100 * 4 + (units - 100) * 5
elif units <= 300:
    bill = 100 * 4 + 100 * 5 + (units - 200) * 6
elif units <= 400:
    bill = 100 * 4 + 100 * 5 + 100 * 6 + (units - 300) * 7
else:
    bill = 100 * 4 + 100 * 5 + 100 * 6 + 100 * 7 + (units - 400) * 8

bill = bill + (bill * 0.10)

print(round(bill, 1))
