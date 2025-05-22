
# File management System.

import os 

def File_create(filename):
    try:
        with open(filename,"x") as f:
            print(f"{filename} is successfully created!")

    except FileNotFoundError:
        print("Your file was not found!")     

    except Exception as e:
        print(f"An error occurred: {e}")

def File_edit(filenmae):
    try:
        with open(filenmae,"a") as f:
            content = input("Enter = ")
            f.write(content + "\n")
            print(f"{filenmae} successfully edit!")
    
    except FileNotFoundError:
        print("Your file was not found!")

    except Exception as e:
        print(f"An error occurred: {e}")

def File_read(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
            print(f"{content}") 
            print(f"{filename} is successfully read!")
    
    except FileNotFoundError:
        print("Your file was not found!")

    except Exception as e:
        print(f"An error occurred: {e}")

def File_deleted(filename):
    try:
        os.remove(filename)
        print(f"Your file {filename} successfully deleted!")

    except FileNotFoundError:
        print("Your file was not found!")

    except Exception as e:
        print(f"An error occurred: {e}")      

def File_check(filename):
    try:
        files = os.listdir()
        if not files:
            print("Not file found! ")
        else:
            print("Files in directory!")                      
            for file in files:
                print(file)
        
    except FileNotFoundError:
        print("Your file was not found!")

    except Exception as e:
        print(f"An error occurred: {e}")

def Tables(filename):
    try:
        with open(filename, "a") as f:
            n = int(input("Enter number for which you want the table: "))
            for i in range(1, 11):
                f.write(f"{n} X {i} = {n*i}\n")  # Write to file
            f.write("Your table was successfully written to the file!\n")
            print("Your table was successfully written to the file!")

    except FileNotFoundError:
        print("Your file was not found!")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\n 1: File Create.")
        print("\n 2: File Edit.")                
        print("\n 3: File Read.")        
        print("\n 4: File Deleted.")        
        print("\n 5: File Check.")
        print("\n 6: Create Tables.")
        print("\n 7: Exit System.")

        Choice = int(input("Enter your choice : "))

        if Choice == 1:
            filename = input("Enter filename you want to be create : ")
            File_create(filename)

        elif Choice == 2:
            filename = input("Enter filename you want to be edit : ")
            File_edit(filename) 

        elif Choice == 3:
            filename = input("Enter filename you want to be read : ")
            File_read(filename)

        elif Choice == 4:
            filename = input("Enter filename you want to be deleted : ")
            File_deleted(filename)

        elif Choice == 5:
           
            File_check(filename)    

        elif Choice == 6:
            filename = input("Enter file name you want add table : ")
            Tables(filename)
        elif Choice == 7:
            print("Closing System.")
            break

        else:
            print("Invaild Choice(1 to 6)!")

if __name__ == "__main__":
    main()