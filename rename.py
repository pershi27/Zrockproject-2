import os

def rename_file(old_name, new_name):
    os.rename("/Users/c.pershi/Desktop/Untitled.pages", new_name)
    print(f"File '{old_name}' renamed to '{new_name}' successfully.")

old_file_name = "old_file.txt"
new_file_name = "newfile.txt"
rename_file(old_file_name, new_file_name)
