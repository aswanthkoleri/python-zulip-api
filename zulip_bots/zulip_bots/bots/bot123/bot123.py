
import re
import os
import sys
import logging
import configparser

import requests

from typing import Dict, Any, Tuple, Union

# Reminder bot format : neo discussion on <subject> at <time> <Date> 


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
            #    convert UTC time to Local time and send the message to everyone in the stream
                # UTC time
                UTCtime = group(2)
                UTCdate= group(3)
                UTCtotal = UTCdate + " " + UTCtime
                # Now we got the UTC time in a variable 
                # We have to run a loop to send a PM to all the users in a stream.
               return
handler_class=botHandler

