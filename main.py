from models.users import User
from services.user_service import UserService
from database import init_db
import getpass

def main():
    init_db()
    while True:
        print("\n1. Register\n2. Login\n3. Forgot Password\n4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            email = input("Email: ")
            password = getpass.getpass("Password: ")
            user = User(email=email, password=password)
            UserService.register(user)

        elif choice == "2":
            email = input("Email: ")
            password = getpass.getpass("Password: ")
            UserService.login(email, password)

        elif choice == "3":
            email = input("Email: ")
            new_pw = getpass.getpass("New Password: ")
            UserService.update_password(email, new_pw)

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()