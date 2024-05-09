from helpers import (
    exit_app,
    create_contact_name
)

def main():
    while True:
        menu()
        user_choice = input('> ')

        if user_choice == '0':
            exit_app()
        elif user_choice == '1':
            create_contact_name()
        else:
            print('Invalid option.')

def menu():
    print('Welcome to My Contacts App.\nPlease select a valid option:')
    print('0. Exit the app.')
    print('1. Create a new contact name.')

#Run the application only if this module is run
if __name__ == '__main__':
    main()