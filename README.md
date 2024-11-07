# Portfolio
Hi! I'm Liam H, a student at the Colorado School of Mines studying Electrical Engineering. At Mines, I am the lead electrical engineer for the Mines Formula SAE Team. Outside FSAE, I am involved with the Mines Theme Park Engineering and Design Group (TPED), Tau Beta Pi, and IEEE. I am passionate about electrical engineering, teaching, and space exploration. Feel free to connect with me on [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/liam-homburger/).

# Theseus
  Two prototypes that lead to a product, the Theseus Escape Room Controller. 
  I started designing escape room controllers in 2022 for the Mines Themepark Engineering and Design Group (TPED). I needed a way to control multiple electronic puzzles at a central point, without daisy chaining of off-the-shelf controllers. (Non-technical [feature article](https://www.themedattraction.com/marvins-gold-rush-escape-colorado-school-of-mines-tped/) of the entire room).
  These Thesus prototypes use a Raspberry Pi running a modified version of Raspbian with node-red to allow graphic programming of the "puzzle flow" in an escape room/themed experience.
  A special version of Theseus is the 0.2 prototype. For this version, I designed it around a Raspberry Pi compute module instead of a regular Raspberry Pi. This board includes controlled impedance HMDI, USB, and Ethernet routing.
## Features of the Theseus0.5 Include:
    -16 Digital GPIO Pins
    -8 Analog Input Pins
    -7 Capacitive Touch Pins
    -8 I2C busses
    -2 WS2812B outputs
    -2 120V compatible relays
    -User-friendly RJ11 Connectors
## Additional features of the Theseus0.3 Include:
    -Motor Driver
    -5V LED Output
# Test and Measurement
  While I can't share details about specific projects at TI, I am familiar with the Pyvisa library and NI's instrument drivers. In addition, I have written SCPI code for Keysight and Tektronix equipment including sampling/real-time oscilloscopes, BERTs, VNAs, Thermal forcing units, DMMs, PSUs, etc used to validate pre-release silicon. I wrote an example script for measuring the temperature of cells over different C rates and included it in this folder.
  I also added a script I wrote to validate our BSPD vs IC.4.8. 
# Power Supply
  This is an adjustable power supply with 8 indicator lights designed for my electric devices class. It features an Analog Devices LDO and is capable of outputting 0-1A at up to 0-12V.
