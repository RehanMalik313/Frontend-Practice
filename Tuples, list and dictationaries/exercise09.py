#Task09:
#Create a list containing the titles of four TV programmes and display them on separate lines. Ask the user to enter another show and a position they want it inserted into the list. Display the list again, showing all five TV programmes in their new positions.

program_list = ['ben10', 'courage', 'john', 'puffgirls']

for i in program_list:
    print(i)

another_show = input('Enter another show you want to insert: ')
show_postion = int(input('Enter the postion of show: '))

program_list.insert(show_postion, another_show)

print(program_list)