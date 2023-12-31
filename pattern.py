# print the same number of asterisks as the value of i while i is 5 or less and then subtract i from 10 to get the second half of the pattern

for i in range(1, 10):
    if i <= 5:
        print(i * "*")
    else:
        print((10-i) * "*")