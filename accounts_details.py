admin_details = {}

admin_ID_passwords = {}

import data_store

user_details = data_store.load_user_data()
user_ID_Passwords = data_store.load_password_data()
transaction_history = data_store.load_transaction_data()

admin_details = {}
admin_ID_passwords = {}
