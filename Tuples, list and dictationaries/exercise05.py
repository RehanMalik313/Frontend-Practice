#Task05:
#Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colours between the start and end numbers the user input.

color_list = ['red', 'blue', 'green', 'yellow', 'orange', 'brown', 'silver', 'black', 'pink', 'white' ]
start_num = int(input('Enter a starting number between 0 and 4: '))
end_num = int(input('Enter an end number between 5 and 9: '))

print(color_list[start_num:end_num])