import os
from sys import exit

def choice():
    print("Python text editor")
    choice_made = input("""
                    1. Create file
                    2. Delete file
                    >> """)
    return choice_made
def create_file():
    fname = input("Filename: ")
    print("Note: You can't press ENTER")
    print("Start Typing the contents now")
    contents = input(">> ")
    contents = contents.encode('utf-8')
    with open(fname, 'wb') as f:
        f.write(contents)
        f.close()
    print("File created successfully")

def delete_file(filename):
    osystem = input("What is the OS you are running Windows or Linux: ")
    if osystem == "Windows":
        os.system(f"del {filename}")
    elif osystem == "Linux":
        os.system(f"rm {filename}")
    else:
        print("Invalid Option")
        exit()

def main():
    chosen = choice()
    if chosen == "Create file":
        create_file()
    elif chosen == "Delete file":
        delete_file(input("Filename: "))
    else:
        print("Invalid choice")
        exit()

if __name__ == "__main__":
    main()


