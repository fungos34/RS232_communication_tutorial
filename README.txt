RS-232 communication tutorial on windows. 

1. download "32bit" 'Virtual Serial Ports Emulator (x32) 1.2.6.788'
          free download available here: https://eterlogic.com/Products.VSPE.html
          NOTE: The 64bit version is not for free
          ALTERNATIVELY: Install the SetupVSPE_32_1.3.6.970.zip 
2. Emulate an RS232 "Pair" with ports 'COM14' and 'COM4' 
          > Device > Create > select 'Pair' > 'Weiter' or 'Continue' > 
                    select Virtual Serial Port 1 'COM4'; 
                    select Virtual Serial Port 2 'COM14'
                    unbox "Emulate Baudrate (optional)" if selected >
                              select 'Fertigstellen' or 'Finish'.
          You can now find two virtually connected, emulated serial ports in your system. 
          This mimics the data cable between the virtual device and your script during testing. 
3. Run the virtual_bkp.py file in a separate terminal window. 
          You are now able to communicate over port 'COM4' and 'COM14' as if they where real connected ports.
          Debug: If your device has already ports 'COM4' or 'COM14' choose other ports. 
          You have to change the called port within your script rs232_communication.py too. 
          Also the virtual device is trying to open 'COM14', change this part of the script virtual_bkp.py too if necessary.
TODO:
write within bkp_communication.py all predefined functions to pass all the tests in test_bkp_communication.py. 
(Run the tests with the command "python -m pytest" in your terminal)
Extra: write a functino to monitor all values for voltage, current and status of the device over an arbitrary time.
Extra: wrap all your functionality in a self made class.
Extra: setup the communication via asynchronous communication (python module 'asyncio')
