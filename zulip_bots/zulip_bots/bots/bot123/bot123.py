
import re
import os
import sys
import logging
import configparser
<<<<<<< HEAD
import zulip
=======
import pytz
>>>>>>> 8d8241fabcf5916c8299f2ee1557210690af9888
import requests

from typing import Dict, Any, Tuple, Union
from datetime import datetime, timezone
# Reminder bot format : neo discussion on <subject> at <time> <Date>
def utc_to_local(utc_dt):
    local_dt= utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

<<<<<<< HEAD
# Reminder bot format : neo discussion on <subject> at <time> <Date> 
=======
def asLocalTimeString(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')

>>>>>>> 8d8241fabcf5916c8299f2ee1557210690af9888
client = zulip.Client(config_file="~/zuliprc")

class botHandler(object):
    def usage(self) -> str:
        return "This is just a sample bot"
        # Discussion\s+on\s+(\w+)\s+at\s+(\w+)\s+(\w+)

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
<<<<<<< HEAD
            REGEX="Discussion\s+on\s+(.+)\s+at\s+(.+)\s+(.+)"
            data=re.search(REGEX,message['content'],re.IGNORECASE)
            if data:
                # Have to get date time and subject in different variables
                date=data.group(3)
                time=data.group(2)
                subject=data.group(1)
                # Got the time date now get the timezone of the user and convert it to UTC
                result = client.get_members()
                print(result)
                # Then take each user 
                bot_handler.send_reply(message,"Date: "+date+"Time: "+time+"Subject: "+subject)

            else:
                bot_handler.send_reply(message,"Wrong format")

                
=======
            print(message)
            REGEX="discussion\s+on\s+(.+)\s+at\s+(.+)\s+(.+)"
            messageContent=message['content']
            data=re.search(REGEX,messageContent,re.IGNORECASE)
            if data:
               bot_handler.send_reply(message,data.group(1)+" "+data.group(2)+" "+data.group(3))
               print(message['message']['display_recipient'])
               SCHEDULER = message['message']['display_recipient']
            #    convert UTC time to Local time and send the message to everyone in the stream
                # UTC time
                subject=data.group(1)
                UTCtime = group(2)
                UTCdate= group(3)
                UTC_string = UTCdate + " " + UTCtime
                print(UTC_string)
                # TODO: 1. Collect all the users in realm
                # TODO: 2. Create the message for each user including the converted time
                # TODO: 3. Send the message as PM to all the users in the Zulip realm
                # 1. Collect all users in realm
                all_users = client.get_members()
                non_bot_users = [x for x in all_users['members'] if x['is_bot']==False ]
                print(non_bot_users)
                # 2. Create the message for each user including the converted time
                for user in non_bot_users:
                    #  Get the time stamp
                    timezone = user['user']
                    MESSAGE = "@**"+SCHEDULER+"** arranged a meeting about "+subject+"on "


               return
>>>>>>> 8d8241fabcf5916c8299f2ee1557210690af9888
handler_class=botHandler
