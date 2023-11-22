#Practical Task 1

""" 
Create a program that ask for a user input and storage this information;
Write if/elif/else statement to fulfil the following criteria:
-user is under 13, output the message "You qualify for the kiddie
discount."
-user is 21, output the message "Congrats on your 21st!"
-user is 40 or over, output the message "You're over the hill."
-user is 65 or older, output the message "Enjoy your retirement!"
-user over 100, output the message "Sorry, you're dead.".
-for any other age, output the message "Age is but a number."
"""

age=int(input("What is your age?"))

if age < 13:
    print("You qualify for the kiddie discount.")

elif age == 21:
    print("Congrats on your 21st!")

elif age > 39:
    print("You're over the hill.")

elif age > 64:
    print("Enjoy your retirement!")

elif age > 100:
    print("Sorry, you're dead.")

else:
    print("Age is but a number.")



