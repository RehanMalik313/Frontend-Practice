#Task00:
# Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.

num00 = int(input("Enter a number: "))
num01 = int(input("Enter a number: "))

if num00 > num01:
    print(num01, num00)
else:
    print(num00, num01)