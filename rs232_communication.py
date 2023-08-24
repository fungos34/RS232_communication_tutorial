#FRAMEWORK WITH PREDEFINED FUNCTIONS FOR SYNCHRONOUS COMMUNICATION BKP.
import serial

def formatting_current(current):
    """Formats a float current value to the format xxx.x according to BKP device manual. Returns the formatted number as a string."""
    pass

def formatting_voltage(voltage):
    """Formats a float voltage value to the format xx.xx according to BKP device manual. Returns the formatted number as a string."""
    pass

def convert_string_to_binary(string):
    """Converts a string to its ASCII binary format. Returns the binary string."""
    pass

def set_current_command(current):
    """Takes an input current as a float or integer. Returns a valid binary command for BKP to set the current."""
    pass

def get_current_command():
    """Returns a valid binary command for BKP to query the current."""
    pass

def set_voltage_command(voltage):
    """Takes an input voltage as a float or integer. Returns a valid binary command for BKP to set the voltage."""
    pass

def get_voltage_command():
    """Returns a valid binary command for BKP to query the voltage."""
    pass

def get_status_command():
    """Returns a valid binary command for BKP to query the status."""
    pass

def set_output_on_command():
    """Returns a valid binary command for BKP to set the ouput to ON."""
    pass

def set_output_off_command():
    """Returns a valid binary command for BKP to set the ouput to OFF."""
    pass

def set_port(port_name = 'COM4'):
    """
    Open a serial port like 'COM4'. 
    :param port_name: port name as string. 
    :returns: the port object.
    """
    pass

def send_command(port,command):
    """Sends command via RS232 to the BKP. 
    Takes a port and a valid binary command as inputs. 
    Returns the device response without any leading or tailing communication characters."""
    pass


if __name__ == '__main__':
    pass
