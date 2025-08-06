import accounts_details, data_store

class Admin:
    def __init__(self, admin_id, password):
        self.__admin_id = admin_id
        self.__password = password
    
    def get_admin_id(self):
        return self.__admin_id
    
    def get_password(self):
        return self.__password
    
    def view_all_users(self):
        """Display all registered users"""
        user_details = data_store.load_user_data()
        if not user_details:
            print("No users found in the system.")
            return
        
        print("\n" + "="*80)
        print("ALL REGISTERED USERS")
        print("="*80)
        print(f"{'User ID':<12} {'Name':<20} {'Age':<5} {'Mobile':<12} {'Email':<25} {'Account Type':<12} {'Balance':<10}")
        print("-"*80)
        
        for user_id, details in user_details.items():
            fullname, age, mobile, email, account_type, balance = details
            print(f"{user_id:<12} {fullname:<20} {age:<5} {mobile:<12} {email:<25} {account_type:<12} ₹{balance:<10}")
        print("="*80)
    
    def view_user_details(self, user_id):
        """View specific user details"""
        user_details = data_store.load_user_data()
        if user_id in user_details:
            fullname, age, mobile, email, account_type, balance = user_details[user_id]
            print(f"\nUser Details for {user_id}:")
            print(f"Name: {fullname}")
            print(f"Age: {age}")
            print(f"Mobile: {mobile}")
            print(f"Email: {email}")
            print(f"Account Type: {account_type}")
            print(f"Balance: ₹{balance}")
            
            # Show transaction history
            transaction_history = data_store.load_transaction_data()
            if user_id in transaction_history:
                print(f"\nTransaction History:")
                for transaction in transaction_history[user_id]:
                    print(f"- {transaction}")
            else:
                print("No transaction history found.")
        else:
            print("User not found.")
    
    def delete_user(self, user_id):
        """Delete a user account"""
        user_details = data_store.load_user_data()
        user_passwords = data_store.load_password_data()
        transaction_history = data_store.load_transaction_data()
        
        if user_id in user_details:
            # Remove from user details
            del user_details[user_id]
            accounts_details.user_details = user_details
            data_store.save_user_data(user_details)
            
            # Remove from passwords
            if user_id in user_passwords:
                del user_passwords[user_id]
                accounts_details.user_ID_Passwords = user_passwords
                data_store.save_password_data(user_passwords)
            
            # Remove transaction history
            if user_id in transaction_history:
                del transaction_history[user_id]
                accounts_details.transaction_history = transaction_history
                data_store.save_transaction_data(transaction_history)
            
            print(f"User {user_id} has been successfully deleted.")
        else:
            print("User not found.")
    
    def view_system_stats(self):
        """View system statistics"""
        user_details = data_store.load_user_data()
        total_users = len(user_details)
        total_balance = sum(details[5] for details in user_details.values())
        
        savings_count = sum(1 for details in user_details.values() if details[4].lower() == 'savings')
        current_count = sum(1 for details in user_details.values() if details[4].lower() == 'current')
        
        print(f"\n" + "="*40)
        print("SYSTEM STATISTICS")
        print("="*40)
        print(f"Total Users: {total_users}")
        print(f"Total System Balance: ₹{total_balance}")
        print(f"Savings Accounts: {savings_count}")
        print(f"Current Accounts: {current_count}")
        print("="*40)


def admin_register():
    """Register a new admin"""
    admin_id = input("Enter your Admin ID: ")
    
    # Check if admin already exists
    if admin_id in accounts_details.admin_ID_passwords:
        print("Admin ID already exists!")
        return None
    
    while True:
        admin_password = input("Enter Admin password (minimum 8 characters): ")
        if len(admin_password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        
        confirm_password = input("Confirm your password: ")
        if admin_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        break
    
    # Store admin credentials
    accounts_details.admin_ID_passwords[admin_id] = admin_password
    data_store.save_admin_data(accounts_details.admin_ID_passwords)
    
    admin = Admin(admin_id, admin_password)
    print(f"Admin account created successfully for {admin_id}")
    return admin


def admin_login():
    """Admin login function"""
    admin_credentials = data_store.load_admin_data()
    admin_id = input("Enter your Admin ID: ")
    admin_password = input("Enter your password: ")
    
    if admin_id in admin_credentials and admin_credentials[admin_id] == admin_password:
        print("Admin Login Successful")
        admin = Admin(admin_id, admin_password)
        return True, admin
    else:
        print("Incorrect admin ID or password")
        return False, None


def admin_operations(admin):
    """Handle admin operations"""
    while True:
        print(f"\nWelcome Admin {admin.get_admin_id()}!")
        print("\nAdmin Operations:")
        print("1. View All Users")
        print("2. View Specific User Details")
        print("3. Delete User Account")
        print("4. View System Statistics")
        print("5. Register New Admin")
        print("6. Logout")
        
        try:
            choice = int(input("Choose an option (1-6): "))
            if choice < 1 or choice > 6:
                print("Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 1:
            admin.view_all_users()
        
        elif choice == 2:
            user_id = input("Enter User ID to view details: ")
            admin.view_user_details(user_id)
        
        elif choice == 3:
            user_id = input("Enter User ID to delete: ")
            confirm = input(f"Are you sure you want to delete user {user_id}? (yes/no): ")
            if confirm.lower() == 'yes':
                admin.delete_user(user_id)
            else:
                print("Delete operation cancelled.")
        
        elif choice == 4:
            admin.view_system_stats()
        
        elif choice == 5:
            admin_register()
        
        elif choice == 6:
            print("Admin logged out successfully!")
            break