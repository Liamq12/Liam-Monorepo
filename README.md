# Liam's Monorepo
Hi! I'm Liam Homburger, a student at the Colorado School of Mines studying Electrical Engineering. At Mines, I am the lead electrical engineer for the Mines Formula SAE Team. Outside FSAE, I am involved with the Mines Theme Park Engineering and Design Group (TPED), Tau Beta Pi, and IEEE. I am passionate about electrical engineering, teaching, and space exploration. Feel free to connect with me on [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/liam-homburger/).

This monorepo holds things/projects I have worked on that I think are interesting but not worth their own repo. Feel free to reach out to me if you have any questions!

# Theseus
  Two prototypes that lead to a product, the Theseus Escape Room Controller. 
  I started designing escape room controllers in 2022 for the Mines Themepark Engineering and Design Group (TPED). I needed a way to control multiple electronic puzzles at a central point, without daisy-chaining off-the-shelf controllers. (Non-technical [feature article](https://www.themedattraction.com/marvins-gold-rush-escape-colorado-school-of-mines-tped/) of the entire escape room).
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
# BSPD 2
This is an brake system plausibility device used by Mines Formula. You may be wondering what happened to BSPD 1? BSPD 1 which I designed years ago was (literally) hanging on by a trace at competition this year. In addition, it uses an RC timer, which does not work well with multiple implausible states, followed by a correction. Because of this, I redesigned it to work with an binary ripple adder which is more precise, and instantly resets. 
This is an brake system plausibility device used by Mines Formula. You may be wondering what happened to BSPD 1? BSPD 1 which I designed years ago was (literally) hanging on by a trace at competition this year. In addition, it uses an RC timer, which does not work well with multiple implausible states, followed by a correction. Because of this, I redesigned it to work with a binary ripple adder, which is more precise, and instantly resets. 
The latching requirement is satisfied by a comparator with positive feedback/extreme hysteresis, and overall, the size of the BSPD 2 is about 20% smaller than BSPD 1.
# Wavy FSTM32
(Formula STM32 Devboard) This is my attempt to settle on of the most heated debates in electrical engineering. Can curved PCB traces look decent? Unlike the tabs vs spaces argument, I don’t think there is a clear winner, but I wanted to design a board with curved traces. This also doubles up as Mines Formula's IsoSPI devboard, used to talk with our BMS modules during development. 
# Test and Measurement
  While I can't share details about specific projects at TI, I am familiar with the Pyvisa library and NI's instrument drivers. In addition, I have written SCPI code for Keysight and Tektronix equipment including sampling/real-time oscilloscopes, BERTs, VNAs, Thermal forcing units, DMMs, PSUs, etc used to validate pre-release silicon. I wrote an example script for measuring the temperature of cells over different C rates and included it in this folder.
  I also added a script I wrote to validate our Formula Society of Automotive Engineers (FSAE) Brake System Plausibility Device (BSPD) vs FSAE Rule IC.4.8. 
# Power Supply
  This is an adjustable power supply with 8 indicator lights made for my electric devices class. It features an Analog Devices LDO and is capable of outputting 0-1A at up to 0-12V. I mainly focused on the PCB layout. 
