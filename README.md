# monitor-tilt-detect

This project uses an arduino with some kind of orientation detecting switch to automatically rotate a monitor on windows.

main.cpp is the code for the arduino. I'm using pin 2 to supply 5v to my switch module and 3 for the signal because this means I could plug my switch module into the breadboard the arduino is one directly without wires.
Every 2 seconds it polls the switch and send a command over serial.

hostBackground.py is a file that receives the command over serial and rotates the screen if necessary.

`possibleDevices` is a list of com ports to try connecting to the arduino.

I have 2 monitors and want to rotate the second one so my monitor is defined as the only monitor from the list that is not my main monitor.


## Dependencies

[pyserial](https://pypi.org/project/pyserial/)

[rotate-screen](https://pypi.org/project/rotate-screen/)

[pywin32](https://pypi.org/project/pywin32/)



## automatically start hostBackground.py

press: winKey + r

enter: 'shell:startup' 

press: ok

create a file ANYNAME.cmd 

file content: ```start pythonw "C:\FULL_PATH_TO_FILE\hostBackground.py"```
