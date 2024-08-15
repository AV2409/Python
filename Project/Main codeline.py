import PySimpleGUI as pg
import mysql.connector as c
import matplotlib.pyplot as plt
con=c.connect(host="localhost",user="root",password="",database="cia")
cursor=con.cursor()

#layout of window creation
layout = [[pg.Text("CIA")]
           ,[pg.Button('login')]#buttons
           ,[pg.Button('exit')]#buttons
         ]
#creating window 
window = pg.Window("CIA",layout)  

def options():
    print()
    print("Press 1 to Search for Criminal Records ")
    print("Press 2 to Add a Criminal Record ")
    print("Press 3 to Delete a Criminal Record ")
    print("Press 4 to View Most Wanted Criminal")
    print("Press 5 to View Graphs ")
    print("Press 6 to Exit ")
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print()
    opt_variable = int(input("Enter your choice: "))
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

    def add():

        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        criminal_id = int(input("Enter the Crimnal ID: "))
        name = input("Enter Name of Criminal: ")
        dob = input("Enter Date of Birth of criminal: ")
        country = input("Enter Country of criminal: ")
        wanted = input("Enter the Wanted Level: ")
        crime = input("Enter Crime done by criminal: ")
        status = input("Enter status of criminal: ")
        doa = input("Enter Date of Arrest: ")
        prison = input("Enter the name of prison ")
        query = "insert into criminal_records values({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(criminal_id,name,dob,country,wanted,crime,status,doa,prison)
        cursor.execute(query)
        con.commit()
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print("RECORD ADDED SUCCESSFULLY")
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        while True:
            print()
            print("Press Y to insert more records")
            print("Press N to Go to main menu")
            choice=input("Press the Key: ").upper()
            print()
            if choice=='Y':
                add()
            if choice=='N':
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                options()

    def search():

        def search_name():

            name=input("Enter the Name of Criminal you want to search for: ")
            query="select * from criminal_records where name='{}'".format(name)
            cursor.execute(query)
            x=cursor.fetchall()
            print(x)

        def search_id():

            crim_id=int(input("Enter the criminal ID you want to search for: "))
            query="select * from criminal_records where criminal_id={}".format(crim_id)
            cursor.execute(query)
            x=cursor.fetchall()
            print(x)

        
        
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        while True:
            print("Press 1 to search by Name")
            print("Press 2 to Search By ID")
            print("Press 3 to go to main menu")
            print()
            choice1 = int(input("Enter your choice: "))
            if choice1 == 1:
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                search_name()
                while True:
                    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                    print("Press Y to continue")
                    print("Press N to go back to Previous menu")
                    print()
                    choice2 =input("Press the key: ").upper()
                    print()
                    if choice2 == 'Y':
                        search_name()
                    if choice2 == 'N':
                        print("Exit successful")
                        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                        search()
            if choice1 == 2:
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                search_id()
                while True:
                    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                    print("Press Y to continue")
                    print("Press N to go back to Previous menu")
                    print()
                    choice2 =input("Press the key: ").upper()
                    print()
                    if choice2 == 'Y':
                        search_id()
                    if choice2 == 'N':
                        print("Exit successful")
                        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                        search()


            if choice1==3:
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                options()

            else:
                print("Press the Correct Key")

    def mostwanted():

        query = 'select * from criminal_records where wanted = "*****" '
        cursor.execute(query)
        b = cursor.fetchall()
        print()
        print(b)
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        options()

    def del_record():
        q = int(input("Enter the crimnal_ID number you want to delete "))
        query = 'delete from criminal_records where criminal_id={}'.format(q)
        cursor.execute(query)
        con.commit()
        print("Record deleted successfully ")
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        options()

    def graph():
        query = 'select count(crime),crime from criminal_records group by crime'
        cursor.execute(query)
        data = cursor.fetchall()


        list1 = []
        list2 = []

        listlenght = len(data)

        for i in range(listlenght):
                tupl = data[i]
                tuplvalue1 = tupl[0]
                list1.append(tuplvalue1)
                tuplvalue2 = tupl[1]
                list2.append(tuplvalue2)

        print("Press 1 to view BAR GRAPH")
        print("Press 2 to view PIE CHART ")
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        x = int(input("Enter your choice "))
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        if x == 1:
            plt.bar(list2,list1)
            plt.minorticks_on()
            plt.grid(which='major',ls='--',color='black')
            plt.xlabel('Crimes')
            plt.ylabel('Number of Crimes')
            plt.title("Crime rate Graph")
            plt.show()
            options()

        elif x == 2:
            plt.pie(list1,labels=list2,startangle=45,shadow=True)
            plt.title("Crime rate Graph")
            plt.legend(list2,loc='best')
            plt.show()
            options()

        else:
            print("Press the Correct Key")



    if opt_variable == 1:
        search()

    if opt_variable == 2:
        add()
    if opt_variable == 3:
        del_record()

    if opt_variable == 4:
        mostwanted()

    if opt_variable == 5:
        graph()

    if opt_variable == 6:
        print('\n******************************Exit Successful******************************')
        exit()
        


def login():
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    Id = input("Enter your CIA ID: ").upper()
    passwd = input("Enter the password: ").upper()
    if Id == 'SEHAJ' or Id=='ASHURAJ' or Id=='AKSHANSH' and passwd == '311':
        print()
        print("Access Granted !")
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        options()
    else:
        print()
        print("Wrong Credentials ")
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        login()

while(True):
    event , values = window.read()
    if event == 'login':
        login()
    elif event == 'exit':
        print('\n******************************Exit Successful******************************')

window.close()





