import pytest
import numpy as np
from solutions.sync_solution import set_port,get_current_command,get_status_command,get_voltage_command,set_current_command,set_output_off_command,set_output_on_command,set_voltage_command,formatting_current,formatting_voltage,convert_string_to_binary,send_command
import rs232_communication
import time

def test_formatting_current():
    for i in [-12,1234.5678,123.4,0.0,100]:
        assert rs232_communication.formatting_current(i) == formatting_current(i)

def test_formatting_voltage():
    for i in [-1,32,29,43.23,34343,3.3453]:
        assert rs232_communication.formatting_voltage(i) == formatting_voltage(i)

def test_convert_string_to_binary():
    for i in ['abc','\r','VOLT?\r', '\x13','hello world!']:
        assert rs232_communication.convert_string_to_binary(i) == convert_string_to_binary(i)

def test_set_current_command():
    for i in np.arange(0.5,999.9,50).reshape([len(np.arange(0.5,999.9,50)),1]):
        assert  rs232_communication.set_current_command(i) == set_current_command(i)

def test_get_current_command():
    assert  rs232_communication.get_current_command() == get_current_command()
    
def test_set_voltage_command():
    for i in np.arange(0.01,30.0,5).reshape([len(np.arange(0.01,30.0,5)),1]):
        assert  rs232_communication.set_voltage_command(i) == set_voltage_command(i)

def test_get_voltage_command():
    assert  rs232_communication.get_voltage_command() == get_voltage_command()


def test_get_status_command():
    assert rs232_communication.get_status_command() == get_status_command()

def test_set_output_off_command():
    assert rs232_communication.set_output_off_command() == set_output_off_command()

def test_set_output_on_command():
    assert rs232_communication.set_output_on_command() == set_output_on_command()


def test_send_command():
    port = set_port()
    for i in ['CURR 100.2\r','CURR?\r','VOLT 23.99\r','VOLT?\r','OUT ON\r','STAT?\r','OUT OFF\r', 'STAT?\r']:
        aimed_response = send_command(port, i.encode('ascii'))
        time.sleep(0.1)
        assert rs232_communication.send_command(port, i.encode('ascii')) == aimed_response


# run with "python -m pytest"
