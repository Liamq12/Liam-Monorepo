"""
BSPD Validation

This program is used to validate the Mines Formula SAE's 2023 BSPD.
Requires:
1 Agilent 34401a Multimeter
1 HP6624A or similar 4 channel PSU
BSPD board

Connect multimeter to GND and output signal
PSU
Channel 1: VDD-GND
Channel 2: Throttle1-GND
Channel 3: Brake1-GND
Channel 4: KeyIn-GND


Author: Liam Homburger
lvhomburger@mines.edu
"""

# Must install NI VISA drivers or Keysight Connection Expert. Instruments must be connected over an GPIB bus, otherwise change addresses to IP addresses
import os, time
import pyvisa

def start():
    # Power on board
    psu.write("INST:NSEL 1") # Select channel 1
    psu.write("VOLT 12") # Set voltage to 12V
    psu.write("CURR 1") # Set current to 1A

    # Set key signal to high
    psu.write("INST:NSEL 4") # Select channel 4
    psu.write("VOLT 12") # Set key signal high
    psu.write("CURR 0.05") # Set current limit to 0.05A

    # Set throttle position to 0% for hall effect sensor
    psu.write("INST:NSEL 2") # Select channel 2
    psu.write("VOLT 0.5") # Set "position" to 0%
    psu.write("CURR 0.05") # Set current limit to 0.05A

    # set brakes to 0%
    psu.write("INST:NSEL 3") # Select channel 3
    psu.write("VOLT 0.5") # Set "position" to 0%
    psu.write("CURR 0.05") # Set current limit to 0.05A

def key_reset():
    # Set key signal to low
    psu.write("INST:NSEL 4") # Select channel 4
    psu.write("VOLT 0") # Set key signal high
    psu.write("CURR 0.05") # Set current limit to 0.05A

    time.sleep(5)

    # Set key signal to high
    psu.write("INST:NSEL 4") # Select channel 4
    psu.write("VOLT 12") # Set key signal high
    psu.write("CURR 0.05") # Set current limit to 0.05A


rm = pyvisa.ResourceManager()
rm.list_resources()

try:
    dmm = rm.open_resource('GPIB0::6::INSTR') # Connect to Ag34401A Digital Multimeter
    psu = rm.open_resource('GPIB0::5::INSTR') # Connect to HP6624 PSU
except Exception as e:
    print(str(e))

print("Instruments Initialized")

ramp = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5] # 2.5% increments

cycles = 5

for i in range(cycles):
    print("Cycle " + i + " starting.")
    start()
    time.sleep(1)

    psu.write("INST:SEL 3") # Select channel 3
    psu.write("VOLT 0.5") # Set brake "position" to 0%
    # First without faulty state, then with fault
    for fault in range(2):
        # Increment throttle by 2.5% until fault
        for j in ramp:
            psu.write("INST:NSEL 2") # Select channel 2
            psu.write("VOLT " + j) # Set throttle "position" to 5%
            time.sleep(0.8)
            if(dmm.query("MEAS:IMM:DCV?") < 1):
                print("SHUTDOWN DUE TO THROTTLE AT " + ((j-0.5)/4)*100 + "%")
                psu.write("INST:NSEL 3") # Select channel 3
                print("Brake at " + psu.query("MEAS:VOLT?"))
        
        key_reset()
        time.sleep(5)
        psu.write("INST:NSEL 3") # Select channel 3
        psu.write("VOLT 3") # Set brake "position" to 62.5% (hard braking)

    psu.write("INST:NSEL 2") # Select channel 2
    psu.write("VOLT 0.5") # Set throttle "position" to 0%

    # First without faulty state, then with fault
    for fault in range(2):
        #Increment brake by 2.5% until fault
        for j in ramp:
            psu.write("INST:NSEL 3") # Select channel 2
            psu.write("VOLT " + j) # Set brake "position" to 5%
            time.sleep(0.8)
            if(dmm.query("MEAS:IMM:DCV?") < 1):
                print("SHUTDOWN DUE TO BRAKE AT " + ((j-0.5)/4)*100 + "%")
                psu.write("INST:NSEL 2") # Select channel 2
                print("Throttle at " + psu.query("MEAS:VOLT?"))

        key_reset()
        time.sleep(5)
        psu.write("INST:NSEL 2") # Select channel 2
        psu.write("VOLT 0.9") # Set throttle "position" to 10%

    # Assuming above tests pass:
    start()
    key_reset()
    time.sleep(1)

    # Put BSPD into fault
    psu.write("INST:NSEL 2") # Select channel 2
    psu.write("VOLT 1") # Set throttle "position" to 12.5%

    psu.write("INST:NSEL 3") # Select channel 3
    psu.write("VOLT 3") # Set brake "position" to 62.5% (hard braking)

    time.sleep(1)

    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but is active. Critical failure.")
        while True:
            time.sleep(1)

    # Try to power cycle to reset BSPD
    psu.write("INST:NSEL 1") # Select channel 1
    psu.write("VOLT 0") # Set voltage to 0V
    time.sleep(5)
    psu.write("VOLT 12") # Set voltage to 12V

    time.sleep(5)

    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but has been reset after power cycle. Critical failure.")
        while True:
            time.sleep(1)

    key_reset()

    if(dmm.query("MEAS:IMM:DCV?") < 1):
        print("BSPD should be in normal operating condition, but is outputing a shutdown signal. Critical failure")
        while True:
            time.sleep(1)

    # Loss of Power test

    start()
    key_reset()

    psu.write("INST:NSEL 1") # Select channel 1
    psu.write("VOLT 0") # Set voltage to 0V

    time.sleep(0.8)

    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but is in normal operation while power is off. Critical failure.")
        while True:
            time.sleep(1)

    # Loss of signal tests
    start()
    key_reset()

    psu.write("INST:NSEL 2") # Select channel 2
    psu.write("OUTP OFF") # turn off channel
    time.sleep(0.08)
    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but is in normal operation (Throttle LOS). Critical failure")
        while True:
            time.sleep(1)

    start()
    key_reset()

    psu.write("INST:NSEL 3") # Select channel 3
    psu.write("OUTP OFF") # turn off channel
    time.sleep(0.08)
    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but is in normal operation (Brakes LOS). Critical failure")
        while True:
            time.sleep(1)
    
    # High fault tests

    start()
    key_reset()

    psu.write("INST:NSEL 2") # Select channel 2
    psu.write("VOLT 5") # Simulate high sensor fault
    time.sleep(0.08)
    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but is in normal operation (Throttle High Fault). Critical failure")
        while True:
            time.sleep(1)

    start()
    key_reset()

    psu.write("INST:NSEL 3") # Select channel 3
    psu.write("VOLT 5") # Simulate high sensor fault
    time.sleep(0.08)
    if(dmm.query("MEAS:IMM:DCV?") > 1):
        print("BSPD should be outputing shutdown signal, but is in normal operation (Brakes High Fault). Critical failure")
        while True:
            time.sleep(1)
    
    print("WOOHOO! BSPD Passes IC.4.8!")

dmm.close()
psu.close()