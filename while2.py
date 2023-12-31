# declare variables to collect count and sum of numbers entered

sum = 0
count = 0

# ask user to enter numbers until they enter -1

number = int(input("Please enter a number: "))

while True:
    
    if number == -1:
        break

# add to the count and sum for each number entered

    count += 1
    sum += number
    
    number = int(input("Please enter a number: "))

# if user enters -1 as their first number don't calculate the average     

if count > 0:
    print(f"Average of numbers entered = {sum/count}")
else:
    print("You have entered -1.")   
      

