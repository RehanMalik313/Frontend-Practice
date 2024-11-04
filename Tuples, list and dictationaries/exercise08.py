#Task08:
#Change program 076 so that once the user has completed their list of names, display the full list and ask them to type in one of the names on the list. Display the position of that name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete that entry from the list and display the list again.

invitees_list = []
count = 3

for i in range(0, 3):
    invitee = input('Enter invitee`s name: ')
    invitees_list.append(invitee)

another_invitee = input('Do you eant to invite more invitees?(y/n): ')

while another_invitee == 'y':
    more_invtees = input('Enter name: ')
    invitees_list.append(more_invtees)
    count += 1
    another_invitee = input('Do you eant to invite more invitees?(y/n): ')

print(f'You have invited {count} and the names are {invitees_list}.')

name = input('Enter one of the names from the list: ')
print(f'{name} is at {invitees_list.index(name)}.')

ask = input(f'Do you want {name} in the party? (y/n): ')

if ask =='n':
    dislike = invitees_list.index(name)
    del invitees_list[dislike]
    print(f'only invite {invitees_list} in the party.')
else:
    print('I want them all')