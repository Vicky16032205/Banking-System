import pickle
import os

USERS_FILE = "users.pkl"
PASSWORDS_FILE = "passwords.pkl"
TRANSACTION_FILE = "transactions.pkl"

def save_pickle(file_path, data):
    with open(file_path, "wb") as f:
        pickle.dump(data, f)

def load_pickle(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "rb") as f:
        return pickle.load(f)

def load_user_data():
    return load_pickle(USERS_FILE)

def save_user_data(data):
    save_pickle(USERS_FILE, data)

def load_password_data():
    return load_pickle(PASSWORDS_FILE)

def save_password_data(data):
    save_pickle(PASSWORDS_FILE, data)

def load_transaction_data():
    return load_pickle(TRANSACTION_FILE)

def save_transaction_data(data):
    save_pickle(TRANSACTION_FILE, data)

def save_admin_data(admin_data):
    """Save admin credentials to file"""
    try:
        with open("admin_credentials.txt", "w") as file:
            for admin_id, password in admin_data.items():
                file.write(f"{admin_id},{password}\n")
    except Exception as e:
        print(f"Error saving admin data: {e}")

def load_admin_data():
    """Load admin credentials from file"""
    admin_data = {}
    try:
        with open("admin_credentials.txt", "r") as file:
            for line in file:
                if line.strip():
                    admin_id, password = line.strip().split(",", 1)
                    admin_data[admin_id] = password
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading admin data: {e}")
    return admin_data
