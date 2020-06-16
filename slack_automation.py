# coding: UTF-8

import sys
import random
import time
import requests

def main():
    print(len(sys.argv))

    if not 5 >= len(sys.argv) >= 4:
        print('You need just 3 or 4 arguments.')
        sys.exit()

    token = sys.argv[1] # Slack Token: string
    channel = sys.argv[2] # Target Channel: string
    message = sys.argv[3] # Message: string

    print('Token: ' + sys.argv[1])
    print('Channel: ' + sys.argv[2])
    print('Message: ' + sys.argv[3])

    if len(sys.argv) >= 5:
        temp = sys.argv[4] # Send Temperature: boolean
        print('Temperature: ' + sys.argv[4])

    rand_time = random.randint(1, 420)
    rand_temp = round(random.uniform(35.5, 36.6), 1)

    if len(sys.argv) >= 5:
        message = message + ' ' + str(rand_temp)
        print('Temperature: ' + str(rand_temp) + '℃')

    print('Wait time: ' + str(rand_time) + 's')

    time.sleep(rand_time)

    data = {
        'token': token,
        'channel': channel,
        'text': message,
        'as_user': True,
    }
    response = requests.post('https://slack.com/api/chat.postMessage', data=data)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    main()
