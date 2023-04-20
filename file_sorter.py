import os

path = input("please enter the starting directory: ")

file_list = os.walk(path)

for root, directory, file in file_list:
    print(file)