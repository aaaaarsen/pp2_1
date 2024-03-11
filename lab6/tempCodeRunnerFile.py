#ex 1
import os

print(os.getcwd())

print("All items:")
print(os.listdir('pp2_1\lab6\\'))

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
