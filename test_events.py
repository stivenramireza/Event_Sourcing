import pytest
from events import AccountCreated, AccountVerified, UserEmailChanged


def test_initial_value_AccountCreated():
    account_created = AccountCreated(1, "tito_perez@yahoo.es", "3215896743", "1020578694", "Carrera 23 #76 124")     
    assert account_created.id == 1
    assert account_created.email == "tito_perez@yahoo.es"
    assert account_created.cell_phone == "3215896743"
    assert account_created.national_id == "1020578694"
    assert account_created.address == "Carrera 23 #76 124"
 
def test_no_value_AccountCreated():
    with pytest.raises(Exception) as e_info:
        obj = AccountCreated()

def test_initial_value_AccountVerified():
    account_verified = AccountVerified(1)
    assert account_verified.account_id == 1
 
def test_no_value_AccountVerified():
    with pytest.raises(Exception) as e_info:
        obj = AccountVerified()

def test_initial_value_UserEmailChanged():
    user_email_changed = UserEmailChanged(1, "tito_perez@gmail.com")
    assert user_email_changed.account_id == 1
    assert user_email_changed.new_email == "tito_perez@gmail.com"
 
def test_no_value_UserEmailChanged():
    with pytest.raises(Exception) as e_info:
        obj = UserEmailChanged()

if __name__ == '__main__':
    pytest.main()