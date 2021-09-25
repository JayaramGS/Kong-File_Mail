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
        print('\n')
        print(plan_id[0],'Free')
        print(plan_id[1],'Pro')
        print(plan_id[2],'Business')

class plans:
    def __init__(self,planId):
        self.planId = planId


class paymentDetails:
    def __init__(self):
        self.user_id = user_id
        self.planId = planId

    def payment(self):
        count = 0
        amount = 0
        if planId == '2':
            count += 1
            amount += 1000
        elif planId == '3':
            count += 1
            amount += 3000
        else:
            pass
        card_number = input("Enter your Card_number: ")
        mycursor.execute("insert into payment_details(payment_id,user_id,plan_id,card_number,count,amount) values(NULL,%s,%s,%s,%s,%s)",(user_id,planId,card_number,count,amount,))
        database.commit()


if __name__ == '__main__':
    print("Welcome to Kong-File Mail")
    print("Sign_up")
    print("Sign_in")
    print("Admin")
    destination = input("Enter your destination: ")
    destination = destination.capitalize()
    if destination == 'Sign_up':
        user_name = input("Enter your username: ")
        email_id = input("Enter your e-mail_id: ")
        phone_no = input("Enter your phone_number: ")
        user_password = input("Enter your password: ")
        mycursor.execute("insert into user_details(user_id, user_name, email_id, phone_no, user_password) values(NULL, %s, %s, %s, %s)",(user_name, email_id, phone_no, user_password,))
        database.commit()
        print("Sign Up Success..!!")
        List_the_plans = displayAll()
        List_the_plans.list_planDetails()

        planId = input("Enter the option to select the plan: ")
        payments = paymentDetails()
        payments.payment()


    if destination == 'Sign_in':
        user_name = str(input("Enter your username: "))
        user_password = str(input("Enter your password: "))
        userValidation =  userDetails(user_name, user_password)
        user_id = userValidation.isAlreadyExistingUser()
        if user_id:
            List_the_plans = displayAll()
            List_the_plans.list_planDetails()
            planId = input("Enter the option to select the plan: ")
            payments = paymentDetails()
            payments.payment()

    if destination == 'Admin':
        print('1. Plans','\n','2. Records')
        option = int(input("Enter your choice: "))
        if option == 1:
            List_the_plans = displayAll()
            List_the_plans.list_planDetails()
        if option == 2:
            mycursor.execute("select count, amount from payment_details")
            records = mycursor.fetchall()
            print("Total Plans sold: ", records[0][0])
            print("Total amount: ",'\t', records[0][1])
