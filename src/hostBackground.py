import serial
import rotatescreen
import time
import screen_brightness_control as sbc

def initSerial(dev):
    ser = serial.Serial(dev, 9600, timeout=1,
                        xonxoff=False, rtscts=False, dsrdtr=False)
    ser.flushInput()
    ser.flushOutput()
    return ser

def waitForSerialInit():
    possibleDevices = ["COM5"]
    while True:
        for dev in possibleDevices:
            try:
                ser = initSerial(dev)
                print("device found on " + dev)
                return ser
            except Exception:
                print("Failed to initialise device on " + dev)
        time.sleep(5)

ser = waitForSerialInit()

monitor = rotatescreen.get_secondary_displays()[0]
landscape = monitor.current_orientation == 0

while True:
    try:
        line = ser.readline().decode("utf-8")
    
    except Exception:
        print("error: ")
        print("probably not plugged in")
        time.sleep(5)
        print("trying to init serial again")
        ser = waitForSerialInit()
        continue


    if line == "":
        continue # ignore empty lines

    if (line.find("command: landscape") != -1):
        if not landscape:
            monitor.set_landscape()
            landscape = True

        
    if (line.find("command: portrait") != -1):
        if landscape:
            monitor.set_portrait_flipped()
            landscape = False

    if (line.find("brightness: ") != -1):
        cbr = -1
        try:
            cbr = sbc.get_brightness(display=0)
        except Exception:
            pass

        nbr = int(line.replace("brightness: ", ""))
        if(nbr != cbr):
            try:
                sbc.set_brightness(nbr, display=0)
            except Exception:
                pass