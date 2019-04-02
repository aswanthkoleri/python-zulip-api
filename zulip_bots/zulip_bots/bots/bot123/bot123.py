
import re
import os
import sys
import logging
import configparser

import requests

from typing import Dict, Any, Tuple, Union

class botHandler(object):
    def usage(self) -> str:
        return "This is just a sample bot"
    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
            print(message)
            if message['content']=="help":
               bot_handler.send_reply(message,"This is just a hlp message")
               return
handler_class=botHandler

