import serial
import rotatescreen
import time
import screen_brightness_control as sbc

def initSerial(dev):
    ser = serial.Serial(dev, 9600, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    return ser

def waitForSerialInit():
    possibleDevices = ["COM3"]
    while True:
        for dev in possibleDevices:
            try:
                ser = initSerial(dev)
                print("device found on " + dev)
                return ser
            except Exception as e:
                print(e)
                print("Failed to initialise device on " + dev)
        time.sleep(5)

ser = waitForSerialInit()

rotatableMonitor = rotatescreen.get_secondary_displays()[0]

while True:
    try:
        line = ser.readline().decode("utf-8")
        landscape = rotatableMonitor.current_orientation == 0
        
        if line == "":
            continue # ignore empty lines

        # ROTATION
        if (line.find("command: landscape") != -1  and not landscape):
            try:
                rotatableMonitor.set_landscape()
            except Exception:
                continue
                
        if (line.find("command: portrait") != -1 and landscape):
            try:
                rotatableMonitor.set_portrait_flipped()
            except Exception:
                continue

        # BRIGHTNESS
        if (line.find("brightness: ") != -1):
            cbr = -1
            try:
                cbr = sbc.get_brightness(display=0)
            except Exception:
                continue

            nbr = int(line.replace("brightness: ", ""))
            if(nbr != cbr):
                try:
                    sbc.set_brightness(nbr, display=0)
                except Exception:
                    continue
                try:
                    sbc.set_brightness(nbr, display=1)
                except Exception:
                    continue

                
    
    except Exception as err:
        print(err)
        time.sleep(5)
        print("trying to init serial again")
        ser.close()
        ser = waitForSerialInit()
        continue


