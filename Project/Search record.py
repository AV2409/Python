import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="project")
cursor=con.cursor()

def search_id():

    id=int(input("Enter the criminal ID you want to search for: "))
    query="select * from record where Criminal_ID={}".format(id)
    cursor.execute(query)
    x=cursor.fetchall()
    print(x)

def search_name():

    name=input("Enter the Name of Criminal you want to search for: ")
    query="select * from record where Name='{}'".format(name)
    cursor.execute(query)
    x=cursor.fetchall()
    print(x)

def search():
    print("-------------------------------------------------------------------------------------------")
    while True:
        print("Press 1 to search by Name")
        print("Press 2 to Search By ID")
        print("Press 3 to go to main menu")
        print()
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            print("-------------------------------------------------------------------------------------------")
            search_name()
            while True:
                print("-------------------------------------------------------------------------------------------")
                print("Press Y to continue")
                print("Press N to go back to Previous menu")
                print()
                choice2 =input("Press the key: ").upper()
                print()
                if choice2 == 'Y':
                    search_name()
                if choice2 == 'N':
                    print("Exit successful")
                    print("-------------------------------------------------------------------------------------------")
                    search()
        if choice1 == 2:
            print("-------------------------------------------------------------------------------------------")
            search_id()
            while True:
                print("-------------------------------------------------------------------------------------------")
                print("Press Y to continue")
                print("Press N to go back to Previous menu")
                print()
                choice2 =input("Press the key: ").upper()
                print()
                if choice2 == 'Y':
                    search_id()
                if choice2 == 'N':
                    print("Exit successful")
                    print("-------------------------------------------------------------------------------------------")
                    search()

        if choice1==3:
            exit()

        else:
            print("Press the Correct Key")
            search()

search()