#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#  /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\  
# <   -  Brandhunt Product Update Scraper Module  -   >
#  \|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/

# --- IMPORT SECTION --- #

import os
import requests
import json
import importlib.util

ext_py_mod_url = os.environ['MORPH_GET_SCRIPT_URL']
max_prods = os.environ['MORPH_MAX_PRODS']

r = requests.get(ext_py_mod_url)
jsonpy = json.loads(r.content)
filecont = jsonpy[0]['file_cont']
filecont = json.loads(filecont)

spec = importlib.util.spec_from_loader('helper', loader=None)
helper = importlib.util.module_from_spec(spec)
newcont = ''

del filecont[-16:-1]

for cont in filecont:
    newcont = newcont + cont
    #print(cont)
exec(newcont, helper.__dict__)
exec('mainfunc(' + str(max_prods) + ')', helper.__dict__)
