# declare variables to hold original string and changed strings

my_string = "This is a string that I am going to change"
my_string_letters = ""
my_string_words = []

               ############### part 1 ######################
# loop through string making every even position letter upper case and every odd position letter lower case. 
# Add the letters to a new string my_string_letters and print it

for i in range(len(my_string)):
    if i%2 == 0:
        my_string_letters += my_string[i].upper()
    else:
        my_string_letters += my_string[i].lower()
      
print(f"String with alternating upper and lower case letters:\n\t{my_string_letters}")


               ############### part 2 ######################

# Convert string into a list

string_as_list = my_string.split()

# loop through list making every even position word upper case and every odd position word lower case. 
# Append the words to a new string my_string_words and print it

for i in range(len(string_as_list)):
    if i%2 == 0:

        my_string_words.append(string_as_list[i].upper()) 
    else: 

        my_string_words.append(string_as_list[i].lower()) 

print(f"String with alternating upper and lower case words:\n\t{' '.join(my_string_words)}")



    