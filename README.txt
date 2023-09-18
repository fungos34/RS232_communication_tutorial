RS-232 communication tutorial on windows in Python 3.10.11:

"""
Why?

Python is the ultimate tool for automation as an easy to learn higher level coding language. 
This tutorial is meant to give some guidance for understanding the major concepts of serial communication with python.
It is tuff to go through this tutorial without any coding knowledge, but anything is called impossible until someone has done it.

RS-232 is the key for automating your production line, laboratory equipment, or CNC-machine. 
With knowledge about the communication via RS-232 you can easily coordinate and automate the boring stuff, 
collect data fully automated to even utilize modern python machine learning techniques (pyTorch, TensorFlow) 
and make most out of your data. Most of the present concepts also apply to any other network communication, 
therefore it opens many doors at once. 
By following this tutorial you will be able to follow a learning-by-doing approach, 
since it provides you with all requirements to set up a virtual device at windows, 
which is communicating over a virtual RS-232 port, even if your computer does not have this kind of port.
Therefore, feel free to play around a little bit to get familiar with automation.

I highly encourage you to use the obtained knowledge from this tutorial to 
- copy and modify the provided async/sync communication protocol to your needs for your devices.
- write your own virtual representation of an arbitrary RS-232 device by analyzing the provided virtual device 
  to work 100% remotely on your automation software while conducting real runs in your working place or to run testing runs.
- copy the python code to a Raspberry Pi which is connected to your equipment and run your devices remotely (OPC-UA).
- many, many more.

So, let's get started!
"""

Setup Environment:
1. download "32bit" 'Virtual Serial Ports Emulator (x32) 1.2.6.788'
          free download available here: https://eterlogic.com/Products.VSPE.html
          NOTE: The 64bit version is not for free, just use the 32 bit version.
          ALTERNATIVELY: Install the SetupVSPE_32_1.3.6.970.zip 
                    Consider the specific Licence conditions for this software package:
                    "License grant. "OLENA TER ETERLOGIC SOFTWARE" grants Licensee a non-exclusive and non-transferable license to reproduce, 
                    use and redistribute for any purposes the executable code version of the Product, 
                    provided any copy must contain all of the original proprietary notices."
                    You can find the full text licence within the SetupVSPE_32_1.3.6.970.zip file.
2. Emulate an RS232 "Pair" with ports 'COM14' and 'COM4' 
          > Device > Create > select 'Pair' > 'Weiter' or 'Continue' > 
                    select Virtual Serial Port 1 'COM4'; 
                    select Virtual Serial Port 2 'COM14'
                    unbox "Emulate Baudrate (optional)" if selected >
                              select 'Fertigstellen' or 'Finish'.
          You can now find two virtually connected, emulated serial ports in your system. 
          This mimics the data cable between the virtual device and your script during testing and during communication trials. 
3. Run the virtual_bkp.py file in a separate terminal window. 
          You are now able to communicate over port 'COM4' with 'COM14' as if they where real connected ports.
          The virtual device listens to COM14 and responds according to a real devices documentation.
          Debug: If your device has already ports 'COM4' or 'COM14' choose other ports. 
          You have to change the called port within your script rs232_communication.py too. 
          Also the virtual device is trying to open 'COM14', change this part of the script virtual_bkp.py too if necessary.

Problem Set:
          write within bkp_communication.py all predefined functions to pass all the tests in test_bkp_communication.py. 
          Run the pytest in your terminal with the command "python -m pytest" to get detailed information about your progress.
Extra Problem: write a function to monitor all values for voltage, current and status of the device over an arbitrary time.
Extra Problem: wrap all your functionality in a self made class.
Extra Problem: setup the communication via asynchronous communication (python module 'asyncio')
