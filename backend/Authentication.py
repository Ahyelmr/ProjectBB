import os

from backend.FilePathing import resource_path


def register_user(user_name, user_pass):
    if os.path.exists(resource_path("Information/users.txt")):
        with (open(resource_path("Information/users.txt"), "r") as file):
            user_data = file.readlines()
            for entry in user_data:
                data = entry.split(":")
                stored_username = data[0]
                stored_password = data[1]
                if stored_username == user_name or stored_password == user_pass:
                    print("Username already exists. Please choose another.")
                    return False

    with open("Information/users.txt", "a") as file:
        file.write(f"{user_name}:{user_pass}:staff\n")
    print("Registration successful!")
    return True

def user_login(user_name, user_pass):
    if not os.path.exists("Information/users.txt"):
        print("No registered users found. Please register first.")
        return False

    with (open("Information/users.txt", "r") as file):
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

def check_admin(user_name, user_pass):
    if  os.path.exists(resource_path("Information/users.txt")):
        with (open(resource_path("Information/users.txt"), "r") as file):
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