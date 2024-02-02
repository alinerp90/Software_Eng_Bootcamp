""" Instructions:
Write a program that allows a user to register students for an exam venue.
1. First, ask the user how many students are registering.
2. Create a for loop that runs for that number of students.
3. Each time the loop runs the program should ask the user to enter the
next student ID number.
4. Write each of the ID numbers to a text file called reg_form.txt
5. Include a dotted line after each student ID because this document will be
used as an attendance register, which the students will sign when they
arrive at the exam venue."""



number = int(input("How many students are registering?"))

with open('reg_form.txt', 'w') as f:
    while number > 0:
        number -= 1
        name = input("Enter ID number: ")
        f.write(name+"   ........................................ \n")
f.close()



