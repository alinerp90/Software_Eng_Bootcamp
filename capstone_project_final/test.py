import shutil

# Specify the path of the file you want to copy
file_to_copy = 'T17 - Capstone Project - Lists, Functions, and String Handling/capstone_project_final/tasks.txt'

# Specify the path of the destination directory you want to copy the file into
destination_directory = 'T17 - Capstone Project - Lists, Functions, and String Handling/capstone_project_final/task_overview.txt'

# Use the shutil.copy2() method to copy the file to the destination directory
shutil.copy2(file_to_copy, destination_directory)

print(destination_directory)