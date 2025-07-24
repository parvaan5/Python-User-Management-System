from auth import login, registration, show_all_users , update_password , delete_account

def MainMenu():
    while True:
        print("1.Login")
        print("2.New User")
        print("3.All Users")
        print("4.Exit")
        print("5.Update Username and Password")
        print("6.delete user")
        choice=input("Enter Your choice(1-5):")
        print(choice)
        if choice=='1':
            print(login())
        elif choice=='2':
            print(registration())
        elif choice=='3':
            print(show_all_users())
        elif choice=='4':
            print('GoodBye')
            break
        elif choice=='5':
            print(update_password())
        elif choice=='6':
            print(delete_account())
        else:
            return "Please Enter a valid choice"
    

print(MainMenu())    

