#Task01:
#Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message “The last number you entered was a [number]” and stop the program. 

num = 0
while num <= 5:
    num = int(input("Enter a number: "))

    if num > 5:
        print(f"The last num you entered was {num}.")

#Practice question
#Write a program that keeps asking the user to enter a password until they enter the correct one. The correct password is "Python123". If the user enters the correct password, print "Access granted!" and break out of the loop. If they enter the wrong password, print "Incorrect password, try again." and continue asking.

password = 0
while password != "Python123":
    password = input("Enter your password: ")

    if password == "Python123":
        print("Access granted!")
    else:
        print("Wrong password, Try again!")


#PracticeQuestion01:
#Putting limitations in above question
correct_Password = "Python123" 
max_Attempts = 3
attempts = 0

while attempts < max_Attempts:
    Password= input("Enter your Password: ")

    if Password == 'Python123':
        print("Access Granted!")
        break

    else:
        print('Wrong Password, Try again!')
        attempts += 1

    if attempts == max_Attempts:
        print("Too many attempts, Try Later!")

    