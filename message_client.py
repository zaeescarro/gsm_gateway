import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")

def get_messages():
    try:
        params = {"gateway": "mario"}
        response = requests.get(API_URL + "/api/queue", params=params)
        # response = requests.get(API_URL + "/api/queue")
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to get message:", response.status_code)
            return None
    except Exception as e:
        print("Error:", str(e))
        return None

def message_sent(message_id):
    try:
        data = {"message_id": message_id, "token": API_TOKEN}
        response = requests.post(API_URL + "/api/message_sent", data=data)
        # response = requests.post(API_MESSAGE_SENT, json={"message_id": message_id})
        if response.status_code == 200:
            r = response.json()
            print("Updating message in server... " + r['status'])
            # print("Message status updated successfully")
        else:
            print("Failed to update message status:", response.status_code)
    except Exception as e:
        print("Error:", str(e))
        