from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open (p, "w") as fs:
                data = input("Enter the data you want to write in your file: ")
                fs.write(data)

            print(f"FILE {name} CREATED SUCCESSFULLY")

        else:
            print("File already exists")

    except Exception as err:
        print(f"An error occured: {err}")

def readfile():
        try:
            readfileandfolder()
            name = input("Enter the name of the file you want to read: ")
            p = Path(name)
            if p.exists() and p.is_file():
                with open(p, "r") as fs:
                    data = fs.read()
                    print(f"File readed successfully: \n{data}")
            else:
                print("File does not exist")
        except Exception as err:
            print(f"An error occurred as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for updating file name")
            print("Press 2 for overwriting the data in file")
            print("Press 3 for appending data in file")
            res = int(input("Enter your choice: "))

        if res == 1:
            name2 = input("Enter the new name of the file: ")
            p2 = Path(name2)
            p.rename(p2)
            print(f"File renamed successfully to {name2}")

        if res == 2:
            with open(p, "w") as fs:
                data = input("Enter your data this will ovewrite the existing file: ")

                fs.write(data)
            print(f"File updated successfully with new data: {data}")

        if res == 3:
            with open(p, "a") as fs:
                data = input("Enter your data this will append your file: ")

                fs.write(" " + data)
                print(f"File appended successfully")
    except Exception as err:
        print(f"An error occurred as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print(f"File {name} deleted successfully")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error occurred as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()