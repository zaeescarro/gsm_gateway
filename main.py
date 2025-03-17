import gsm_modem
import message_client
import time

# gsm_modem.send_sms("+639228545058", "Hello from Python GSM Modem!")

while (True):
    messages = message_client.get_messages()['data']
    print(messages)
    for m in messages:
        phone_number = m['recipient']
        message = m['body']
        message_id = m['id'];
                
        phone_number = "+63" + phone_number[-10:]
        print(f"Message for {phone_number}: {message}")
        gsm_modem.send_sms(phone_number, message)

        message_client.message_sent(message_id)
    time.sleep(60)



