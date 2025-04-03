import os

def register_user(user_name, user_pass):
    if os.path.exists("Information/users.txt"):
        with open("Information/users.txt", "r") as file:
            user_data = file.readlines()
            for entry in user_data:
                stored_user, _ = entry.strip().split(":")
                if stored_user == user_name:
                    print("Username already exists. Please choose another.")
                    return False

    with open("Information/users.txt", "a") as file:
        file.write(f"{user_name}:{user_pass}\n")
    print("Registration successful!")
    return True

def user_login(user_name, user_pass):
    if not os.path.exists("Information/users.txt"):
        print("No registered users found. Please register first.")
        return False

    with open("Information/users.txt", "r") as file:
        user_data = file.readlines()
        for entry in user_data:
            stored_user, stored_pass = entry.strip().split(":")
            if stored_user == user_name and stored_pass == user_pass:
                print("Login successful!")
                return True
    print("Invalid username or password.")