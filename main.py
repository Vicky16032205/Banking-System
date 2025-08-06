import account_creation, admin_data, data_store, accounts_details
from datetime import datetime

def log_transaction(user_id, message):
    now = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    full_message = f"{message} on {now}"

    if user_id not in accounts_details.transaction_history:
        accounts_details.transaction_history[user_id] = []

    accounts_details.transaction_history[user_id].append(full_message)

    data_store.save_transaction_data(accounts_details.transaction_history)


def user_operations(user):
    """Handle user banking operations"""
    while True:
        print("\nChoose from the following operations:")
        print("1. Deposit \n2. Withdraw \n3. Transfer \n4. View Balance \n5. View Transaction History \n6. LogOut")
        
        try:
            user_in_input = int(input("Pick your option: "))
            if user_in_input < 1 or user_in_input > 6:
                print("Enter input within 1 to 6 only")
                continue
        except ValueError:
            print("Enter valid input only in numbers.")
            continue

        if user_in_input == 1:  # Deposit
            try:
                deposit = int(input("Enter amount to deposit: "))
                if deposit <= 0:
                    print("Please enter a positive amount.")
                else:
                    new_balance = user.get_balance() + deposit
                    user.set_balance(new_balance)
                    accounts_details.user_details[user.get_user_id()][5] = user.get_balance()
                    log_transaction(user.get_user_id(), f"Deposited ₹{deposit}")
                    print("Amount deposited successfully!")
                    print(f"Balance in your account: ₹{user.get_balance()}")
                    data_store.save_user_data(accounts_details.user_details)
            except ValueError:
                print("Please enter a valid number.")

        elif user_in_input == 2:  # Withdraw
            try:
                withdraw = int(input("Enter amount to withdraw: "))
                if withdraw <= 0:
                    print("Please enter a positive amount.")
                elif withdraw > user.get_balance():
                    print("Cannot withdraw more than your account balance.")
                else:
                    new_balance = user.get_balance() - withdraw
                    user.set_balance(new_balance)
                    accounts_details.user_details[user.get_user_id()][5] = user.get_balance()
                    log_transaction(user.get_user_id(), f"Withdrawn ₹{withdraw}")
                    print("Amount withdrawn successfully!")
                    print(f"Remaining balance: ₹{user.get_balance()}")
                    data_store.save_user_data(accounts_details.user_details)
            except ValueError:
                print("Please enter a valid number.")

        elif user_in_input == 3:  # Transfer
            receiver_id = input("Enter Receiver's User ID: ")
            if receiver_id not in accounts_details.user_details:
                print("Receiver ID not found. Please check and try again.")
            elif receiver_id == user.get_user_id():
                print("You cannot transfer money to yourself.")
            else:
                try:
                    money = int(input("Enter amount to send: "))
                    if money <= 0:
                        print("Please enter a positive amount.")
                    elif user.get_balance() < money:
                        print("Insufficient balance for this transfer.")
                    else:
                        receiver_user = accounts_details.user_details[receiver_id]
                        receiver_balance = receiver_user[5]
                        
                        new_balance = user.get_balance() - money
                        user.set_balance(new_balance)
                        accounts_details.user_details[user.get_user_id()][5] = user.get_balance()
                        accounts_details.user_details[receiver_id][5] = receiver_balance + money
                        
                        log_transaction(user.get_user_id(), f"Transferred ₹{money} to {receiver_id}")
                        log_transaction(receiver_id, f"Received ₹{money} from {user.get_user_id()}")
                        
                        print(f"Transfer successful! Sent ₹{money} to {receiver_id}")
                        print(f"Your remaining balance: ₹{user.get_balance()}")
                        data_store.save_user_data(accounts_details.user_details)
                except ValueError:
                    print("Please enter a valid number.")

        elif user_in_input == 4:  # View Balance
            print(f"Your current balance: ₹{user.get_balance()}")

        elif user_in_input == 5:  # Transaction History
            print("\nYour Transaction History:")
            history = accounts_details.transaction_history.get(user.get_user_id(), [])
            if history:
                for entry in history:
                    print(f"- {entry}")
            else:
                print("No transactions found.")

        elif user_in_input == 6:  # Logout
            print("Thanks for using Smart Bank!")
            break
  
def main():
    print("Welcome to Smart Bank! We are happy to see you here 😊.")
    
    while True:
        print("\nChoose from the following operations:")
        print("1. Create Account \n2. Login as User \n3. Login as Admin \n4. Register as Admin \n5. Exit")
        
        try:
            user_input = int(input("Choose from these given inputs: "))
            if user_input < 1 or user_input > 5:
                print("Enter input within 1 to 5 only")
                continue
        except ValueError:
            print("Enter valid input only in numbers.")
            continue

        if user_input == 1:
            user = account_creation.user_register()
            if user is not None:
                print(f"Account created successfully for {user.get_user_id()}")

        elif user_input == 2:
            flag, user = account_creation.login()
            if flag:
                print(f"User {user.get_user_id()} logged in successfully")
                user_operations(user)

        elif user_input == 3:
            flag, admin = admin_data.admin_login()
            if flag:
                print(f"Admin {admin.get_admin_id()} logged in successfully")
                admin_data.admin_operations(admin)

        elif user_input == 4:
            admin = admin_data.admin_register()
            if admin is not None:
                print("Admin registration successful!")

        elif user_input == 5:
            print("Thank you for using Smart Bank! Goodbye!")
            break

if __name__ == "__main__":
    main()