# 🏦 Smart Bank - Banking Management System

A comprehensive Python-based banking management system that simulates real-world banking operations with both customer and administrative functionalities.

## 📋 Table of Contents
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Classes and Modules](#classes-and-modules)
- [Data Storage](#data-storage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)

## ✨ Features

### 👤 Customer Features
- **Account Creation**: Register new bank accounts with personal details
- **Secure Login**: Password-protected user authentication
- **Deposit Money**: Add funds to your account
- **Withdraw Money**: Withdraw funds (with balance validation)
- **Money Transfer**: Transfer funds between accounts
- **Balance Inquiry**: Check current account balance
- **Transaction History**: View detailed transaction records
- **Account Types**: Support for Savings and Current accounts

### 🔧 Admin Features
- **Admin Registration**: Create new admin accounts
- **Admin Login**: Secure admin authentication
- **User Management**: View all registered users
- **User Details**: View specific user information and transaction history
- **Account Deletion**: Remove user accounts from the system
- **System Statistics**: View comprehensive banking system statistics
- **Multi-Admin Support**: Register multiple administrators

## 🔧 System Requirements

- Python 3.x
- No external libraries required (uses built-in modules only)

## 🚀 Installation & Setup

1. **Clone or Download** the project files to your local machine
2. **Navigate** to the project directory:
   ```powershell
   cd Banking_Project
   ```
3. **Run** the main application:
   ```powershell
   python main.py
   ```

## 🎯 Usage

### Starting the Application
Run the main script to start the banking system:
```powershell
python main.py
```

### Main Menu Options
When you start the application, you'll see these options:
1. **Create Account** - Register as a new customer
2. **Login as User** - Access your banking account
3. **Login as Admin** - Access administrative functions
4. **Register as Admin** - Create a new admin account
5. **Exit** - Close the application

### Customer Operations
After logging in as a user:
1. **Deposit** - Add money to your account
2. **Withdraw** - Remove money from your account
3. **Transfer** - Send money to another user
4. **View Balance** - Check your current balance
5. **View Transaction History** - See all your transactions
6. **Logout** - Return to main menu

### Admin Operations
After logging in as an admin:
1. **View All Users** - See all registered customers
2. **View Specific User Details** - Check individual user information
3. **Delete User Account** - Remove a user from the system
4. **View System Statistics** - See banking system overview
5. **Register New Admin** - Add another administrator
6. **Logout** - Return to main menu

## 📁 Project Structure

```
Banking_Project/
├── main.py                 # Main application entry point
├── account_creation.py     # User account creation and login
├── admin_data.py          # Admin functionality and operations
├── accounts_details.py    # Global data storage variables
├── data_store.py          # Data persistence functions
├── admin_credentials.txt  # Admin credentials storage
├── users.pkl             # User data storage (created at runtime)
├── passwords.pkl         # User passwords storage (created at runtime)
├── transactions.pkl      # Transaction history storage (created at runtime)
└── README.md            # Project documentation
```

## 🏗️ Classes and Modules

### `CreateAccount` Class (`account_creation.py`)
- Handles user account creation and management
- Manages user login functionality
- Stores user details and banking information

### `Admin` Class (`admin_data.py`)
- Manages administrative operations
- Provides user management capabilities
- Handles system statistics and reporting

### Data Management (`data_store.py`)
- Handles data persistence using pickle serialization
- Manages file I/O operations for user data, passwords, and transactions
- Provides load/save functions for all data types

### Global Variables (`accounts_details.py`)
- Maintains in-memory storage of user details
- Stores user passwords and transaction history
- Acts as a bridge between modules

## 💾 Data Storage

The system uses two storage methods:

1. **Pickle Files** (for user data):
   - `users.pkl` - User account details
   - `passwords.pkl` - User login credentials
   - `transactions.pkl` - Transaction history

2. **Text Files** (for admin data):
   - `admin_credentials.txt` - Admin login credentials

All data files are created automatically when the application runs for the first time.

## 🔒 Security Features

- **Password Validation**: Minimum 8-character requirement for admin passwords
- **Data Encryption**: User passwords are stored securely
- **Input Validation**: Comprehensive input validation throughout the application
- **Balance Verification**: Prevents overdrafts and negative transactions
- **User Verification**: Validates user existence before transfers

## 🎨 User Interface Features

- **Clear Menu System**: Intuitive navigation through numbered options
- **Error Handling**: Comprehensive error messages and input validation
- **Transaction Logging**: Detailed transaction records with timestamps
- **Formatted Output**: Clean, readable display of account information
- **Confirmation Prompts**: Safety checks for critical operations like account deletion

## 🚀 Future Enhancements

Potential improvements for future versions:
- GUI interface using Tkinter or PyQt
- Database integration (SQLite/MySQL)
- Interest calculation for savings accounts
- Account statements generation
- Email notifications
- Enhanced security with password hashing
- Multi-currency support
- Loan management system

## 🤝 Contributing

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 Notes

- This is a educational project demonstrating OOP concepts in Python
- Data is stored locally in pickle and text files
- The system supports multiple users and admins simultaneously
- All monetary values are displayed in Indian Rupees (₹)

## 🐛 Known Issues

- Data files must be in the same directory as the Python scripts
- No password recovery mechanism implemented
- Limited to local storage only

---

**Smart Bank** - Making banking simple and accessible! 🏦✨

For any questions or support, please refer to the code comments or create an issue in the project repository.
