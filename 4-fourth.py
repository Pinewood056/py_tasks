n = 0
# start position for nums
for num in range(1000000):
    strNum = str(num)
# move nums to a string
    strNum = '0'*(6-len(strNum)) + strNum
# make strNum 6-digits. If need more/less than 6 nums in ticket - change "int`s" bellow
    if int(strNum[0]) + int(strNum[1]) + int(strNum[2]) == int(strNum[3]) + int(strNum[4]) + int(strNum[5]):
        n = n+1

print(n)
