from pathlib import Path
import os

def read_file_and_folder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def create_file():
   try:
        read_file_and_folder()
        name=input("please tell your file name :- ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as f:
                data=input("what you want to write in this file :- ")
                f.write(data)
            print("File created successfully")
        else:
            print("This file already exist")

   except Exception as e:
       print(f"An error occured as {e}")


def read_file():
    try:
        read_file_and_folder()
        name=input("Which file you want to read ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as f:
                data=f.read()
                print(data)

            print("Readed successfully")
        else:
            print("The file doesnot exist" )
    except Exception as e:
        print(f"An error occured as {e}")


def update_file():
    try:
        read_file_and_folder()
        name=input("Which file you want to update")
        p=Path(name)

        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file:-")
            print("press 2 for overwriting  the data of your file:-")
            print("press 3 for appending something to your file:-")

            res=int(input("Please tell your response:-"))

            if res==1:
                name2=input("Tell your new name :-")
                p2=Path(name2)
                p.rename(p2)
                print("Name changed successfully! ")

            if res==2:
                with open(p,'w') as f:
                    data=input("What you want to overwrite . ")
                    f.write(data)
                    print("Content overwrite successfully! ")

            if res==3:
                with open(p,'a') as f:
                    data=input("What you want to append. ")
                    f.write(" "+data)
                    print("Data appended successfully! ")

    except Exception as e:
        print(f"An error occured as {e}")   

def delete_file():
    try:
        read_file_and_folder()
        name=input("Enter name of the file you want to delete. ")
        p=Path(name)

        if p.exists() and p.is_file():
            os.remove(p)

            print("file removed successfully")

        else:
            print("No such file exist")
    except Exception as e:
        print(f"An error occured as {e}")

        




print("press 1 for creating a file ")

print("press 2 for reading a file ")

print("press 3 for updating a file ")

print("press 4 for deleting a file ")

check = int(input("please tell your response:- "))

if check==1:
    create_file()

if check==2:
    read_file()

if check==3:
    update_file()

if check==4:
    delete_file()