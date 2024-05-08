from __init__ import CONN, CURSOR
from contact_names import ContactName

class ContactNumber:
    all_contact_numbers = {}

    def __init__(self, number, contact_name_id, id=None):
        self.id = id
        self.number = number
        self.contact_name_id = contact_name_id
        #Contact_name_id is the foreign key referencing the contact names table
        #This is a one-to-many relationship & the number holds the relationship as the many

    def __repr__(self):
        return f'Contact {self.id}: {self.number}, {self.contact_name_id}.'
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if isinstance(number, str) and len(number) == 5 and number.isnumeric():
            # print(f'number length {len(number)}.')
            self._number = number
        else:
            # print('number setter called before error.')
            raise ValueError('Phone number should be numeric and 5 digits long.')
        
    @property
    def contact_name_id(self):
        return self._contact_name_id
    
    @contact_name_id.setter
    def contact_name_id(self, contact_name_id):
        if isinstance(contact_name_id, int) and ContactName.find_by_id(contact_name_id):
            self._contact_name_id = contact_name_id
        else:
            raise ValueError('Contact name id should be a valid id value.')
    
    def save(self):
        '''Add an object's data into a row in the contact numbers table.'''
        sql = '''
            INSERT INTO contact_numbers (number, contact_name_id)
            VALUES (?, ?);
        '''

        CURSOR.execute(sql, (self.number, self.contact_name_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_contact_numbers[self.id] = self

    def update(self):
        '''Update the contact number data in the table.'''
        sql = '''
            UPDATE contact_numbers
            SET number = ?, contact_name_id = ?
            WHERE id = ?;
        '''

        CURSOR.execute(sql, (self.number, self.contact_name_id, self.id))
        CONN.commit()

        updated_number = self.find_by_id(self.id)
        return updated_number

    def delete(self):
        '''Delete a row from the contact numbers table'''
        sql = '''
            DELETE FROM contact_numbers
            WHERE id = ?;
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all_contact_numbers[self.id]
        self.id = None

        return 'Number deleted.'
    
    @classmethod
    def create_table(cls):
        '''Create the contact numbers table.'''
        sql = '''
            CREATE TABLE contact_numbers (
                id INTEGER PRIMARY KEY,
                number VARCHAR(5),
                contact_name_id INTEGER,
                FOREIGN KEY (contact_name_id) REFERENCES contact_names
            );
        '''

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, number, contact_name_id):
        contact_number = cls(number, contact_name_id)
        contact_number.save()
        return contact_number
    
    @classmethod
    def instance_from_db(cls, row):
        contact_number = cls.all_contact_numbers.get(row[0])

        if contact_number:
            contact_number.number = row[1]
            contact_number.contact_name_id = row[2]
        else:
            contact_number = cls(row[1], row[2])
            contact_number.id = row[0]
            cls.all_contact_numbers[contact_number.id] = contact_number

        return contact_number
    
    @classmethod
    def get_all_numbers(cls):
        '''Get all the rows in the contact numbers table.'''
        sql = '''
            SELECT * FROM contact_numbers;
        '''

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        '''Get a row from the contact numbers table using it's id.'''
        sql = '''
            SELECT * FROM contact_numbers
            WHERE id = ?;
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def drop_table(cls):
        '''Delete the contact numbers table.'''
        sql = '''
            DROP TABLE contact_numbers;
        '''

        CURSOR.execute(sql)
        CONN.commit()

# ContactNumber.create_table()
# print(ContactNumber.find_by_id(1))
# cont2 = ContactNumber.create('02345', 3)
# ContactNumber.create('02345', 3)
# print(cont2.delete())
# cont2.number = '23478'
# print(cont2.number)
# print(cont2.update())
# print(ContactNumber.get_all_numbers())