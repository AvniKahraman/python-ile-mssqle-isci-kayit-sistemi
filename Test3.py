import getpass
import random
import datetime
import pypyodbc    #sql bağlanması için gereken kütüphane
import os     
import time
import pandas
import msvcrt
import sys
import msvcrt

db = pypyodbc.connect(              #SQl aktif hale getirdim
    'Driver={SQL SERVER};'
    'Server=DESKTOP-264MAM5;'
    'Database=project1;'
    'Trusted_Connection=True;'
)

imlec = db.cursor() 
print("1---> Existing Registration")
print("2---> New Registration ")
print("3---> Exit ")
label=int(input("---> Please Enter Your Request ----> "))


leon=int(random.randint(12,9999))

while True:
    if label ==1:
        userID = int(input("\033[1mEnter the userID "))
        password = getpass.getpass(prompt='Enter your password: ')
        imlec.execute("SELECT * FROM Users WHERE UsersID=? AND Password=?", [userID,password])
        Result = imlec.fetchone()
        while True:
            
            if Result:
                print("\03 Enter is Successful ")
                time.sleep(0.5)
                os.system('cls')
                imlec.execute("SELECT * FROM DEPARTMANS WHERE ID=? ", [userID]) #departman tablosunun ıd sini kontrol ederek  
                Result1 = imlec.fetchone() 
                
                if Result1[1] == "Admin":
                    print ("\03 Welcome to the Admin Panel")
                    print("1-> Display Employee List: ")
                    print("2-> Adding New Record: ")
                    print("3-> Deleting Existing Record: ")
                    print("4-> Searching in Records: ")
                    print("5-> Change Password:  ")
                    print("6-> Display Every list: ")
                    print("7-> Adding New authorizations: ")
                    print("8-View Your Salary")
                    print("9-Exit")
                    number1=int(input("Select an operation: "))
                    os.system('cls')
                    
                    if number1==1:
                        print("Welcome to Employee Displaying System\n")
                        imlec.execute("select * from EMPLOYEE")
                        liste=imlec.fetchall()
                        df = pandas.DataFrame(liste, columns = ['ID','FirstName','SecondName','Surname','Birthday','Birthplace','Departmans','EmployeeID'])

                        print(df.to_string()) 
                        input("Press Enter to Continue!")
                        
                    
                    elif number1==2:
                        print("-->Welcome To Record Adding Screen<--")
                        ID=int(input("Please Enter User ID: "))
                        FirstName=input("Please Enter User Name: ")
                        SecondName=input("Please Enter Second Name If There is: ")
                        Surname=input("Please Enter User's surname: ")
                        Birhday = input("Please Enter Users Date of Birth as  yyyy-aa-gg")
                        birthday_datetime = datetime.datetime.strptime(Birhday, '%Y-%m-%d')
                        birthday_array=Birhday.split("-")
                        x = datetime.datetime(int(birthday_array[0]),int(birthday_array[1]),int(birthday_array[2]))

                        BirthPlace=input("Please Enter User Place of Birth: ")
                        Departmans=input("Please Enter Department of  User: ")
                        
                        

                        imlec.execute("INSERT INTO EMPLOYEE (ID, FirstName, SecondName, Surname, Birthdate, Birthplace, Departmans,EmployeeID) VALUES (?, ?, ?, ?, ?, ?, ?,?)", (ID, FirstName, SecondName, Surname, x.date(), BirthPlace, Departmans,leon))
                        db.commit()
                        imlec.close()  
                        time.sleep(0.5)
                        print("Successfully Registered")  
                        print("Please press any key")
                        msvcrt.getch()
                        char = msvcrt.getch() 
                        
                    

                    elif number1==3:

                        print("Welcome to Delete Screen")
                        user_ID = int(input("Please  Enter User ID to Delete: "))
                        imlec.execute("DELETE FROM EMPLOYEE WHERE ID = ?",(user_ID,))

                        db.commit()
                        print("User Deleted Successfully")

                    elif number1==4:
                        print("Welcome to User Display Screen ")
                        musakka  = int(input("Please Enter a user ID to Display: "))    
                        imlec.execute("SELECT * FROM EMPLOYEE WHERE ID=?", (musakka,))
                        musakka = imlec.fetchone()
                        print("ID:", musakka[0])
                        print("First Name:", musakka[1])
                        print("Second Name:", musakka[2])
                        print("Surname:", musakka[3])
                        print("Birthday:", musakka[4])
                        print("Birthplace:", musakka[5])
                        print("Departmans:", musakka[6])
                        print("Please press any key")
                        msvcrt.getch()
                        
                    
                    elif number1 == 5:
                            kafir=db.cursor() 
                            print("Welcome to Password Changing Screen")
                            şifre1 = getpass.getpass(prompt='Please Enter Old Password: ')
                            kafir.execute("SELECT * FROM Users WHERE Password=?", [şifre1])
                            tamam = kafir.fetchone() 

                            if tamam:
                                şifre2=int(input("Pleaase Enter New Password: "))
                                imlec.execute("UPDATE Users SET Password=? WHERE UsersID=?", [şifre2, userID])
                                db.commit()
                                time.sleep(0)
                                print("Password Changed Successfully")
                                time.sleep(0)
                                print("Please press any key")
                        
                                print("----->Redirectioning to the Main Menu ---->")
                                
                                msvcrt.getch()
                                time.sleep(0.9)
                            elif tamam is None:

                                print("Wrong old password.") 
                            


                    elif number1 == 6:
                        imlec.execute("SELECT E.ID,E.FirstName,E.SecondName,E.Surname,E.Birthdate,E.Department,U.Password,U.Role,D.Role_Desc  FROM EMPLOYEE E,DEPARTMENT D,Users U WHERE E.Department = D.ID AND D.RoleID=U.RoleID ORDER BY E.ID ASC;")
                        patlican=imlec.fetchall()
                        df = pandas.DataFrame(patlican,columns = ['ID','FirstName','SecondName','Surname','Birthday','Department','Password','Role','Role_Desc'])
                        print(df.to_string()) 
                        print("Please press any key to cotinue\n")
                        msvcrt.getch()


                    elif number1 == 7:
                        print("Authorizations Screen")
                       
                        gmod=db.cursor() 
                        zalim2=int(input("Please Enter User ID to Change Authorization: "))
                        zalim3=input("Please Enter New Authorization Role: ")
                        imlec.execute("UPDATE DEPARTMANS SET Roles=? WHERE ID=?", [zalim3, zalim2])
                        db.commit()
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                        
                    elif number1==8:
                        imlec.execute("Select * From SalaryT Where ID = ?",[userID])
                        liste=imlec.fetchall()
                        df = pandas.DataFrame(liste,columns=['','Salary','']) 
                        print(df.to_string())
                        
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                    elif number1 == 9:
                        sys.exit()
                        
                elif Result1[1]== "Moderator":
                    print("\033[1Welcome to Moderator Panel")
                    print("1->Add a New Record")
                    print("2->Delete a Record ")
                    print("3->Display Employee List")
                    print("4->Change Password")
                    print("5-View Your Salary")
                    print("6-Exit")
                    line=int(input("Please Enter a Function to Proceed: "))
                    time.sleep(0.5)
                    
                    if line == 1:
                        print("Werlcome to User Adding Screen") 
                        ID=int(input("Please Enter User ID to Register: "))
                        FirstName=input("Please Enter User Name: ")
                        SecondName=input("Please Enter Second Name If There is: ")
                        Surname=input("Please Enter User's surname: ")
                        Birhday = input("Please Enter Users Date of Birth as  yyyy-aa-gg: ")
                        birthday_datetime = datetime.datetime.strptime(Birhday, '%Y-%m-%d')
                        birthday_array=Birhday.split("-")
                        x = datetime.datetime(int(birthday_array[0]),int(birthday_array[1]),int(birthday_array[2]))

                        BirthPlace=input("Please Enter User Place of Birth: ")
                        Departmans=input("Please Enter Department of  User: ")

                        imlec.execute("INSERT INTO EMPLOYEE (ID, FirstName, SecondName, Surname, Birthdate, Birthplace, Departmans,UserID,'EmployeeID') VALUES (?, ?, ?, ?, ?, ?, ?,?)", (ID, FirstName, SecondName, Surname, x.date(), BirthPlace, Departmans,leon))
                        db.commit()
                        imlec.close()  
                        time.sleep(0.5)
                        print("Successfully Registered")    
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                        break
                    
                    elif line == 2:
                        print("Welcome to Record Deleting Screen")
                        row_id = int(input("Please Enter User ID to Delete:"))
                        imlec.execute("DELETE FROM EMPLOYEE WHERE ID=?", (row_id))
                        db.commit()
                        print("Record Deleted Successfully")
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                        
                    elif line == 3:
                        print("Welcome to Employee Display Screen.\n")
                        imlec.execute("select * from EMPLOYEE")
                        liste=imlec.fetchall()
                        df = pandas.DataFrame(liste, columns = ['ID','FirstName','SecondName','Surname','Birthday','Birthplace','Departmans','EmployeeID'])

                        print(df.to_string()) 
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                        break
                    elif line == 4:
                        
                            kafir=db.cursor() 
                            print("Welcome to Password Changing Screen")
                            şifre1 = getpass.getpass(prompt='Please Enter Old Password:  ')
                            kafir.execute("SELECT * FROM Users WHERE Password=?", [şifre1])
                            tamam = kafir.fetchone() 

                            if tamam:
                                şifre2=int(input("Pleaase Enter New Password: "))
                                imlec.execute("UPDATE Users SET Password=? WHERE UsersID=?", [şifre2, userID])
                                db.commit()
                                time.sleep(0)
                                print("Password Changed Successfully")
                                time.sleep(0)
                                print("-----> Redirectioning to the Main Menu---->")
                                print("Please press any key to cotinue")
                                msvcrt.getch()

                                time.sleep(0.9)
                            elif tamam is None:

                                print("Wrong old password. .") 
                            else:
                                print("Wrong Password ")
                                
                    if line == 5:
                        imlec.execute("Select * From SalaryT Where ID = ?",[userID])
                        liste=imlec.fetchall()
                        df = pandas.DataFrame(liste,columns=['','Salary','']) 
                        print(df.to_string())
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                        if line == 6:
                            sys.exit()
                            
                elif Result1[1]=="User":
                    
                    print("\033[1Welcome to User Panel")
                    print("1-Display Employee List  ")
                    print("2-Changing Password")
                    print("3-View your Salary")
                    print("4-Exit")
                    patates=int(input("Please Enter a Function to Proceed:"))
                    if  patates == 1:
                        print("Welcome to Employee Display Screen .\n")
                        imlec.execute("select * from EMPLOYEE")
                        liste=imlec.fetchall()
                        df = pandas.DataFrame(liste, columns = ['ID','FirstName','SecondName','Surname','Birthday','Birthplace','Departmans','EmployeeID'])

                        print(df.to_string()) 
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                        break
                    elif patates==2 : 
                        kafir=db.cursor() 
                        print("Welcome to Password Changing Screen")
                        şifre1 = getpass.getpass(prompt='Please Enter old password: ')
                        kafir.execute("SELECT * FROM Users WHERE Password=?", [şifre1])
                        tamam = kafir.fetchone()
                        print("Please press any key to cotinue")
                        msvcrt.getch()
 

                        if tamam:
                            şifre2=int(input("Please Enter New Password: "))
                            imlec.execute("UPDATE Users SET Password=? WHERE UsersID=?", [şifre2, userID])
                            db.commit()
                            time.sleep(0)
                            print("Password Changed Successfully")
                            time.sleep(0)
                            print("Please press any key to cotinue")
                            msvcrt.getch()

                            print("-----> Redirectioning to the Main Menu ---->")
                            time.sleep(0.9)
                        elif tamam is None:
                            print("Wrong Old Password") 
                        else:
                            print("Wrong Password ")    
                    elif patates==3:
                        imlec.execute("Select * From SalaryT Where ID = ?",[userID])
                        liste=imlec.fetchall()
                        df = pandas.DataFrame(liste,columns=['','Salary','']) 
                        print(df.to_string())
                        print("Please press any key to cotinue")
                        msvcrt.getch()

                    if patates == 4:
                        sys.exit()
            else:
                time.sleep(0)
                os.system('cls')
                print("Password is wrong, Please Try Again ")
    elif label == 2:
        imlec=db.cursor() 
        print("-->Welcome To Record Adding Screen<--")
        ID=int(input("Enter User ID: "))
        FirstName=input("Please Enter User Name:")
        SecondName=input("Please Enter Second Name If There is: ")
        Surname=input("Enter User's surname: ")
        Birhday = input("Please Enter Users Date of Birth as  yyyy-aa-gg")
        birthday_datetime = datetime.datetime.strptime(Birhday, '%Y-%m-%d')
        birthday_array=Birhday.split("-")
        x = datetime.datetime(int(birthday_array[0]),int(birthday_array[1]),int(birthday_array[2]))
        

        BirthPlace=input("Please Enter User Place of Birth: ")
        Departmans=input("Please Enter Department of  User: ")

        imlec.execute("INSERT INTO EMPLOYEE (ID, FirstName, SecondName, Surname, Birthdate, Birthplace, Departmans,EmployeeID) VALUES (?, ?, ?, ?, ?, ?, ?,?)", (ID, FirstName, SecondName, Surname, x.date(), BirthPlace, Departmans,leon))
        db.commit()

        print("--->Password Creation Screen<---")
        password1=int(input("Please Enter Password: "))

        imlec.execute("INSERT INTO Users(UsersID,Password,) VALUES (?,?)",(ID,password1))
        db.commit()
        time.sleep(0)
        os.system('cls')
        print("Registered Successfully")

        imlec.execute("UPDATE DEPARTMANS SET Roles='User' WHERE ID=?", (ID,))
        db.commit()
        print("Your role is Set as default employee, please contact with Admin ")
        
        

        imlec.close()  
        time.sleep(0.5)
    elif label == 3:
        exit_program = input("Exit? (Y/N): ")
        if exit_program == "Y" or "y":
            sys.exit()
    else:
        print("Please Enter one of above.")
        time.sleep(0)
        os.system('cls')