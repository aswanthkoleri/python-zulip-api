
import re
import os
import sys
import logging
import configparser
import zulip
import requests
import pytz
import threading
from typing import Dict, Any, Tuple, Union
from datetime import datetime, timezone
import time
# Reminder bot format : neo discussion on <subject> at <time> <Date>
def utc_to_local(utc_dt,local_tz):
    local_dt= utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

def asLocalTimeString(utc_dt,local_tz):
    return utc_to_local(utc_dt,local_tz).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')
def getTimestamp(t):
    return time.mktime(t.timetuple())
client = zulip.Client(config_file="~/zuliprc")

class botHandler(object):
    def usage(self) -> str:
        return "This is just a sample bot"
        # Discussion\s+on\s+(\w+)\s+at\s+(\w+)\s+(\w+)

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
            print(message)
            REGEX="discussion\s+on\s+(.+)\s+at\s+(.+)\s+(.+)"
            messageContent=message['content']
            data=re.search(REGEX,messageContent,re.IGNORECASE)
            if data:
                bot_handler.send_reply(message,data.group(1)+" "+data.group(2)+" "+data.group(3))
                print(message['sender_short_name'])
                SCHEDULER = message['sender_short_name']
                # UTC time
                subject=data.group(1)
                UTCtime = data.group(3)
                UTCdate= data.group(2)
                UTC_string = UTCdate + " " + UTCtime
                print(UTC_string)
                # TODO: 1. Collect all the users in realm
                # TODO: 2. Create the message for each user including the converted time
                # TODO: 3. Send the message as PM to all the users in the Zulip realm
                # TODO: 4. Send a message half an hour before the meeting 
                # 1. Collect all users in realm
                all_users = client.get_members()
                non_bot_users = [x for x in all_users['members'] if x['is_bot']==False ]
                print(non_bot_users)
                # 2. Create the message for each user including the converted time
                for user in non_bot_users:
                    #  Get the time zone for each user
                    timezone =  pytz.timezone(user['timezone'])
                    # get the converted time for the user
                    # for converting first we need to convert the UTC_string to UTC date object 
                    UTC_datetimeObject=datetime.strptime(UTC_string, '%Y-%m-%d %H:%M:%S')
                    convertedTime=asLocalTimeString(UTC_datetimeObject,timezone)
                    MESSAGE = "@**"+SCHEDULER+"** arranged a meeting about "+subject+" on "+convertedTime
                    # 3. Send the Message as PM to user
                    request={
                        "type":"private",
                        "to":user['email'],
                        "content":MESSAGE    
                    }
                    result=client.send_message(request)
                # 4. Send a message half an hour before the meeting
                # Get the time stamp of the schedule message
                timestampSchedule=message['timestamp']
                # Get the time stamp of the meeting time
                timestampMeeting=getTimestamp(UTC_datetimeObject)
                print(timestampMeeting)
                # Now get the timestamp just before 30 mins of the meeting 
                # 30 mins = 30*60 s= 1800
                diff=timestampMeeting-timestampSchedule-1800
                timestampReminder=diff if (diff>0 ) else 0
                def reminder():
                    for user in non_bot_users:
                        REMINDER_MESSAGE = "REMINDER : @**"+SCHEDULER+"** arranged a meeting about "+subject+" on "+convertedTime
                        request={
                        "type":"private",
                        "to":user['email'],
                        "content":REMINDER_MESSAGE    
                    }
                    result=client.send_message(request)
                    timer.cancel()
                # Run a timer to send the message
                timer = threading.Timer(timestampReminder,reminder)
                timer.start()
                return
handler_class=botHandler
