#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto

This module is resposible for login 
in MINERVA graphql server. Expected
answer is 200 with:
1. firt name user
3. token  JWT  Minerva  server what 
   encode, cpf and email.
4. MJ token

Return this module is status and data
"""

import requests
import json
import configparser
 
config = configparser.ConfigParser()
config.read("/media/dgbe/HD/appAnaliseMovimento/appAnaliseMovimento/config/.ini")
hostMinerva = config.get('geral', 'HOST_MINERVA')


def login(email, password):
    
	url = hostMinerva

	query = ('mutation{login(email:"%s" password:"%s"){first_name confirmed_is token AUTH_TOKEN_MJ AUTH_TOKEN_MJ_PESSOA}}' %(email, password))

	response = requests.post(url, json={'query': query})
	status = response.status_code
	data = response.json()

	return (status, data)