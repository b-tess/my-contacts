from __init__ import CONN, CURSOR

class ContactName:
    all_contact_names = {}

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Contact {self.id}: {self.first_name.capitalize()} {self.last_name.capitalize()}.'
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name):
            self._first_name = first_name.lower()
        else:
            raise ValueError('The first name must be a string at least one character long.')
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name):
            self._last_name = last_name.lower()
        else:
            raise ValueError('The last name must be a string at least one character long.')
    
    def save(self):
        '''Add an object's data into a row in the contact names table.'''
        sql = '''
            INSERT INTO contact_names (first_name, last_name)
            VALUES (?, ?);
        '''

        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_contact_names[self.id] = self

    def update(self):
        '''Update a row in the contact names table when an object's data is changed.'''
        sql = '''
            UPDATE contact_names
            SET first_name = ?, last_name = ?
            WHERE id = ?;
        '''

        CURSOR.execute(sql, (self.first_name, self.last_name, self.id))
        CONN.commit()

    def delete(self):
        '''Delete an object's data from a row in the contact names table. Remove the object from the local dict cache.'''
        sql = '''
            DELETE FROM contact_names
            WHERE id = ?;
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all_contact_names[self.id]
        self.id = None
    
    @classmethod
    def create_table(cls):
        '''Create the contact names table.'''
        sql = '''
            CREATE TABLE contact_names (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                CONSTRAINT UC_contactname UNIQUE (first_name, last_name)
            );
        '''

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, first_name, last_name):
        '''Create an instance of the contact names class. Add the instance data to a row in the contact names table. Return the instance once successfully saved to the table.'''
        contact_name = cls(first_name, last_name)
        contact_name.save()
        return contact_name
    
    @classmethod
    def instance_from_db(cls, row):
        contact_name = cls.all_contact_names.get(row[0])

        if contact_name:
            contact_name.first_name = row[1]
            contact_name.last_name = row[2]
        else:
            contact_name = cls(row[1], row[2])
            contact_name.id = row[0]
            cls.all_contact_names[contact_name.id] = contact_name

        return contact_name
    
    @classmethod
    def get_all(cls):
        '''Get all rows of contact names from the contact names table. Then change the rows into Python objects to display to the user.'''
        sql = '''
            SELECT * FROM contact_names;
        '''

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        '''Get a contact name row from the contact names table using an id. Display this row to the user.'''
        sql = '''
            SELECT * FROM contact_names
            WHERE id = ?;
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        '''Find a row/rows in the contact names table casing not withstanding when a user searches for a name or part of a name in the table.'''
        lowercase_name = f'%{name.lower()}%'
        # print(lowercase_name)
        sql = '''
            SELECT * FROM contact_names
            WHERE first_name LIKE ? OR last_name LIKE ?;
        '''

        rows = CURSOR.execute(sql, (lowercase_name, lowercase_name)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def drop_table(cls):
        '''Delete the contact names table from the database.'''
        sql = '''
            DROP TABLE contact_names;
        '''

        CURSOR.execute(sql)
        CONN.commit()

# ContactName.create_table()
# ContactName.create('Jane', 'Doe')
# print(ContactName.find_by_id(1))
# print(ContactName.find_by_name('J'))
# print(ContactName.get_all())
# print('hello')