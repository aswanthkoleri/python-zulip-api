
import re
import os
import sys
import logging
import configparser
import zulip
import requests

from typing import Dict, Any, Tuple, Union

# Reminder bot format : neo discussion on <subject> at <time> <Date> 
client = zulip.Client(config_file="~/zuliprc")

class botHandler(object):
    def usage(self) -> str:
        return "This is just a sample bot"
        # Discussion\s+on\s+(\w+)\s+at\s+(\w+)\s+(\w+)
    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
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

                
handler_class=botHandler

