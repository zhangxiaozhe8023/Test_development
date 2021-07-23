from func_login import login
import requests

s = requests.session()
login(s)

from ke9.func_login import *