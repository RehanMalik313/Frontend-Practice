# Task02:
# Ask the user to enter their name and display each letter in their name on a separate line.

name = input("Enter your name: ")
for i in name:
    print(i)

#Question:
#Ask the user to enter their name and display the total number of vowels in their name, listing each vowel on a separate line if there are any.

name = input("Enter your name: ")
vowels_dict = "a,e,i,o,u" 
vowels_count = 0

for char in name:
    if char in vowels_dict:
        print(char)
        vowels_count += 1

print("Total num of vowels: ", vowels_count)