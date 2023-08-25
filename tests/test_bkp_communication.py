import pytest
import numpy as np
import sys
sys.path.append("C:\\Users\\accou\\OneDrive\\Desktop\\RS232_communication_tutorial")

from solutions.sync_solution import set_port,get_current_command,get_status_command,get_voltage_command,set_current_command,set_output_off_command,set_output_on_command,set_voltage_command,formatting_current,formatting_voltage,convert_string_to_binary,send_command,performance_quest
import rs232_communication
import time
import serial
import timeit


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

def test_set_output_on_command():
    assert rs232_communication.set_output_on_command() == set_output_on_command()
    
def test_set_output_off_command():
    assert rs232_communication.set_output_off_command() == set_output_off_command()

def test_set_port(port = 'COM4'):
    testing_port = serial.Serial(port)
    testing_port_type = type(testing_port)
    testing_port.close()
    assert type(rs232_communication.set_port(port)) == testing_port_type

def test_send_command():
    port = set_port()
    for i in ['CURR 100.2\r','CURR?\r','VOLT 23.99\r','VOLT?\r','OUT ON\r','STAT?\r','OUT OFF\r', 'STAT?\r']:
        aimed_response = send_command(port, i.encode('ascii'))
        assert rs232_communication.send_command(port, i.encode('ascii')) == aimed_response

def count_indentation_spaces(line: str) -> int:
    spaces = 0
    for i in range(len(line)):
        if line[i] != ' ':
            break
        else:
            spaces += 1
    return int(spaces)

def determine_first_nospace_character_in_line(line: str) -> str:
    for i in range(len(line)):
        if line[i] == ' ':
            pass
        else:
            return line[i]
        
def remove_multiline_comments(text_with_potential_multiline_comments: str) -> str:
    """Removes any multiline comment within the input string (either double or single quotes)."""
    removing_start_index = None
    removing_end_index = None
    single = False
    double = False
    for i in range(len(text_with_potential_multiline_comments)):
        character = text_with_potential_multiline_comments[i]
        if single == False:
            if character == '"':
                next_character = text_with_potential_multiline_comments[i+1]
                after_next_character = text_with_potential_multiline_comments[i+2]
                if character == next_character and character == after_next_character:
                    double = True
                    if removing_start_index == None:
                        removing_start_index = i
                        continue
                    else:
                        removing_end_index = i+2
                        continue
        if double == False:
            if character == "'":
                next_character = text_with_potential_multiline_comments[i+1]
                after_next_character = text_with_potential_multiline_comments[i+2]
                if character == next_character and character == after_next_character:
                    single = True
                    if removing_start_index == None:
                        removing_start_index = i
                        continue
                    else:
                        removing_end_index = i+2
                        continue
        if removing_end_index != None and removing_start_index != None:
            multiline_comment_list = [text_with_potential_multiline_comments[k] for k in range(len(text_with_potential_multiline_comments)) if removing_start_index <= k <= removing_end_index ]
            while True:
                remove_string = ''.join(multiline_comment_list)
                print(f'The following multiline comment will be removed: {remove_string}')
                improved_text = str(text_with_potential_multiline_comments).replace(remove_string,'')
                return remove_multiline_comments(improved_text)
    print(f'No multiline comment found.')
    return text_with_potential_multiline_comments


def read_in_function_as_string(file_name: str, function_name: str):
    with open(file_name,'r') as file:
        string_list = []
        lines = file.readlines()
        line_number = 0
        starting_line = len(lines)
        for line in lines:
            line_number += 1
            first_char = determine_first_nospace_character_in_line(line)
            if first_char == '#':
                continue
            if function_name in line:
                spaces1 = count_indentation_spaces(line)
                starting_line = line_number
            if starting_line < line_number:
                spaces2 = count_indentation_spaces(line)
                if spaces2 >= spaces1 + 4:
                    string_list.append(line)
                else:
                    break
        string_modified = remove_multiline_comments(''.join(string_list))
        # return str( '"""' + string_modified + '"""' )
        return str( "'''" + string_modified + "'''" )

        
def test_performance_quest():
    # t_list_of_lists = [[1,2,3],[3,4,5],[2,3,4,5,6,7]]
    t_code = read_in_function_as_string('rs232_communication.py','def performance_quest(')
    print(t_code)
    challenge_code = read_in_function_as_string('.\solutions\sync_solution.py','def performance_quest(')
    print(challenge_code)
    t_performance = timeit.repeat(t_code, number=1000000, repeat=4)
    challenge_performance = timeit.repeat(challenge_code, number=1000000, repeat=4)
    print(f"test performance: {t_performance}, challange performance: {challenge_performance}")
    assert np.mean(t_performance) < np.mean(challenge_performance)
    assert rs232_communication.performance_quest() == performance_quest()


# run with "python -m pytest"

if __name__ == '__main__':
    test_performance_quest()