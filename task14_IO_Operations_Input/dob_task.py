with open('T14 - IO Operations - Input/DOB.txt', 'r+') as file:
    lines = file.readlines()

print('\033[1m' + 'Name' + '\033[0m')
# print('\033[0m')
for line in lines:
    names = line.split(" ")
    print(names[0] +" " +names[1])

print("")
print('\033[1m' + 'BirthDate' + '\033[0m')

for line in lines:
    dob = line.strip()
    dob = dob.split(" ")
    print(dob[2] + " " + dob[3] + " " + dob[4])
