""" 
num_list = [1, 2, 3, 4, 5]
found = False
num = int(input("Input a number from 1 to 10 and find out if it's in our list:"))

if num<1 or num>10:
    print("Number out of range")
else:
    for number in num_list:
        if num == number:
            found = True
            break
print(f'List contains {num}: {found}')
"""
for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} * {y} = {x*y}")
    print("")

