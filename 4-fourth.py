result = int(0)

for i in range(1, 1000000, 1):
    numeralFirst = int(i % 10)
    numeralSecond = int((i / 10) % 10)
    numeralThird = int((i / 100) % 10)
    numeralFourth = int((i / 1000) % 10)
    numeralFifth = int((i / 10000) % 10)
    numeralSixth = int((i / 100000) % 10)

    leftHalf = numeralSixth + numeralFifth + numeralFourth
    rightHalf = numeralThird + numeralSecond + numeralFirst

    if rightHalf == leftHalf:
        result += 1

print(result)
