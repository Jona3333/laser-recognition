import serial


def capture_image():
    ser = serial.Serial('COM3', 115200, timeout=5)  # change COM3 to your Arduino port
    with open('captured.jpg', 'wb') as f:
        capturing = False
        while True:
            line = ser.readline().decode(errors='ignore').strip()
            if line == "CAPTURING...":
                print("Capturing image...")
            elif line.startswith("SIZE:"):
                size = int(line.split(":")[1])
                print(f"Receiving {size} bytes...")
                data = ser.read(size)
                f.write(data)
                print("Saved captured.jpg")
            elif line == "DONE":
                print("Done!")
                break


if __name__ == '__main__':
    capture_image()