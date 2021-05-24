import random
# Generate 1000 random numbers between -1000 and 1000
randomList = random.sample(range(-1000, 1000), 1000)
# Sort with Reverse
randomList.sort(reverse=True)
# List only 2 first value
print(randomList[:2])
