import random
random_list = random.sample(range(-1000, 1000), 1000)


class Average:
    def average(self):
        return sum(random_list)/len(random_list)

    def average08(self):
        return Average.average(self) * 0.8

    def average12(self):
        return Average.average(self) * 1.2


class Final:
    finalArray = []

    if Average().average() > 0:
        for i in random_list:
            if Average().average08() < i < Average().average12():
                finalArray.append(i)
    if Average().average() < 0:
        for i in random_list:
            if Average().average08() > i > Average().average12():
                finalArray.append(i)
    if Average().average() == 0:
        print('You are winner. Average is Zero!')


print(random_list)
print("Average is", Average().average())
print("80% from average is", Average().average08())
print("120% from average is", Average().average12())
print(Final().finalArray)
