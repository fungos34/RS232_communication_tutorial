#SOLUTION FOR SYNCHRONOUS COMMUNICATION 
import serial
import timeit

def formatting_current(value: int|float):
    """Formats a float current value to the format xxx.x according to BKP device manual. Returns the formatted number as a string."""
    if value > 999.9:
        value = 999.9
    elif value < 0.1:
        value = 0.1
    value = round(float(value), 1)
    formatted_value = "{:.1f}".format(value)
    formatted_string = str(formatted_value).zfill(5)
    print(f'CURRENT INPUT: {value}, OUTPUT: {formatted_string}')
    return formatted_string

def formatting_voltage(value: int|float):
    """Formats a float voltage value to the format xx.xx according to BKP device manual. Returns the formatted number as a string."""
    if value > 30.0:
        value = 30.0
    elif value < 0.1:
        value = 0.1
    value = round(float(value), 1)
    formatted_value = "{:.2f}".format(value)
    formatted_string = str(formatted_value).zfill(5)
    print(f'VOLTAGE INPUT: {value}, OUTPUT: {formatted_string}')
    return formatted_string

def convert_string_to_binary(input_string):
    """Converts a string to its ASCII binary format. Returns the binary string."""
    output_bin = str(input_string).encode('ascii')
    print(f'INPUT STRING: {input_string}, OUTPUT BINARY: {output_bin}')
    return output_bin




def set_current_command(current):
    """Takes an input current as a float or integer. Returns a valid binary command for BKP to set the current."""
    formatted_current = formatting_current(current)
    command = convert_string_to_binary(f'CURR {formatted_current}\r')
    print(f'CURRENT INPUT: {current}, COMMAND OUTPUT: {command}')
    return command


def get_current_command():
    """Returns a valid binary command for BKP to query the current."""
    command = convert_string_to_binary('CURR?\r')
    print(f'COMMAND OUTPUT: {command}')
    return command

def set_voltage_command(voltage):
    """Takes an input voltage as a float or integer. Returns a valid binary command for BKP to set the voltage."""
    formatted_voltage = formatting_voltage(voltage)
    command = convert_string_to_binary(f'VOLT {formatted_voltage}\r')
    print(f'VOLTAGE INPUT: {voltage} COMMAND OUTPUT: {command}')
    return command


def get_voltage_command():
    """Returns a valid binary command for BKP to query the voltage."""
    command = convert_string_to_binary('VOLT?\r')
    print(f'COMMAND OUTPUT: {command}')
    return command


def get_status_command():
    """Returns a valid binary command for BKP to query the status."""
    command = convert_string_to_binary('STAT?\r')
    print(f'COMMAND OUTPUT: {command}')
    return command


def set_output_on_command():
    """Returns a valid binary command for BKP to set the ouput to ON."""
    command = convert_string_to_binary('OUT ON\r')
    print(f'COMMAND OUTPUT: {command}')
    return command


def set_output_off_command():
    """Returns a valid binary command for BKP to set the ouput to OFF."""
    command = convert_string_to_binary('OUT OFF\r')
    print(f'COMMAND OUTPUT: {command}')
    return command


def set_port(port_name = 'COM4'):
    """Open a serial port 'COM4'. Takes a port name as string. Returns the port object."""
    port = serial.Serial(port_name)
    print(f'PORT {port_name} INITIALISED SUCCESSFULLY\n')
    return port

def send_command(port: serial.Serial, command):
    """Sends command via RS232 to the BKP. 
    Takes a port and a valid binary command as inputs. 
    Returns the device response without any leading or tailing communication characters."""
    print(f'SENDING COMMAND TO {port.name} >>> {command}')
    port.write(command)
    response_raw =  port.read_until(b'\x11')
    response = response_raw.decode('ascii').replace('\x11','').replace('\x13','').replace('\r','')
    print(f'RECEIVING FROM {port.name} <<< "{response}" (RAW: {response_raw})\n')
    return response    

def performance_quest(port,valid_command_1,valid_command_2,valid_command_3):
    '''Improve the performance of this function to pass the pytest.'''
    response_1 = send_command(port,valid_command_1)
    response_2 = send_command(port,valid_command_2)
    response_3 = send_command(port,valid_command_3)
    return [response_1,response_2,response_3]

if __name__ == '__main__':
    pass
