import mysql.connector
database = mysql.connector.connect(host='localhost', username='root', password='Marshmellow@10', database='kongfile_mail')
mycursor = database.cursor()

class userDetails:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def isAlreadyExistingUser(self):
        mycursor.execute("select user_id, user_name, user_password from user_details where user_name like %s",(self.user_name,))
        details = mycursor.fetchall()
        if details[0][1] == self.user_name and details[0][2] == self.user_password:
            return details[0][0]

    def personalDetails(self):
        mycursor.execute("select * from user_details where user_id like %s", (user_id,))
        details = mycursor.fetchall()
        print('Username: \t\t', details[0][1])
        print('E-mail ID: \t\t', details[0][2])
        print('Phone Number: \t', details[0][3])
        print('Password: \t\t', details[0][4])

    def modifyDetails(self):
        print("What do you want to update?")
        print("1. Username\n2. Email-ID\n3. Phone_number\n4. Password")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            userName = str(input("Enter your new username: "))
            passWord = str(input("To Confirm, please enter your password: "))
            mycursor.execute('update user_details set user_name = replace(user_name,"userName") where user_password = "passWord"')
            database.commit()

class adminDetails:
    def __init__(self, admin_name, admin_password):
        self.admin_name = admin_name
        self.admin_password = admin_password

    def isAlreadyExistingAdmin(self):
        mycursor.execute("select admin_id, admin_name, admin_password from admin_details where admin_name like %s",(self.admin_name,))
        details = mycursor.fetchall()
        if details[0][1] == self.admin_name and details[0][2] == self.admin_password:
            return details[0][0]

class displayAll:
    def list_planDetails(self):
        mycursor.execute("select * from plan_details")
        plan = mycursor.fetchall()
        plan_id = [plan[0][0],plan[1][0],plan[2][0]]
        print('Plan_type             :',plan[0][1],'\t''\t',plan[1][1],'\t''\t',plan[2][1])
        print('Maximum_Transfer_Size :',plan[0][2],'\t''\t',plan[1][2],'\t''\t',plan[2][2])
        print('Files Available for   :',plan[0][3],'\t',plan[1][3],'\t',plan[2][3])
        print('Plan_Cost/month       :',plan[0][4],'\t''\t''\t',plan[1][4],'\t''\t''\t',plan[2][4])
        print('Password_Protection   :',plan[0][5],'\t''\t''\t',plan[1][5],'\t''\t',plan[2][5])
        print('Storage_Capacity      :',plan[0][6],'\t''\t',plan[1][6],'\t''\t',plan[2][6])
        print('Show_Ads              :',plan[0][7],'\t''\t',plan[1][7],'\t''\t',plan[2][7])

class FileDetails:
    def __init__(self):
        self.user_id = user_id

    def fileCreation(self):
        file_name = str(input("Enter the file_name: "))
        file_txt = input()
        mycursor.execute("insert into file_details(file_id, file_name, file_txt) values(NULL,%s,%s)", (file_name, file_txt))
        database.commit()

    def fileDeletion(self):
        file_name = str(input("Enter the file_name: "))
        mycursor.execute("select file_name,file_txt from file_details where file_name like %s", (file_name,))
        file = mycursor.fetchall()
        print('File_Name',file[0][0])
        print('',file[0][1])
        print("Are you want to remove the file? ")
        print("1. Yes")
        print("2. No")
        option = int(input("Enter your option: "))
        if option == 1:
            mycursor.execute("delete from file_details where file_name like %s", (file_name,))
            database.commit()
            print("File is removed.")
        else:
            print("No file is removed")

    def fileContains(self):
        file_name = str(input("Enter the file_name: "))
        mycursor.execute("select file_name,file_txt from file_details where file_name like %s", (file_name,))
        file = mycursor.fetchall()
        print('File_Name: ', file[0][0])
        print('', file[0][1])

class plans:
    def __init__(self):
        self.planId = planId


class paymentDetails:
    def __init__(self):
        self.user_id = user_id
        self.planId = planId

    def payment(self):

        if planId > 1:
            card_number = str(input("Enter your Card_number: "))
            mycursor.execute("insert into payment_details(payment_id,user_id,plan_id,card_number) values(NULL,%s,%s,%s)",(user_id,planId,card_number,))
            database.commit()

if __name__ == '__main__':
    print("Welcome to Kong-File Mail")
    print("\t1. Login")
    print("\t2. Register")
    print("\t3. Admin")
    count = 0
    amount = 0
    destination = int(input("Enter your destination: "))
    #destination = destination.lower()
    if destination == 2:
        user_name = input("Enter your username: ")
        email_id = input("Enter your e-mail_id: ")
        phone_no = input("Enter your phone_number: ")
        user_password = input("Enter your password: ")
        mycursor.execute("insert into user_details(user_id, user_name, email_id, phone_no, user_password) values(NULL, %s, %s, %s, %s)",(user_name, email_id, phone_no, user_password,))
        database.commit()
        print("Sign Up Success..!!")
        print("\n")
        print("Do you want to...")
        print("\t1. Create a file")
        print("\t2. Remove a file")
        print('\t3. View the file')
        print('\t4. View the plans')
        print('\t5. Logout')
        option = int(input("Enter your choice: "))
        if option == 1:
           create = FileDetails()
           create.fileCreation()
        elif option == 2:
            remove = FileDetails()
            remove.fileDeletion()

        elif option == 3:
            view = FileDetails()
            view.fileContains()

        elif option == 4:
            List_the_plans = displayAll()
            List_the_plans.list_planDetails()
            print("Want to buy a plan?")
            print('1.Pro')
            print('2. Business')
            planId =int(input("Enter the option to select the plan: "))
            count = 0
            amount = 0
            if planId > 0 and planId < 2:
                payments = paymentDetails()
                payments.payment()
                count += 1
                amount += 1000
            elif planId > 1 and planId < 3:
                payments = paymentDetails()
                payments.payment()
                count += 1
                amount += 3000
            else:
                exit()

        elif option == 5:
            print('Logged Out Successfully..!!!')
            exit()

        else:
            print('Please Login and select correct option')


    if destination == 1:
        user_name = str(input("Enter your username: "))
        user_password = str(input("Enter your password: "))
        user_name = user_name.capitalize()
        userValidation =  userDetails(user_name, user_password)
        user_id = userValidation.isAlreadyExistingUser()
        if user_id:
            print("Do you want to...")
            print('\t1. Create a file')
            print('\t2. Remove a file')
            print('\t3. View the file')
            print('\t4. View your personal details')
            print('\t5. Modify your personal information')
            print('\t6. View the plans')
            print('\t7. Logout')
            option = int(input("Enter your choice: "))
            if option == 1:
                create = FileDetails()
                create.fileCreation()
            elif option == 2:
                remove = FileDetails()
                remove.fileDeletion()

            elif option == 3:
                view = FileDetails()
                view.fileContains()

            elif option == 4:
                persInform = userDetails(user_name,user_password)
                persInform.personalDetails()

            elif option == 5:
                modifydetails = userDetails(user_name,user_password)
                modifydetails.modifyDetails()

            elif option == 6:
                List_the_plans = displayAll()
                List_the_plans.list_planDetails()
                print("Want to buy a plan?")
                planId = int(input("Enter the option to select the plan: "))
                print('1.Pro')
                print('2. Business')
                if planId > 0 and planId < 2:
                    payments = paymentDetails()
                    payments.payment()
                    count += 1
                    amount += 1000
                    mycursor.execute("insert into records(count,amount) values(%s,%s)",(count,amount))
                    database.commit()
                elif planId > 1 and planId < 3:
                    payments = paymentDetails()
                    payments.payment()
                    count += 1
                    amount += 3000
                    mycursor.execute("insert into records(count,amount) values(%s,%s)", (count, amount))
                    database.commit()
                else:
                    exit()


    if destination == 3:
        admin_name = str(input("Enter your username: "))
        admin_password = str(input("Enter your password: "))
        adminValidation = adminDetails(admin_name, admin_password)
        admin_id = adminValidation.isAlreadyExistingAdmin()
        if admin_id:
            print('1. Plans''\t2. Records')
            option = int(input("Enter your choice: "))
            if option == 1:
                List_the_plans = displayAll()
                List_the_plans.list_planDetails()
            if option == 2:
                mycursor.execute("select * from records")
                Records = mycursor.fetchall()
                print("Total Plans sold: ", Records[0][0])
                print("Total amount: \t", Records[0][1])
