import pytest
from modules.common.database import Database
import sqlite3


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'biscuite', 'sweet', 30)
    water_qnt = db.select_product_qnt_by_id(4)    

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'data', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)    

    assert len(qnt) == 0



@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_check_user_by_id():
    db = Database()
    user = db.get_user_info_by_id(1)

    print (user)


@pytest.mark.database
def test_user_insert():
    db = Database()
    db.insert_user(99, 'John', 'Peremogi 66', 'Kyiv', 3115, 'Ukraine')
    user = db.get_user_info_by_id(99)

    print ("id 99 =", user)

#if one element in the column is not filled in
@pytest.mark.database
def test_user_info():
    db = Database()
    db.insert_user(100, 'John', '', 'Kyiv', 3115, 'Ukraine')
    user_info = db.get_user_info_by_id(100)

    for record in user_info:
        address = record[1]
    assert len(address) == 0
    
     
@pytest.mark.database
def test_customer_delete():
    db = Database()
    db.insert_user(999, 'Johny', 'Peremogi 100', 'Kyiv', 3115, 'Ukraine')
    db.delete_user_by_id(999)
    user = db.get_user_address_by_name('Johny')    

    assert len(user) == 0

@pytest.mark.database
def test_insert_user_with_invalid_data_type():
    db = Database()
    db.insert_user(500, "Noname", "123 Street", "Noname City", 3115, 'Field')
    customer_id = db.customer_id
    db.select_user(customer_id)
    if type(customer_id) is int:
        print("true")
    else:
        print("false")
