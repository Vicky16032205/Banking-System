import accounts_details, data_store

class CreateAccount:
    def __init__(self,fullname, age, mobile, email, account_type,user_id,balance):
        self.__fullname = fullname
        self.__age = age
        self.__mobile = mobile
        self.__email = email
        self.__account_type = account_type
        self.__user_id = user_id
        self.__balance = balance

        user_detail = [self.__fullname, self.__age, self.__mobile, self.__email, self.__account_type,self.__balance]
        user_dict = {self.__user_id:user_detail}
        accounts_details.user_details.update(user_dict)

        data_store.save_user_data(accounts_details.user_details)

    def get_fullname(self):
        return self.__fullname
    
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_email(self):
        return self.__email
    
    def get_account_type(self):
        return self.__account_type
    
    def get_user_id(self):
        return self.__user_id
    
    def get_balance(self):
        return self.__balance
    
    def get_user_password(self):
        return self.__user_password
    
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            raise ValueError("Balance cannot be negative")

    def setting_account(self, user_id, user_password):
        self.__user_id = user_id
        self.__user_password = user_password
        id_pass = {self.__user_id : self.__user_password}
        accounts_details.user_ID_Passwords.update(id_pass)
        data_store.save_password_data(accounts_details.user_ID_Passwords)


def user_register():
    fullname = input("Enter your full name: ")
    try:
        age = int(input("Enter your age: "))
        if age < 18 or age>100:
            print("You are not eligible for bank account opening.")
            return None
    except ValueError:
        print("Enter numbers only.")
        return None
    
    mobile = input("Enter your mobile number: ")
    email = input("Enter your email: ")
    account_type = input("Choose account type (Savings/Current): ")

    try:
        balance = int(input("Enter amount to deposit: "))
        if balance <= 1000:
            print("Invest amount greater than 1000.")
            return None
    except ValueError:
        print("Enter numbered values only.")
        return None
    
    user_count = len(accounts_details.user_ID_Passwords) + 1
    user_id = f"USER{user_count:04d}"
    while True:
        user_password = input("Enter your password: ")
        if len(user_password) < 8:
            print("Enter password of greater than 8 length")
            continue
        
        confirm_password = input("Confirm your password: ")
        if user_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        break

    print(f"Your User ID is: {user_id}. Note it down somewhere as it will be shown only once.")

    account = CreateAccount(fullname, age, mobile, email, account_type,user_id,balance)
    account.setting_account(user_id, user_password)

    return account


def login():
    user_ID_Passwords = data_store.load_password_data()
    user_details = data_store.load_user_data()
    user_id = input("Enter your user id here: ")
    user_password = input("Enter your account password: ")
    
    if user_id in user_ID_Passwords and user_ID_Passwords[user_id] == user_password:
        print("Login Successful")
        if user_id in user_details:
            user_data = user_details[user_id]
            fullname, age, mobile, email, account_type, balance = user_data
            account = CreateAccount(fullname, age, mobile, email, account_type, user_id, balance)
            return True, account
        else:
            print("User data not found.")
            return False, None
    else:
        print("Incorrect user id or password")
        return False, None
