import random


class RandomList:
    randomList = random.sample(range(-1000, 1000), 1000)

    def length_check(self):
        if len(RandomList.randomList) != 1000:
            return False
        else:
            return True

    randomList.sort(reverse=True)
    final = randomList[0:2]
    length = len(final)


print('The original list:', RandomList.randomList)
print(RandomList().final)
