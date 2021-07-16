#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto

This module takes care of the menu options

"""

import requests
import json
import configparser
import sys
from jose import jwt

import loginMinerva 
import getMJ
from graph import graph
import opcao2
from relatorios import relatorios
 
config = configparser.ConfigParser()
config.read("./config/.ini")
secret = config.get("geral", "SECRET_JWT"),

def inicio():
    print("Entre com suas credenciais do MINERVA")

    email = str(input('Entre com o email: '))
    password = str(input('Digite a sua senha: '))

    status, data = loginMinerva.login(email, password)

    while status == 200:
        
        while data['data'] == None:
            print(data['errors'][0]['extensions']['errors'])
            
            email = str(input('Entre com o email: '))
            password = str(input('Digite a sua senha: '))
            
            status, data = loginMinerva.login(email, password)

            if status != 200:
                print('Erro: ' + status)
                exit()
      
        token = data['data']['login']['token']
        credenciais = jwt.decode(token, secret)
        tokenMJ = data['data']['login']['AUTH_TOKEN_MJ']
        print('Senha bem-vindo ' + credenciais['first_name'])
        break

       
    while True:
        print('Digite a opção desejada:')
        print('Digite 1: Para busca por coordenadas GPS e raio')
        print('Digite 2: Para relatório por período')
        print('Digite q: Para finalizar')
        opcao = input('Opção: ')

        if opcao == 'q':
            break

        if opcao == '1':
            placa = str(input('Digite a placa: '))
            print('Obtendo dados...')
            msg, dados = getMJ.getMovimentoSimple(placa, tokenMJ, credenciais['cpf']) 
            if msg == '':
                print('Dados Obtidos com sucesso')
            else:
                print('Ocorreu um erro na obtenção dos dados. Erro: ', msg)
        
        if opcao == '2':
            placa = str(input('Digite a placa (ex:AAA0000 ou AAA0A00): '))
            dataInicial = str(input('Data inicial (ex:XX/XX/XXXX): '))
            dataFinal = str(input('Data Final (ex:XX/XX/XXXX): '))
            print('Obtendo dados...')
            
            table = opcao2.opcao2(placa, dataInicial, dataFinal, tokenMJ, credenciais['cpf'])
            if table.empty:
                print('Erro: Os dados retornaram vazios')
            else:
                graph.analiseGraficaOpcao2(table, credenciais['cpf'])
                relatorios.relatorioOpcao2(credenciais['first_name'], credenciais['cpf'], placa, dataInicial, dataFinal, table)
                
            
            