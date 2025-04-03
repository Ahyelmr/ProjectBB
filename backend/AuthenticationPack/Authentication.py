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

"""
def dashboard():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        user_choice = input("Choose an option: ")
        if user_choice == "1":
            user_name = input("Enter a username: ")
            user_pass = input("Enter a password: ")
            register_user(user_name, user_pass)
        elif user_choice == "2":
            user_name = input("Enter your username: ")
            user_pass = input("Enter your password: ")
            user_login(user_name, user_pass)
        elif user_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    dashboard()

"""