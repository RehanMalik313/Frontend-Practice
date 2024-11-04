#Task01.py:
#Add to program 069 to ask the user to enter a number and display the country in that position.

country_name = ['afghanistan', 'russia', 'china', 'america', 'india']
print(country_name)
print()
country = input('Enter one of the above country: ')
print(f'{country} has the number {country_name.index(country)} in the above list.')
num = int(input('Enter number between 0 and 5: '))
print(country_name[num])