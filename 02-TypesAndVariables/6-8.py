first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
# distance between the codes minus 1 (we do not count the last letter);
# max(..., 0) makes K and K give 0 instead of -1
number_of_letters = max(abs(last_letter_code - first_letter_code) - 1, 0)
print(f'Between {first} and {last} is {number_of_letters} letters')
