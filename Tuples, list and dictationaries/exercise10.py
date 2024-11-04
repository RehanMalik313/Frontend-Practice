#Task10:
#Create an empty list called “nums”. Ask the user to enter numbers. After each number is entered, add it to the end of the nums list and display the list. Once they have entered three numbers, ask them if they still want the last number they entered saved. If they say “no”, remove the last item from the list. Display the list of numbers. 

nums = []
count = 0
while count < 3:
    numbers = int(input('Enter numbers: '))
    nums.append(numbers)
    print(nums)
    count = count + 1

last_num = input('Do you want the last number saved (y/n): ')
if last_num == 'n':
    nums.remove(numbers)
print(nums)




