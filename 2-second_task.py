import random
# Generate 1000 random numbers between -1000 and 1000
random_list = random.sample(range(-1000, 1000), 1000)


def average():
    return sum(random_list)/len(random_list)


average08 = average() * 0.8
average12 = average() * 1.2

print(random_list)
print("Average is", average())
print("80% from average is", average08)
print("120% from average is", average12)

finalArray = []

if average() > 0:
    for i in random_list:
        if average08 < i < average12:
            finalArray.append(i)
if average() < 0:
    for i in random_list:
        if average08 > i > average12:
            finalArray.append(i)
if average() == 0:
    print('You are winner. Average is Zero!')

print(finalArray)
