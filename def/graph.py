import os
import datetime
import pandas as pd
import matplotlib.pyplot as pl
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

class graph():

    def analiseGraficaOpcao2(table, cpf):
        
        tabelaEntrada = table
        weekday_name = ["SEG", "TER", "QUA", "QUI", "SEX", "SAB", "DOM"]

        tabelaEntrada['Ano'] = tabelaEntrada['dataPassagem']. apply(lambda x: (datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).strftime('%Y'))
        tabelaEntrada['Mes'] = tabelaEntrada['dataPassagem']. apply(lambda x: (datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).strftime('%m'))
        tabelaEntrada['Dia'] = tabelaEntrada['dataPassagem']. apply(lambda x: (datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).strftime('%d'))
        tabelaEntrada['Sem'] = tabelaEntrada['dataPassagem']. apply(lambda x: weekday_name[(datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).weekday()])
        tabelaEntrada['Hora'] = tabelaEntrada['dataPassagem']. apply(lambda x: int((datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).strftime('%H')))
        tabelaEntrada['Minuto'] = tabelaEntrada['dataPassagem']. apply(lambda x: int((datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).strftime('%M')))
        tabelaEntrada['Segundo'] = tabelaEntrada['dataPassagem']. apply(lambda x: int((datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%S')).strftime('%S')))

        explode = (0.1, 0, 0.1, 0, 0.1, 0)
        Local = tabelaEntrada["local"].value_counts()
        localTrun = Local[0:6]

        localTrunName = []
        for i in range(len(list(localTrun))):
            localTrunName.append((pd.DataFrame(localTrun)).iloc[i].name)

        localFreq0 = (pd.DataFrame(localTrun)).iloc[0].name
        expLocal0 = tabelaEntrada[tabelaEntrada['local'].str.contains(localFreq0)]

        localFreq1 = (pd.DataFrame(localTrun)).iloc[1].name
        expLocal1 = tabelaEntrada[tabelaEntrada['local'].str.contains(localFreq1)]


        ###### Grafico Pie ###########################

        fig, ax = pl.subplots(nrows=2, figsize=(20, 20))

        pl.figure(figsize=(22, 22))
        G = gridspec.GridSpec(4, 4)
        pl.subplots_adjust(hspace=0.4, wspace=0.4)

        axes_1 = pl.subplot(G[0, :])

        patches, texts, pcts  = axes_1.pie(list(localTrun), 
                                    labels = localTrunName,
                                    autopct='%.0f%%',
                                    explode=explode,
                                    textprops={'fontsize': 12})

        axes_1.set_title('Frequência x Local', fontsize=16)
        pl.setp(pcts, color='white', size=12, fontweight='bold')


        ###### Grafico hist localFreq 0 ###########################

        axes_2 = pl.subplot(G[1:2, :3])
        expLocal0["Hora"].value_counts().plot.bar(ax =axes_2, align='center'
                                #bins=10,
                                #xticks=range(0,24,1), 
                                #sharex=True, 
                                #sharey=True)
                                )

        axes_2.tick_params(axis='both', which='both', labelsize=12)
        pl.xticks(rotation=0)
        pl.title(localFreq0, size=16)
        pl.xlabel('Hora', size=12)
        pl.ylabel('Frequência', size=12)
        for bar in axes_2.patches:
            pl.annotate(int(bar.get_height()), 
                    (bar.get_x() + bar.get_width() / 2, bar.get_height()-0.6), ha='center', va='center',
                    size=12,
                    fontweight='bold',
                    color='black',
                    xytext=(0, 8),
                    textcoords='offset points')


        ###### Grafico hist localFreq 1 ###########################

        axes_3 = pl.subplot(G[2:3, :3])
        expLocal1["Hora"].value_counts().plot.bar(ax =axes_3,  align='center'
                                #bins=24,
                                #xticks=range(0,24,1), 
                                #sharex=True, 
                                #sharey=True
                                )

        #axes_3.tick_params(axis='both', which='both', labelsize=12)
        pl.title(localFreq1, size=16)
        pl.xticks(rotation=0)
        pl.xlabel('Hora', size=12)
        pl.ylabel('Frequência', size=12)
        for bar in axes_3.patches:
            pl.annotate(int(bar.get_height()), 
                    (bar.get_x() + bar.get_width() / 2, bar.get_height()-0.6), ha='center', va='center',
                    size=12,
                    fontweight='bold',
                    color='black',
                    xytext=(0, 8),
                    textcoords='offset points')


        ###### Grafico hist localFreq0 Semana ###########################

        axes_4 = pl.subplot(G[1:2, -1])
        expLocal0["Sem"].value_counts().plot.barh(ax = axes_4, align='center')
        pl.title('Dia da Semana x Frequência', size=16)
        axes_4.tick_params(axis='both', which='both', labelsize=12)
        axes_4.invert_yaxis()
        pl.ylabel('Dia', size=12)
        for bar in axes_4.patches:
            pl.text(bar.get_width()-1.4, 
                    bar.get_y()+0.3,
                    str(round((bar.get_width()), 2)),
                    fontsize=12, fontweight='bold',
                    color='black')


        ##### Grafico hist localFreq1 Semana ###########################

        axes_5 = pl.subplot(G[2:3, -1])
        expLocal1["Sem"].value_counts().plot.barh(ax = axes_5, align='center')
        pl.title('Dia da Semana x Frequência', size=16)
        axes_5.tick_params(axis='both', which='both', labelsize=12)
        axes_5.invert_yaxis()
        pl.ylabel('Dia', size=12)
        for bar in axes_5.patches:
            pl.text(bar.get_width()-1.4, 
                    bar.get_y()+0.3,
                    str(round((bar.get_width()), 2)),
                    fontsize=12, fontweight='bold',
                    color='black')

        if os.path.isdir(os.getcwd() + '/graph/' + str(cpf)):
            graf = os.getcwd() + '/graph/' + str(cpf) + str('/graficos.png')
        else: 
            os.makedirs(os.getcwd() + '/graph/' + str(cpf))
            graf = os.getcwd() + '/graph/' + str(cpf) + str('/graficos.png')
        
        pl.savefig(graf, dpi = 300, 
                orientation='landscape', papertype=None, format=None,
                transparent=False,  bbox_inches='tight', pad_inches=0.1,
                frameon=None, metadata=None)