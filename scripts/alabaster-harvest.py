#!/usr/bin/env python3

import json
import re
import httpx
import urllib
import configparser
from datetime import timedelta, datetime
from xml.dom import minidom

# define function to get the creds
def read_json_creds(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


