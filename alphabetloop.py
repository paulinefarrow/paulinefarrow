vowel_count = 0
consonant_count = 0
my_alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in (my_alphabet):
    if i in ('a','e','i','o','u'):
        vowel_count = vowel_count + 1
    elif i not in ('a','e','i','o','u'):
        consonant_count = consonant_count + 1
print(f"Vowels = {vowel_count}")
print(f"Consonents = {consonant_count}")