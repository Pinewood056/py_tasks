import random
# Generate 1000 random numbers between -1000 and 1000
random_list = random.sample(range(-1000, 1000), 1000)


def average():
    return sum(random_list)/len(random_list)


average08 = int(average()-200)
average12 = int(average()+200)

print(random_list)
print("Average is", average())
print("80% from average is", average08)
print("120% from average is", average12)

finalArray = []

for i in random_list:
    if average08 < i < average12:
        finalArray.append(i)

print(finalArray)
