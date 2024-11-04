#Task04:
#Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting from 1. Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary. 

food_dict = {}
for i in range(0, 4):
    fav_food = input('Enter fav food: ')
    food_dict[i + 1] = fav_food
    
print(food_dict)
print()
getrid = int(input('which one you don`t like: '))
del food_dict[getrid]
print(sorted(food_dict.values()))