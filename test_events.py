import pytest
from events import AccountCreated

def test_initial_value():
    account_created = AccountCreated(1, "tito_perez@yahoo.es", "3215896743", "1020578694", "Carrera 23 #76 124")     
    assert account_created.id == 1
    assert account_created.email == "tito_perez@yahoo.es"
    assert account_created.cell_phone == "3215896743"
    assert account_created.national_id == "1020578694"
    assert account_created.address == "Carrera 23 #76 124"
 
def test_no_value():
    with pytest.raises(Exception) as e_info:
        obj = AccountCreated()   

if __name__ == '__main__':
    pytest.main()