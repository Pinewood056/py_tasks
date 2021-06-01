import random
# Generate 1000 random numbers between -1000 and 1000
randomList = random.sample(range(-1000, 1000), 1000)
# print the list
print('The original list:', randomList)


def length_check():
    if len(randomList) != 1000:
        return 'The list isn`t equal 1000. FAIL.'
    else:
        return "The list is equal 1000. OK."


print(length_check())
# Sort with Reverse
randomList.sort(reverse=True)
print('The sorted list:', randomList)
print(length_check())


def final_check():
    if len(randomList[:2]) != 2:
        return "There is not 2 elements. FAIL."
    else:
        return "There is only 2 elements returned. OK."


print('The first values from the sorted list:', randomList[:2])
print(final_check())
