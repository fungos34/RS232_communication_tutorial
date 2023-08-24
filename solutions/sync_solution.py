#SOLUTION FOR SYNCHRONOUS COMMUNICATION 
import serial
from loguru import logger

def set_port(port_name = 'COM4'):
    """Open a serial port 'COM4'. Takes a port name as string. Returns the port object."""
    port = serial.Serial(port_name)
    logger.info(f'PORT {port_name} INITIALISED SUCCESSFULLY\n')
    return port

def formatting_current(value: int|float):
    """Formats a float current value to the format xxx.x according to BKP device manual. Returns the formatted number as a string."""
    if value > 999.9:
        value = 999.9
    elif value < 0.1:
        value = 0.1
    value = round(float(value), 1)
    formatted_value = "{:.1f}".format(value)
    formatted_string = str(formatted_value).zfill(5)
    logger.info(f'CURRENT INPUT: {value}, OUTPUT: {formatted_string}')
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
    logger.info(f'VOLTAGE INPUT: {value}, OUTPUT: {formatted_string}')
    return formatted_string

def convert_string_to_binary(input_string):
    """Converts a string to its ASCII binary format. Returns the binary string."""
    output_bin = str(input_string).encode('ascii')
    logger.info(f'INPUT STRING: {input_string}, OUTPUT BINARY: {output_bin}')
    return output_bin




def set_current_command(current):
    """Takes an input current as a float or integer. Returns a valid binary command for BKP to set the current."""
    formatted_current = formatting_current(current)
    command = convert_string_to_binary(f'CURR {formatted_current}\r')
    logger.info(f'CURRENT INPUT: {current}, COMMAND OUTPUT: {command}')
    return command


def get_current_command():
    """Returns a valid binary command for BKP to query the current."""
    command = convert_string_to_binary('CURR?\r')
    logger.info(f'COMMAND OUTPUT: {command}')
    return command

def set_voltage_command(voltage):
    """Takes an input voltage as a float or integer. Returns a valid binary command for BKP to set the voltage."""
    formatted_voltage = formatting_voltage(voltage)
    command = convert_string_to_binary(f'VOLT {formatted_voltage}\r')
    logger.info(f'VOLTAGE INPUT: {voltage} COMMAND OUTPUT: {command}')
    return command


def get_voltage_command():
    """Returns a valid binary command for BKP to query the voltage."""
    command = convert_string_to_binary('VOLT?\r')
    logger.info(f'COMMAND OUTPUT: {command}')
    return command


def get_status_command():
    """Returns a valid binary command for BKP to query the status."""
    command = convert_string_to_binary('STAT?\r')
    logger.info(f'COMMAND OUTPUT: {command}')
    return command


def set_output_on_command():
    """Returns a valid binary command for BKP to set the ouput to ON."""
    command = convert_string_to_binary('OUT ON\r')
    logger.info(f'COMMAND OUTPUT: {command}')
    return command


def set_output_off_command():
    """Returns a valid binary command for BKP to set the ouput to OFF."""
    command = convert_string_to_binary('OUT OFF\r')
    logger.info(f'COMMAND OUTPUT: {command}')
    return command



def send_command(port: serial.Serial, command):
    """Sends command via RS232 to the BKP. 
    Takes a port and a valid binary command as inputs. 
    Returns the device response without any leading or tailing communication characters."""
    logger.info(f'SENDING COMMAND TO {port.name} >>> {command}')
    port.write(command)#'CURR?'.encode('ascii'))#'STAT?'.encode('ascii'))
    response_raw = bytearray()
    while True:
        response_byte = port.read(1)
        if response_byte == b'\x13':
            response_raw.extend(response_byte)
            while True:
                response_byte = port.read(1)
                response_raw.extend(response_byte)
                if response_byte == b'\x11':
                    break
            break
    # formatting response.
    stripped_response = response_raw.replace(b'\r',b'')
    stripped_response = stripped_response.replace(b'\x13',b'')
    stripped_response = stripped_response.replace(b'\x11',b'')
    response = stripped_response.decode('ascii')

    logger.info(f'RECEIVING FROM {port.name} <<< "{response}" (RAW: {response_raw})\n')
    return response


if __name__ == '__main__':
    port = set_port()
    send_command(port,set_current_command(234234.7876))
    send_command(port,set_voltage_command(4.675))
    send_command(port,get_current_command())
    send_command(port,get_voltage_command())
    send_command(port,get_status_command())
    send_command(port,set_output_on_command())
    send_command(port,get_status_command())
