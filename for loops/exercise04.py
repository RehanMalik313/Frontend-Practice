#Task04:
# Ask the user to enter a number between 1 and 12 and then display the times table for that number. 

num = int(input("Enter a number between 1 and 12: "))

for i in range(1, 13):
    ans = i * num
    print(i, "X", num, "=", ans) 
