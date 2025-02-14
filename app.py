import os
import socket
import subprocess
import json

# Function to list connected devices
def list_connected_devices():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Connected devices: {ip_address}")

def load_users():
    with open('users.json') as f:
        return json.load(f)

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

def start_service():
    base_directory = input("Enter the base directory (e.g., C:/Files): ")
    if not os.path.isdir(base_directory):
        print(f"Directory {base_directory} does not exist.")
        return
    # Run the Flask server in a new terminal window
    subprocess.Popen(["qterminal", "-e", "python3 server.py"])


def stop_service():
    os._exit(0)

def manage_users():
    users = load_users()
    while True:
        print("User Management")
        print("1. Add User")
        print("2. Remove User")
        print("3. List Users")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            users[username] = password
            save_users(users)
            print(f"User {username} added.")
        elif choice == '2':
            username = input("Enter username to remove: ")
            if username in users:
                del users[username]
                save_users(users)
                print(f"User {username} removed.")
            else:
                print("User not found.")
        elif choice == '3':
            print("Users:")
            for username in users:
                print(f" - {username}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    while True:
        print("Main Menu")
        print("1. Start File Hosting Service")
        print("2. Stop File Hosting Service")
        print("3. Manage Users")
        print("4. List Connected Devices")
        print("5. Exit")
        choice = input("Select Option: ")
        if choice == '1':
            start_service()
        elif choice == '2':
            stop_service()
        elif choice == '3':
            manage_users()
        elif choice == '4':
            list_connected_devices()
        elif choice == '5':
            stop_service()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
