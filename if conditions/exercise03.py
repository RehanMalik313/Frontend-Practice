#Task03:
#Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”. 

color = input("Enter your favourite color: ")

if color == "red" or color =="RED" or color =="Red":
    print("I like Red too")
else:
    print(f"I don't like {color}")