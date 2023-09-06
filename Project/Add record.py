import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="project")
cursor=con.cursor()
def add():

    print("-------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------")
    id = int(input("Enter the Crimnal ID: "))
    name = input("Enter Name of Criminal: ")
    dob = input("Enter Date of Birth of criminal: ")
    country = input("Enter Country of criminal: ")
    wanted = input("Enter the Wanted Level: ")
    crime = input("Enter Crime done by criminal: ")
    current = input("Enter status of criminal: ")
    doa = input("Enter Date of Arrest: ")
    dor = input("Enter Date of Release: ")
    query = "insert into record values({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(id, name, dob, country,wanted, crime, current, doa,dor)
    cursor.execute(query)
    con.commit()
    print("RECORD ADDED SUCCESSFULLY")
    print("-------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------")

while True:
    add()
    print()
    print("Press Y to insert more records")
    print("Press N to Go to main menu")
    choice=input("Press the Key: ").upper()
    print()
    if choice=='Y':
        add()
    if choice=='N':
        exit()



