"""
extract_msg:
    Extracts emails and attachments saved in Microsoft Outlook's .msg files

https://github.com/mattgwwalker/msg-extractor
"""

__author__ = 'Matthew Walker & The Elemental of Creation'
__date__ = '2018-05-22'
__version__ = '0.20.2'

import glob
import sys
import traceback
from extract_msg.base import Attachment, Properties, Prop, Recipient, Message, parse_type, properHex
from extract_msg import constants
