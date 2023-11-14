# Option 1:

num_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]

for number in num_list:
    print("*" * number)

# Option 2:  

for i in range(1,10):
    if i <= 5:
        print("*" * i)
    else:
        print("*" * (10 - i))

# Option 3:

for i in range(1,6):
    print("*" * i)
for i in range(6,-1,-1):
    print("*" * i)










