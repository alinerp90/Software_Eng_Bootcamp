#Write a program that continually asks the user to enter a number
#should stop when the user write -1
#program must calculate the average of the numbers entered, excluding -1

number = int(input("Please write a number (Write -1 to stop!)"))
total = 0
count = 0
average = 0

while number != -1 :
    total = total + number
    count = count + 1 
    number = int(input("Please write a number (Write -1 to stop!)"))

    if number == -1 :
        average = total / count
        print ("Average: " , average)
        break




