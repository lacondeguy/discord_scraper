import requests
import json
import time

delay = 5 # Delay between checks
channels_id = [100000000000000001, 100000000000000002]

def get_messages(channel_id):
    message_id = 0
    headers = {
        'authorization' : 'key'
    }

    while 1:
        for channel in channels_id:
            r = requests.get(f'https://discord.com/api/v9/channels/{channel}/messages', headers = headers)
            message = json.loads(r.text)
            
            # Check if channel empty
            if message == [] or None:
                print('Wait new message...')
                time.sleep(delay)

            # Сheck if this message has already been forwarded
            else:
                if message[0]['id'] == message_id:
                    print('Wait new message...')
                    time.sleep(delay)

                # If this is a new message, then print it to the console or do something else..
                else:
                    print(f"{message[0]['author']['username']}:")
                    print(message[0]['content'])
                    message_id = message[0]['id']
                    time.sleep(delay)

get_messages(channels_id)
