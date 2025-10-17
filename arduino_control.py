import serial
import time
from serial.tools import list_ports
import image_capture

def arduino_control():
    # find available ports (pick the one that matches your Arduino)
    ports = list(list_ports.comports())
    for p in ports:
        print(p.device, p.description)

    # set the correct port below (e.g., "COM3" on Windows or "/dev/ttyACM0" on Linux)
    PORT = "/dev/ttyACM0"
    BAUD = 115200

    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)  # wait for Arduino reset after opening serial

    image_capture.capture_image()
    print(send("LASER ON"))
    image_capture.capture_image()
    print(send("LASER OFF"))

    ser.close()

def send(cmd, ser):
    ser.write((cmd + "\n").encode('utf-8'))
    # read ack/response
    resp = ser.readline().decode().strip()
    return resp


