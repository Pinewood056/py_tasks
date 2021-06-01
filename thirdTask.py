import random
# Generate 1000 random numbers between -1000 and 1000
randomList = random.sample(range(-1000, 1000), 1000)
# print the list
print('The original list:', randomList)
# print the count of the items of the list
print('The length of the original list:', len(randomList))

# Sort with Reverse
randomList.sort(reverse=True)
print('The sorted list:', randomList)
# print the count of the items of the sorted list
print('The length of the sorted list:', len(randomList))
# List only 2 first value
print('The first 2 values from the sorted list:', randomList[:2])
