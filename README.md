# gsm_gateway


```
pip install pyserial
pip install python-dotenv
```

## Configuration

Change the .env file to link to correct API URL which exposes the messages via api/queue and api/message_sent to update
message status for GSM

```
API_URL=http://localhost:8888/zae/aims
```

In the gsm_modem.py, change the PORT to reflect the proper Ports. Run Device Manager, check Ports (COM & LPT) and check the 
USB-SERIAL CH340 and get the COM<X>. Sample if it's COM6, change the PORT to COM6

## Run

```
python main.py
```

## Linux

```
ls /dev/tty*
```