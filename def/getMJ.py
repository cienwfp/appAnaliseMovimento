#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto

This class is resposible for get data
in MJ API.  The  class  has functions
to get data in:

1. getMovimentoSimples: /movimentos/placa/
2. getMovimentoPeriodo: /movimentos/placa/' + placa +'/periodo?dataHoraFinal='+str(dataFinal)+'&dataHoraInicial='+str(dataInicial))

"""

import requests
import pandas as pd

class getMJ():
        
    def getMovimentoSimple(placa, tokenMJ, CPF):
        
        msg = ''
        url = str('https://devveiculos.azurewebsites.net/movimentos/placa/' + str(placa))

        payload = {}
        files = {}
        headers = {'Authorization': tokenMJ, 'usuario': CPF}

        response = requests.request("GET", url, headers=headers, data = payload, files = files)

        if response.status_code != 200:
            msg = str(response)
            dados = []
        else:
            dados = pd.json_normalize(response.json())
            
        return(msg, dados)
    
    def getMovimentoPeriodo(placa, dataInicial, dataFinal, tokenMJ, CPF):
    
        msg = ''
        url = str('https://devveiculos.azurewebsites.net/movimentos/placa/' + placa +'/periodo?dataHoraFinal='+str(dataFinal)+'&dataHoraInicial='+str(dataInicial))
        payload = {}
        files = {}
        headers = {'Authorization': tokenMJ, 'usuario': CPF}
        
        response = requests.request("GET", url, headers=headers, data = payload, files = files)
        
        if response.status_code != 200:
            mgs = str(response)
            dados = []
        else:
            dados = response.json()

        return(msg, dados)
    
    
    def getListaLocal(lat, long, r, token, cpf):
        
        msg = ''

        url = str('https://devveiculos.azurewebsites.net/local/locais/?latitude=' + str(lat) + '&longitude=' + str(long) + '&raio=' + str(r))

        payload = {}
        files = {}
        headers = {
        'Authorization': token,
        'usuario': cpf, 
        }

        response = requests.request("GET", url, headers=headers, data = payload, files = files)
        
        if response.status_code != 200:
            mgs = str(response)
            dados = []
        else:
            dados = response.json()
        
        print('aqui', dados)

        return(msg, dados)
    
    def reqIdLocalPeriodo(local, dataHoraInicial, dataHoraFinal, token, cpf):
            
        msg = ''

        url = str('https://devveiculos.azurewebsites.net/movimentos/local/'+str(local)+'/periodo?dataHoraFinal='+str(dataHoraFinal)+'&dataHoraInicial='+str(dataHoraInicial))
              
        print(url)
          
        payload = {}
        files = {}
        headers = {
        'Authorization': token,
        'usuario': cpf}

        response = requests.request("GET", url, headers=headers, data = payload, files = files)
        
        if response.status_code != 200:
            mgs = str(response)
            dados = []
        else:
            dados = response.json()

        print(dados)
        return(msg, dados)