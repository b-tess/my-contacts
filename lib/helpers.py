# import lib.models.contact_names
# from lib.models.contact_names import ContactName
import models.contact_names
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
        contact_name = models.contact_names.ContactName.create(first_name, last_name)
        print(f'Contact name created: {contact_name}')
    except Exception as error:
        print('Contact name not created: ', error)

def update_contact_name():
    pass

def view_all_contact_names():
    pass

def find_contact_name_by_id():
    pass

def find_contact_name_by_name():
    pass

def view_one_contact_name_and_number():
    pass

def view_all_contact_names_and_numbers():
    pass

def delete_contact_name():
    pass