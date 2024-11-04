#Task06:
#Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line. Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of that number in the list, otherwise display the message “That is not in the list”.

digit_list = [674, 553, 452, 756]

for i in digit_list:
    print(i)

num = int(input('Enter a three-digit number: '))
if num in digit_list:
    print(f'{num} is at {digit_list.index(num)}')
else:
    print('That is not in the list.')