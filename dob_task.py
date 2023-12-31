
# Open the file 

with open('dob.txt', 'r') as file:

    lines = file.readlines()               # read each line into an item in a list
    print("Name:")
    for i in lines:                        # loop through each line 
        j = i.split()                      # splitting words into items in sublist 
       
        print(j[0], j[1])                  # print the first two words under 'Name'
    


    print("\nBirthdate:")    
    for k in lines:
        l = k.split()
       
        print(l[2], l[3], l[4])            # print the next 3 words under 'Birthdate'

        