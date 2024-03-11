#ex 1
import os

print(os.getcwd())

print("All items:")
print(os.listdir('pp2_1\\'))

directories = []
files = []
for item in os.listdir('pp2_1\\'):
    full_path = os.path.join('pp2_1\\', item)
    if os.path.isdir(full_path):
        directories.append(item)
    if os.path.isfile(full_path):
        files.append(item)

print("\nDirectories:")
print(directories)
print("\nFiles:")
print(files)


#ex 2

import os

def check_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    if os.access(path, os.R_OK):
        print(f"You have read access to the path.")
    else:
        print(f"You do not have read access to the path.")
    if os.access(path, os.W_OK):
        print(f"You have write access to the path.")
    else:
        print(f"You do not have write access to the path.")

    if os.access(path, os.X_OK):
        print(f"You have execute access to the path.")
    else:
        print(f"You do not have execute access to the path.")

path = input("Enter the path: ")
check_access(path)


#ex 3

import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = input("Enter the path to test: ")
check_path(path)


#ex 4

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")

filename = '/Users/Арсен/OneDrive/Рабочий стол/Lessons/GitHub/pp2_1/lab6/justafile.txt'
num_lines = count_lines(filename)
print(f"Number of lines in {filename}: {num_lines}")


#ex 5

def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List successfully written to {filename}.")
    except Exception as e:
        print(f"Error occurred: {e}")

filename = 'justafile.txt' 
my_list = ['hello', 'world'] 
write_list_to_file(filename, my_list)


#ex 6

import string

def generate_text_files():
    try:
        for i in string.ascii_uppercase:
            filename = i+ ".txt"
            with open(filename, 'w') as file:
                file.write(f"This is file {filename}.")
        print("Text files created successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

generate_text_files()

#ex 7

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print(f"Contents of {source_file} copied to {destination_file} successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

source_file = 'justafile.txt'
destination_file = 'anotherfile.txt'
copy_file(source_file, destination_file)

#ex 8

import os

def delete_file(path):
    if not os.access(path, os.F_OK):
        print(f"File at {path} does not exist.")
    elif not os.access(path, os.W_OK):
        print(f"You don't have permission to delete the file at {path}.")
    else:
        try:
            os.remove(path)
            print(f"File at {path} deleted successfully.")
        except Exception as e:
            print(f"Error occurred while deleting file: {e}")

file_path = 'filetodelete.txt'
delete_file(file_path)
