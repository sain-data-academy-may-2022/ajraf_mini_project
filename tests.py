from unittest.mock import Mock, patch
from courier_funcs import *
from innventory_funcs import *
from cust_items_funcs import *
from app import *


#----------------------------------CUSTOMER PY---------------------------------------------------------------


@patch('builtins.input', side_effect=["John"])
def test_get_customer_name(mock_input):
    expected = "John"
    actual = get_customer_name()
    assert expected == actual
    assert mock_input.call_count == 1

@patch('builtins.input', side_effect=[""])
def test_get_customer_name_empty(mock_input):
    expected = None
    actual = get_customer_name()
    assert expected == actual
    assert mock_input.call_count == 1

@patch('builtins.input', side_effect=["C"])
@patch("builtins.print")
def test_get_customer_phone_str(mock_print, mock_input):
    get_customer_phone()
    # Assert
    mock_print.assert_called_with("Phone number can only contain digits") # Passes
    assert mock_input.call_count == 1
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect=[""])
@patch("builtins.print")
def test_get_customer_phone_empty(mock_print, mock_input):
    get_customer_phone()
    # Assert
    mock_print.assert_called_with("This cannot be empyty") # Passes
    assert mock_input.call_count == 1
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect=["2.2"])
@patch("builtins.print")
def test_get_customer_phone_float(mock_print, mock_input):
    get_customer_phone()
    # Assert
    mock_print.assert_called_with("Phone number can only contain digits") # Passes
    assert mock_input.call_count == 1
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect=["11111111111111111111111"])
@patch("builtins.print")
def test_get_customer_phone_long20(mock_print, mock_input):
    get_customer_phone()
    # Assert
    mock_print.assert_called_with("This number is too long") # Passes
    assert mock_input.call_count == 1
    assert mock_print.call_count == 1

@patch('builtins.input', side_effect=["Aberdeen"])
def test_get_customer_address(mock_input):
    expected = "Aberdeen"
    actual = get_customer_address()
    assert expected == actual
    assert mock_input.call_count == 1

@patch('builtins.input', side_effect=[""])
@patch("builtins.print")
def test_get_customer_address_empty(mock_print,mock_input):
    get_customer_address()
    mock_print.assert_called_with("This cannot be empyty") # Passes
    assert mock_input.call_count == 1

#---------------------------Inventory-------------------------------------------------------
@patch("builtins.print")
def test_delete_book_with_DI_empty(mock_print):
    # assemble
    mock_func_to_call = Mock(return_value=None)
    delete_book(mock_func_to_call)
    mock_print.assert_called_with("Enter a valid book name") 

@patch('builtins.input', side_effect=[1])
def test_get_book_quantity(mock_input):
    expected = 1
    actual = get_book_quantity()
    assert actual == expected
    assert mock_input.call_count == 1
    
