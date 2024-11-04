#Task07:
#Ask the user to enter the names of three people they want to invite to a party and store them in a list. After they have entered all three names, ask them if they want to add another. If they do, allow them to add more names until they answer “no”. When they answer “no”, display how many people they have invited to the party.

invitees_list = []
count = 3
for i in range(3):
    invitees = input('Enter name of a invitee: ')
    invitees_list.append(invitees)

another_invitee = input('Do you want to invite another invitee? (y/n): ')

while another_invitee == 'y':
    add_invitee = input('Add another invitee: ')
    invitees_list.append(add_invitee)
    count += 1
    another_invitee = input('Do you want more invitees? (y/n):')
    
print(f'you have invited {count} people in the party and names are {invitees_list}.')
