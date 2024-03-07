#Practical task 1:

'''
PSEUDO CODE
Write a Python code:
1. Ask for the user's name input, storage information in a variable and print it out
2. Ask for the user's age input, storage information in a variable and print it out
3. Print the string "Hello World!" in a new line
'''

#Input from user the name and print it
user_name = input("What is your name? ")
print(user_name)

#Input from the user the age and print it, than print Hello World in sequence
user_age = input ("How old are you? ")
print(user_age)
print("Hello World")

# improvements:

def greeting():
    name = input("What is your name? ")
    age = input ("How old are you? ")
    print(f"{name}, {age}, Hello World!")

greeting()

"""  
Pick any one of your GitHub repos.
● Create 2 issues for things you think could be improved. Ideas for
improvements include making new methods, adding constants, renaming
variables and functions, or adding comments.
● For each issue:
○ Create a branch with a meaningful name.
○ Implement the changes required by the issue.
○ Commit and push your work.
○ Create a PR for your changes.
○ Merge in the PR and close the issue.
● In a text file called repo.txt, paste the link to your repo. Add the file to this task’s folder.
"""