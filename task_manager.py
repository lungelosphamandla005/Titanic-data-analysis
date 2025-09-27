# ===== Importing external modules ===========
import datetime
import sys

# ==== Login Section ====


def load_users(file_path):
    """
    Load user credentials from a file into a dictionary.
    Each line in the file should be 'username,password'.
    Returns a dict mapping usernames to passwords.
    """
    users = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ',' not in line:
                    continue  # skip invalid lines
                username, password = line.split(',', 1)
                users[username.strip().lower()] = password.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return users


def authenticate(users):
    """
    Prompt the user to enter username and password and validate.
    Continues until valid credentials are entered.
    """
    while True:
        username_input = input("Username: ").strip().lower()
        password_input = input("Password: ").strip()

        if username_input in users and users[username_input] == password_input:
            print(f"\nLogin successful. Welcome, {username_input}!\n")
            return username_input
        else:
            print("Invalid username or password. Please try again.\n")


users = load_users("user.txt")
current_user = authenticate(users)


# ==== Task Management Section ==== 

while True:
    # Present the menu to the user and make sure that the user input is converted to lower case.
    menu = input(
        '''Select one of the following options:
r  - register a user
a  - add task
va - view all tasks
vm - view my tasks
e  - exit
: '''
    ).lower()

    if menu == 'r':
        # Register a new user:

        # 1. Ensure the username is unique
        while True:
            username = input("Enter a new username: ").strip().lower()
            if not username:
                print("Username cannot be empty. Please try again.")
            elif username in users:
                print(f"Username '{username}' already exists. Please choose a different username.")
            else:
                break

        # 2. Prompt for password and confirmation
        while True:
            password = input("Enter a new password: ").strip()
            confirm_password = input("Confirm your password: ").strip()
            if not password:
                print("Password cannot be empty. Please try again.")
            elif password != confirm_password:
                print("Passwords do not match. Please try again.")
            else:
                break

        # 3. Store the new credentials
        users[username] = password
        with open("user.txt", "a") as uf:
            uf.write(f"\n{username},{password}\n")
        print(f"User '{username}' registered successfully.\n")

    elif menu == 'a':
        # Add a new task:
        print("\n=== Add New Task ===")
        assignee = input("Enter the username of the person assigned to the task: ").strip().lower()
        title    = input("Enter the title of the task: ").strip()
        description = input("Enter the description of the task: ").strip()
        due_date = input("Enter the due date of the task (YYYY-MM-DD): ").strip()
        assigned_date = datetime.date.today().isoformat()
        complete = 'No'  # Default value for completeness

        # Write the new task to the tasks file
        with open("tasks.txt", "a") as tf:
            tf.write(f"\n{assignee}, {title}, {description}, {assigned_date}, {due_date}, {complete}\n")
        print("Task added successfully.\n")

    elif menu == 'va':
        # View all tasks
        print("\n=== All Tasks ===")
        try:
            with open("tasks.txt", "r") as tf:
                for i, line in enumerate(tf, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split(',')]
                    # Display each task's details
                    print(f"\n--- Task {i} ---")
                    print(f"Username      : {parts[0]}")
                    print(f"Title         : {parts[1]}")
                    print(f"Description   : {parts[2]}")
                    print(f"Date Assigned : {parts[3]}")
                    print(f"Due Date      : {parts[4]}")
                    print(f"Complete?     : {parts[5]}")
        except FileNotFoundError:
            print("No tasks found.\n")

    elif menu == 'vm':
        # View my tasks
        print(f"\n=== Tasks for {current_user} ===")
        found = False
        try:
            with open("tasks.txt", "r") as tf:
                for i, line in enumerate(tf, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split(',')]
                    # Check if the task is assigned to the current user
                    if parts[0].lower() == current_user:
                        found = True
                        # Display the current user's task details
                        print(f"\n--- Task {i} ---")
                        print(f"Title         : {parts[1]}")
                        print(f"Description   : {parts[2]}")
                        print(f"Date Assigned : {parts[3]}")
                        print(f"Due Date      : {parts[4]}")
                        print(f"Complete?     : {parts[5]}")
        except FileNotFoundError:
            print("No tasks found.\n")

        if not found:
            print("You have no tasks assigned.\n")

    elif menu == 'e':
        # Exit the program
        print("\nGoodbye!!!")
        sys.exit(0)

    else:
        # Handle invalid menu input
        print("You have entered an invalid input. Please try again.\n")
