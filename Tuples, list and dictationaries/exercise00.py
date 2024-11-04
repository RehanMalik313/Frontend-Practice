#Task00:
#Create a tuple containing the names of five countries and display the whole tuple. Ask the user to enter one of the countries that have been shown to them and then display the index number (i.e. position in the list) of that item in the tuple.

country_name = ['afghanistan', 'India', 'America', 'Russia', 'China']
print(country_name)
print()
country = input('Enter one of the country: ')
print(f'{country} has the index number', country_name.index(country))