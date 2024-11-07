"""
This is code I wrote to run automatic cycles on various lithium cells to validate their datasheet over temperature range and C rates. It uses an TA5000 from MPI Thermal Corporation
an Agilent 34401a Multimeter, and an electronic load. 

It prints data out to the console so the user can ensure nothing abnormal occurs as it runs. 

If you want to run this program, use the attached virtual enviornment with its libraries, external equipment, and the NI VISA drivers. 

Author: Liam Homburger
Let me know if you have any questions. 
"""

# Must install NI VISA drivers or Keysight Connection Expert. Instruments must be connected over an GPIB bus, otherwise change addresses to IP addresses
import os, time
import pyvisa

rm = pyvisa.ResourceManager()
rm.list_resources()

try:
    stream = rm.open_resource('GPIB0::16::INSTR') # Connect to MPI TA5000 Thermostream
    dmm = rm.open_resource('GPIB0::6::INSTR') # Connect to Ag34401A Digital Multimeter
    eload = rm.open_resource('GPIB0::10::INSTR') # MUST INIT ELECTRONIC LOAD MANUALLY!!!!!!!!
except Exception as e:
    print(str(e))

# SCPI Commands from TA5000 programming guide
stream.write("DUTM 1") # Sets TA5000 to DUT Mode
stream.write("AIRD 40") # Sets air to DUT max dif to 40 C
stream.write("COOL 1") # Initialize compressor
stream.write("MAXT 130") # Sets max temperature to 130 C
stream.write("HEAD 0") # Lower head to DUT
stream.write("FLOW 1") # Enable head flow
stream.write("SETP 25") # Set TA5000 to 25C to begin

while abs((25 - stream.query("TEMPD?")) > 1):
    print("Going to 25C")
    time.sleep(1)

print("Instruments Initialized")

soak_time = 30 # Soak at temp for 60 seconds

cell_capacity = 4.2 # Capacity of cell in Ah

temps = [5, 25, 40]
c_rates = [0.5, 1, 5]

for temp in temps:
    stream.write("SETP " + str(temp))
    print("Going to " + str(temp))
    for c_rate in c_rates:
        eload.write("EN 0")
        eload.write("MODE CC")
        eload.write("CC:SETA " + str((cell_capacity*c_rate)/cell_capacity))
        for temp in temps:
            stream.write("SETP " + str(temp))
            while abs((temp - stream.query("TEMPD?")) > 1):
                print("Going to " + str(temp))
                time.sleep(1)
            print("Temperature set, soaking")
            time.sleep(soak_time)
            print("Measuring")
            print(temp)
            print(eload.query("CC:VALA?"))
            print(dmm.query("MEAS:IMM:DCV?"))
            print("Done Measuring")

stream.close()
dmm.close()
eload.close()