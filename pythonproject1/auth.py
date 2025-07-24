def login():
    chance=3
    while chance>0:
        username=input("Enter username:")
        password=input("Enter password:")
        with open("users.txt","r")as file:
            for d in file:
                data=d.strip().split(",")
                print(data)
                if username==data[0] and password==data[1]:
                    return f"the username {username} is found"
        chance-=1
        print(f"no user found try again total chances left:{chance}")
    return "no user found"

# print(login())


def registration():
    name=input("Enter Username for your account:")
    password=input("Enter Password for your password")
    with open("users.txt","r") as file:
        for d in file:
            indata=d.strip().split(",")
            print(indata)
            if name==indata[0]:
                return "the username is already taken"
    with open("users.txt","a") as file:
        file.write(f"{name},{password}\n")
        file.close()
        return "new account created successfully"


# print(registration())


def show_all_users():
    print("total username:")
    with open("users.txt","r") as file:
        for f in file:
            data=f.strip().split(",")
            print(data[0])

# print(show_all_users())

def update_password():
    old_username = input("Please enter old Username: ")
    old_password = input("Please enter old Password: ")

    # Read all lines from the file
    with open("users.txt", "r") as file:
        lines = file.readlines()

    # Input new details
    new_username = input("Please enter new Username: ")
    new_password = input("Please enter new Password: ")

    # Step 1: Check if new username is already taken (by someone else)
    for line in lines:
        u, _ = line.strip().split(",")
        if u == new_username and u != old_username:
            print("❌ This username is already taken by someone else.")
            return

    # Step 2: Write back updated lines
    updated = False
    with open("users.txt", "w") as file:
        for line in lines:
            u, p = line.strip().split(",")
            if u == old_username and p == old_password:
                file.write(f"{new_username},{new_password}\n")
                updated = True
            else:
                file.write(line)

    # Step 3: Final result
    if updated:
        print(f"✅ User updated successfully from '{old_username}' to '{new_username}'.")
    else:
        print("❌ Old username and password not found or incorrect.")

# print(update_password())

def delete_account():
    username = input("🔑 Enter your username to delete: ")
    password = input("🔒 Enter your password to confirm: ")
    deleted = False

    with open("users.txt", "r") as file:
        lines = file.readlines()

    with open("users.txt", "w") as file:
        for line in lines:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                deleted = True
                continue
            file.write(line)

    if deleted:
        return f"✅ User '{username}' deleted successfully."
    else:
        return "❌ Username or password incorrect. Nothing was deleted."



# print(delete_account())





    
        
        
        
            

    
        






