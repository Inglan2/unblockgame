import os

# Get the current folder path
current_folder_path = os.getcwd()

# Iterate over all subdirectories and print the path of each file
for root, dirs, files in os.walk(current_folder_path):
    for file in files:
        print(os.path.join(root, file))
