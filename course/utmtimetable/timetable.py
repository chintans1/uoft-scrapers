import requests, http.cookiejar
from bs4 import BeautifulSoup
from collections import OrderedDict
import time
import re
import os
import json
import pprint
import tidylib


class UTMTimetable:

    def __init__(self):
        self.host = 'https://student.utm.utoronto.ca/timetable/'

    def update_files(self):
        pass