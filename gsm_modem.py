import serial
import time
import requests

# Configure Serial Port (Change 'COM5' to your correct port)
PORT = "COM5"   # For Windows: COM5, COM3, etc. | For Linux: /dev/ttyUSB0, /dev/ttyS0
BAUD_RATE = 9600  # Common baud rates: 9600, 115200

def send_sms(phone_number, message):
    try:
        # Open serial connection to GSM modem
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        time.sleep(1)  # Wait for connection

        # Send AT commands to configure SMS sending
        ser.write(b'AT\r')  # Check connection
        time.sleep(0.5)
        # print(ser.read(64).decode(errors='ignore'))

        ser.write(b'AT+CMGF=1\r')  # Set SMS mode to text
        time.sleep(0.5)
        # print(ser.read(64).decode(errors='ignore'))

        # Set recipient phone number
        ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
        time.sleep(0.5)
        # print(ser.read(64).decode(errors='ignore'))

        # Send message text
        ser.write(message.encode() + b"\r")
        time.sleep(0.5)

        # Send CTRL+Z to indicate the end of message (ASCII 26)
        ser.write(b'\x1A')
        time.sleep(3)  # Wait for modem to send SMS

        # Read modem response
        response = ser.read(128).decode(errors='ignore')
        # print("Modem Response:", response)

        print("SMS sent")

        # Close serial connection
        ser.close()

    except Exception as e:
        print("Error:", str(e))

# Example: Send SMS
# send_sms("+639228545058", "Hello from Python GSM Modem!")