# print a symmetrical shape out of @ symbols using a for loop, with a logical error

for i in range(1, 19):
    if i <= 10:
        print((10-i)*" " + (2*i*"@") + (10-i)*" " )
    if i > 10:
        print((i-10)*" " + (2*(19-i)*"@") + (i-10)*" " )


