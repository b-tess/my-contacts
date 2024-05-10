from helpers import (
    exit_app,
    create_contact_name,
    update_contact_name,
    view_all_contact_names,
    find_contact_name_by_id,
    find_contact_name_by_name,
    view_one_contact_name_and_number,
    view_all_contact_names_and_numbers,
    delete_contact_name
)

def main():
    while True:
        menu()
        user_choice = input('> ')

        if user_choice == '0':
            exit_app()
        elif user_choice == '1':
            create_contact_name()
        elif user_choice == '2':
            update_contact_name()
        elif user_choice == '3':
            view_all_contact_names()
        elif user_choice == '4':
            find_contact_name_by_id()
        elif user_choice == '5':
            find_contact_name_by_name()
        elif user_choice == '6':
            view_one_contact_name_and_number()
        elif user_choice == '7':
            view_all_contact_names_and_numbers()
        elif user_choice == '8':
            delete_contact_name()
        else:
            print('Invalid option.')

def menu():
    print('\nWelcome to My Contacts App.\nPlease select a valid option:')
    print('0. Exit the app.')
    print('1. Create a new contact name.')
    print('2. Update a contact name.')
    print('3. View all contact names.')
    print('4. Find a contact name by ID.')
    print('5. Find a contact name by name.')
    print('6. View one contact name and its number(s).')
    print('7. View all your contact names and numbers.')
    print('8. Delete one contact name\'s data.')

#Run the application only if this module is run
if __name__ == '__main__':
    main()