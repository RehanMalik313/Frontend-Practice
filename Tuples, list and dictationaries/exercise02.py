#Task02:
#Create a list of two sports. Ask the user what their favourite sport is and add this to the end of the list. Sort the list and display it. 

list = ['cricket', 'football']
fav_sport = input('What is your favourite sport: ')
num = int(input('Enter index between 0 and 2: '))
list.insert(num, fav_sport)
print(sorted(list))
