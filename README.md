# My Contacts CLI App

This application aims to showcase Object Relational Mapping. It runs on the Command Line Interface. It is built using Python and SQLite3.

## Overview

A user can create contact details that will be persisted in a database. This database is created in a local machine by SQLite3. The details can be viewed, updated and deleted as the user wishes.

**NOTE:** The contact information is purely dummy data. This is intentional.

The data is stored in two separate SQL tables that have a one-to-many relationship. A contact name can have multiple contact numbers. A contact number can only be linked to one name.

Data from both tables can be viewed in combination or separately. Data can also be edited and deleted separately.

## How to run the application

Fork and/or clone this repository so that you have your own copy of it.

Once on your machine and with the working directory open, run the following command, on your terminal, to initialize a connection with the available database file.

```
python3 lib/models/__init__.py
```

Open a SQLite3 terminal, in a separate space/terminal, by running

```
sqlite3 mycontacts.sqlite3
```

Once in this teminal, run

```
PRAGMA foreign_keys = ON;
```

The command above will help start Foreign Keys support in the database. _This is important since the two tables have a relationship with each other. By default, support for Foreign Keys is set to OFF in SQLite._

After the steps above are completed, you can launch the application by running the following command.

```
python3 lib/cli.py
```

The application is interactive and calls for user engagement.

A welcome message, an instruction and a menu will be presented. The menu is pretty straightfoward and self explanatory.

Each instruction from the menu will provide a response on the same command line inteface depending on whether data is returned from the instruction or if an error is encountered during the execution of the instruction.

It is also possible to exit the program using a simple instruction on the menu.

### FYI

The database file that is present in this repo contains some dummy data. To be able to view a sampling of the data, you can run the following commands on a SQLite3 terminal/CLI.

```
SELECT * FROM contact_names;
```

```
SELECT * FROM contact_numbers;
```

### Contribution

This application is pretty simple and you are welcome to make it your own by changing up the layout and data collected. Any additions are likely not going to be incorporated into it on my part.

### Built using

-   Python version 3.10.12.
-   SQLite3 version 3.37.2.

## Licence

MIT License

Copyright (c) [2024]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Author

Barbara Ndiba.
