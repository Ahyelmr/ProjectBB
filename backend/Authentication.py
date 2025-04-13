"""
Authentication.py

This file is responsible for checking files and contains the logic for
registering and logging in users
"""

import os
from FilePathing import resource_path

# This function registers a new user (if there is no existing user with the same credentials)
def register_user(user_name, user_pass):
    if os.path.exists(resource_path("Information/users.txt")):
        with open(resource_path("Information/users.txt"), "r") as file:
            user_data = file.readlines()
            for entry in user_data:
                data = entry.split(":")
                stored_username = data[0]
                stored_password = data[1]
                if stored_username == user_name or stored_password == user_pass:
                    print("Username already exists. Please choose another.")
                    return False

    with open(resource_path("Information/users.txt"), "a") as file:
        file.write(f"{user_name}:{user_pass}:staff\n")
    print("Registration successful!")
    return True

# This function checks if the credentials inputted matches that of an existing user
def user_login(user_name, user_pass):
    if not os.path.exists(resource_path("Information/users.txt")):
        print("No registered users found. Please register first.")
        return False

    with open(resource_path("Information/users.txt"), "r") as file:
        user_data = file.readlines()
        for entry in user_data:
            data = entry.split(":")
            stored_username = data[0]
            stored_password = data[1]
            if stored_username == user_name and stored_password == user_pass:
                print("Login successful!")
                return True
    print("Invalid username or password.")
    return False

# This function checks if the user logging in has admin access or not
def check_admin(user_name, user_pass):
    if  os.path.exists(resource_path("Information/users.txt")):
        with open(resource_path("Information/users.txt"), "r") as file:
            user_data = file.readlines()
            for entry in user_data:
                data = entry.split(":")
                stored_username = data[0]
                stored_password = data[1]
                stored_type = data[2]
                if stored_username == user_name and stored_password == user_pass:
                    print("Admin login successful!")
                    print(stored_type)
                    if "admin" in stored_type:
                        return True

    return False