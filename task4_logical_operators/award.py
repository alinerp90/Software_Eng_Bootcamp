#Practical task 1

'''
Determines the award a person competing in a triathlon will receive, based in the total time inserted individualy for the 3 categories:
-Swimming,
-Cycling,
-Running.
Then calculate total in minutes.
To qualify need to be less than 111min.

Qualifying Criteria
0 - 100 minutes = Provincial Colours
101 - 105 minutes = Provincial Half Colours
106 - 110 minutes = Provincial Scroll
111+ minutes = No award
'''

Name = input("Please insert your name: ")
print("Hello" , Name)
swimming_time = int(input("Please insert the time you finished the Swimming part in the Triathlon in minutes:"))
cycling_time = int(input("Now, please insert your time for cycling, in minutes:"))
running_time = int(input("Finally, please insert your time for the running in minutes:"))

total_time = swimming_time + cycling_time + running_time

if total_time <= 100 :
    print("Congratulations, you awarded Provincial colours. Your time was",total_time, "minutes.")

elif (total_time>100) and (total_time<=105) :
    print("You are awarded with Provincial Half Colours. Your time was", total_time,"minutes")

elif (total_time>105) and (total_time<=110) :
    print("You are awarded with Provincial Scroll. Your total time was", total_time,"minutes")

else: 
    print("Sorry, you didn't qualified. Your time was",total_time, "minutes.")
