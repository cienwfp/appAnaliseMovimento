#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto

This module processes the option 2
of the menuInicial
"""
import datetime
import pandas as pd
from getMJ import getMJ
    
class opcao():  
          
    def opcao2(placa, dataInicial, dataFinal, tokenMJ, cpf):
                
        dataInicio = datetime.datetime.strptime(dataInicial, '%d/%m/%Y')
        dataFim = datetime.datetime.strptime(dataFinal, '%d/%m/%Y')
        deltaTime = abs((dataInicio - dataFim).days)

        df1 = pd.DataFrame()
        df2 = pd.DataFrame()

        if deltaTime > 30:
            dataFimParcial = dataInicio
            dataInicioParcial = dataInicio
            controle = 0

            while dataFimParcial < dataFim and controle!=1:
                dataFimParcial = dataInicioParcial + datetime.timedelta(days=30)

                if dataFimParcial > dataFim:
                    dataFimParcial = dataFim
                    controle = 1

                msg, dados = getMJ.getMovimentoPeriodo(placa, dataInicioParcial.strftime("%Y-%m-%dT%H:%M:%S"), dataFimParcial.strftime("%Y-%m-%dT%H:%M:%S"), tokenMJ, cpf)
                            
                dataInicioParcial = dataFimParcial
                
                if msg != '':
                    print('Erro: Erro para busca entre as datas %s e %s' (dataInicioParcial, dataFimParcial))
                else:
                    df1 = pd.json_normalize(dados)
                    df2 = df2.append(df1, ignore_index=True)

        else:
            msg, dados = getMJ.getMovimentoPeriodo(placa, dataInicio.strftime("%Y-%m-%dT%H:%M:%S"), dataFim.strftime("%Y-%m-%dT%H:%M:%S"), tokenMJ, cpf)
            if msg != '':
                print('Erro: Erro para busca entre as datas %s e %s' (dataInicioParcial, dataFimParcial))
            else:
                df1 = pd.json_normalize(dados)
                df2 = df2.append(df1, ignore_index=True)
        
        return(df2)
    
    def opcao3(dadosEntrada, dataInicial, dataFinal, tokenMJ, cpf):
                
        dataInicio = datetime.datetime.strptime(dataInicial, '%d/%m/%Y %H:%M')
        dataFim = datetime.datetime.strptime(dataFinal, '%d/%m/%Y %H:%M')
        deltaTime = abs(((dataInicio - dataFim).days))*24

        latitude = dadosEntrada.split(',')[0]
        longitude = dadosEntrada.split(',')[1]
        raio = dadosEntrada.split(',')[2]
        
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()

        msg, listLocal = getMJ.getListaLocal(latitude, longitude, raio, tokenMJ, cpf)
        
        localTable = pd.json_normalize(listLocal)
        
        if msg != '':
            print('Erro: ', msg )
            df2 = pd.DataFrame()
            return(df2)
        
        if localTable.empty:
            print('Erro: Lista de local vazia')
            df2 = pd.DataFrame()
            return(df2)

        listaIdLocal = list(localTable['idLocal'])
        
        for local in listaIdLocal:
            
            if deltaTime > 1:
                dataFimParcial = dataInicio
                dataInicioParcial = dataInicio
                controle = 0
                    
                while dataFimParcial < dataFim and controle!=1:
                    dataFimParcial = dataInicioParcial + datetime.timedelta(days=(1/24))

                    if dataFimParcial > dataFim:
                        dataFimParcial = dataFim
                        controle = 1

                    msg, dados = getMJ.reqIdLocalPeriodo(local, dataInicioParcial.strftime("%Y-%m-%dT%H:%M:%S"), dataFimParcial.strftime("%Y-%m-%dT%H:%M:%S"), tokenMJ, cpf)
                                
                    dataInicioParcial = dataFimParcial
                    
                    if msg != '':
                        print('Erro: Erro para busca entre as datas %s e %s' (dataInicioParcial, dataFimParcial))
                    else:
                        df1 = pd.json_normalize(dados)
                        df2 = df2.append(df1, ignore_index=True)

            else:
                msg, dados = getMJ.reqIdLocalPeriodo(local, dataInicioParcial.strftime("%Y-%m-%dT%H:%M:%S"), dataFimParcial.strftime("%Y-%m-%dT%H:%M:%S"), tokenMJ, cpf)
                if msg != '':
                    print('Erro: Erro para busca entre as datas %s e %s' (dataInicioParcial, dataFimParcial))
                else:
                    df1 = pd.json_normalize(dados)
                    df2 = df2.append(df1, ignore_index=True)
            
            df2.to_csv('teste.csv', sep=';')
            
        return(df2)