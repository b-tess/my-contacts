from models.contact_names import ContactName
from models.contact_numbers import ContactNumber


#This file contains only function definitions. The functions are not being called here.

def exit_app():
    print('My Contacts App Closed.')
    exit()

#Contact name functions
def create_contact_name():
    first_name = input('First name: ')
    last_name = input('Last name: ')

    try:
        contact_name = ContactName.create(first_name, last_name)
        print(f'Contact name created: {contact_name}')
    except Exception as error:
        if type(error).__name__ == 'IntegrityError':
            print(f'Contact name not created: A contact, {first_name} {last_name}, already exists.')
        else:
            print(f'Contact name not created: {error}')

def update_contact_name():
    id = input('Enter the contact name\'s ID: ')
    if contact_name := ContactName.find_by_id(id):
        try:
            #Allow a user to change only one of the names instead of rewriting
            #a name they don't want to change.
            if first_name := input('Enter the new first name: '):
                contact_name.first_name = first_name
            else:
                contact_name.first_name = contact_name.first_name
                
            if last_name := input('Enter the new last name: '):
                contact_name.last_name = last_name
            else:
                contact_name.last_name = contact_name.last_name

            contact_name.update()
            print(f'Contact name updated to: {contact_name}')
        except Exception:
            print(f'*****Contact name not updated: A contact, {first_name} {last_name}, already exists.*****')
    else:
        print(f'*****Contact with id {id} not found.*****')

def view_all_contact_names():
    if contact_names := ContactName.get_all():
        for name in contact_names:
            print(f'{name}')
    else:
        print('No contact names to show.')

def find_contact_name_by_id():
    id = input('Enter the contact name\'s ID: ')
    if contact_name := ContactName.find_by_id(id):
        print(contact_name)
    else:
        print('*****Contact name ID not found.*****')

def find_contact_name_by_name():
    if name := input('Enter a name to search for: '):
        if contact_names := ContactName.find_by_name(name):
            for contact_name in contact_names:
                print(contact_name)
        else:
            print('*****No contact name found.*****')
    else:
        print('*****Please enter a name to search for.*****')

def view_one_contact_name_and_number():
    id = input('Enter a contact name ID: ')
    if contact_name := ContactName.find_by_id(id):
        if contact_info := contact_name.get_number():
            for info in contact_info:
                print(f'{info}')
        else:
            print('*****No number for the provided contact in record.*****')
    else:
        print('*****Contact ID not found.*****')

def view_all_contact_names_and_numbers():
    if contact_info := ContactName.get_names_numbers():
        for info in contact_info:
            print(f'{info}')
    else:
        print('No contact names AND numbers to show.')

def delete_contact_name():
    id = input('Enter contact name ID: ')
    confirm = input('Are you sure you would like to delete this contact? y/n: ')
    if confirm == 'y' or confirm == 'Y':
        contact_name = ContactName.find_by_id(id)
        try:
            contact_name.delete()
            print('Contact data deleted successfully.')
        except Exception as error:
            print(f'Contact not deleted: {error}')
    else:
        print('Contact data not deleted.')

#Contact numbers functions
def create_contact_number():
    number = input('Enter a contact number: ')
    contact_name_id = input('Enter a contact name id: ')

    try:
        contact_number = ContactNumber.create(number, contact_name_id)
        print(f'Contact number created. {contact_number}')
    except Exception as error:
        print(f'*****Contact number not added: {error}*****')

def update_contact_number():
    id = input('Enter the contact number ID: ')
    if contact_number := ContactNumber.find_by_id(id):
        try:
            if new_number := input('Enter the new number: '):
                contact_number.number = new_number
            else:
                contact_number.number = contact_number.number

            if new_contact_name_id := input('Enter the new contact name ID: '):
                contact_number.contact_name_id = new_contact_name_id
            else:
                contact_number.contact_name_id = contact_number.contact_name_id

            contact_number.update()
            print(f'Contact number successfully updated: {contact_number}')
        except Exception as error:
            print(f'*****Contact number not updated: {error}')
    else:
        print('*****Contact number not updated: The contact number ID is not valid.*****')

def view_all_contact_numbers():
    if contact_numbers := ContactNumber.get_all_numbers():
        for contact_number in contact_numbers:
            print(contact_number)
    else:
        print('*****No contact numbers to show.*****') 

def find_a_number_by_id():
    id = input('Enter a contact number ID: ')
    if contact_number := ContactNumber.find_by_id(id):
        print(contact_number)
    else:
        print('*****Contact number ID not found.*****')

def delete_contact_number():
    id = input('Enter the contact number ID: ')
    confirm = input('Are you sure you would like to delete this contact number? y/n: ')
    if confirm == 'y' or confirm == 'Y':
        if contact_name := ContactNumber.find_by_id(id):
            contact_name.delete()
            print('Contact number deleted.')
        else:
            print('*****Contact number ID not found.*****')
    else:
        print('Contact number not deleted.')