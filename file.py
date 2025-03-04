#1
import os
def print_dirs(path):
    print(os.listdir(path))


#2
def exists_path(path):
    if os.path.exists(path):
        print(os.access(path, os.R_OK))
        print(os.access(path, os.W_OK))
        print(os.access(path, os.X_OK))

exists_path("111.txt")
#3
def find_file(path):
    if os.path.exists(path):
        print("Path exists")
        print("Dir and file names", os.listdir(path))
    else:
        print("Path does not exists")
find_file("lab1")
#4
file = open('111.txt')
a = 0
for i in file:
    a+=1
print(a)
#5
arr = ['fknv', 'kmvfmvf']
file = open('111.txt','w')
for i in arr:
    file.write(i+'\n')
#6
def generate_files():
    for char in range(65,91):
        filename = f"{chr(char)}.txt"
        with open(filename, "w") as file:
            file.write(f"{filename}")
generate_files()
#7
file = open("111.txt")
file_2 = open("A.txt",'w')
for i in file:
    file_2.write(i)
#8
def file_delete(file_path):
    if os.path.exists(file_path) and os.access(file_path,os.W_OK):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print(f"Cannot delete: {file_path}")
if __name__ == "__main__":
    file_delete(input("File: "))


