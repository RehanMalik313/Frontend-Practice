#Task02:
#Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total.

num0 = int(input("Enter a number: "))
num1 = int(input("Enter a number: "))

total = num0 + num1

while True:
    ans = input('Do you want to add another number?(y/n): ')
    if  ans == 'y':
        ask = int(input("Enter another number: "))
        total = ask + total
    elif ans == 'n':
        break
    
print(f"The total is {total}")



#Practice Question:
#Write a program that asks the user to enter a series of expenses they’ve incurred throughout the day. The program should:

#Ask the user to enter an expense amount.
#Add that amount to a running total.
#Prompt the user if they have another expense to enter.
#If the user enters "y", ask for the next expense and add it to the total.
#If the user enters "n", stop the loop and display the total expenses for the day.
#If the user enters any other input, prompt them to enter "y" or "n".

exp_amount = int(input("Enter an expense amount: "))

add = exp_amount 

while True:
    expense = input("anyother expense to enter: (y/n)")

    if expense == 'y':
        next_expense=int(input("Enter next expense: "))
        add = exp_amount + next_expense 
    elif expense =='n':
        print(f"The total expenses for the day are {add}. ")
        break
    else:
        print("Enter y or n!")

