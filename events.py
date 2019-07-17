from uuid import uuid4

class AccountCreated():

    def __init__(self, id, email, cell_phone, national_id, address):
        self.id = id
        self.email = email
        self.cell_phone = cell_phone
        self.national_id = national_id
        self.address = address

class AccountVerified():

    def __init__(self, account_id):
        self.account_id = account_id

class UserEmailChanged():

    def __init__(self, account_id, new_email):
        self.account_id = account_id
        self.new_email = new_email
    
class UserMoved():
    
    def __init__(self, account_id, new_address):
        self.account_id = account_id
        self.new_address = new_address

class UserChangedCellPhone():

    def __init__(self, account_id, new_cell_phone):
        self.account_id = account_id
        self.new_cell_phone = new_cell_phone

class AccountDeleted():

    def __init__(self, account_id):
        self.account_id = account_id

# Event Store
events = [
    AccountCreated(
        1, 
        "tito_perez@yahoo.es", 
        "3215896743",
        "1020578694",
        "Carrera 23 #76 124"
    ),
    AccountVerified(1),
    AccountCreated(
        2, 
        "amparo_grisales@gmail.com", 
        "3006014825",
        "1",
        "Carrera 1 #5 426B"
    ),
    AccountCreated(
        3, 
        "maelo_ruiz@gmail.com", 
        "3014567842",
        "7045896",
        "Carrera 33 #10 784"
    ),
    AccountVerified(2),
    UserEmailChanged(
        1,
        "tito_perez@gmail.com"
    ),
    UserMoved(
        2,
        "Tumba"
    )
]

# DB

users = {}

class User():

    def __init__(self, id, email, cell_phone, national_id, address, verified):
        self.id = id
        self.email = email
        self.cell_phone = cell_phone
        self.national_id = national_id
        self.address = address
        self.verified = verified

    def __repr__(self):
        return "ID: {} -- Email: {} -- Cell Phone: {} -- National ID: {} -- Address: {} -- Verified: {}".format(
            self.id,
            self.email,
            self.cell_phone,
            self.national_id,
            self.address,
            self.verified
        )

for event in events:

    if type(event) == AccountCreated:
            users[event.id] = User(
                event.id,
                event.email,
                event.cell_phone,
                event.national_id,
                event.address,
                False
            )  

    if type(event) == AccountVerified:
        account = users[event.account_id]
        account.verified = True

    if type(event) == UserEmailChanged:
        account = users[event.account_id]
        account.email = event.new_email
    
    if type(event) == UserMoved:
        account = users[event.account_id]
        account.address = event.new_address
    
    if type(event) == UserChangedCellPhone:
        account = users[event.account_id]
        account.cell_phone = event.cell_phone

    if type(event) == AccountDeleted:
        del users[event.account_id]

#[print (x) for x in users.values()]