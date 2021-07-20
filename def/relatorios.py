import os
import time
from reportlab.lib import utils
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, NextPageTemplate, PageTemplate, PageBreak, Paragraph, Spacer, Image, Table, TableStyle, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

class relatorios():

    def addPageNumber(canvas, doc):
        """
        Add the page number
        """
        page_num = canvas.getPageNumber()
        text = "Pag %s" % page_num
        canvas.drawRightString(200*mm, 10*mm, text)
        
        
    def relatorioOpcao1(name, cpf, placa, table):
        
        '''
        Report of Option one. This has content of the
        ten last observations of the veficle
        '''
        
        if os.path.isdir(os.getcwd() + '/report/' + str(cpf)):
            rep = os.getcwd() + '/report/' + str(cpf) + str('/reportOption1.pdf')
        else: 
            os.makedirs(os.getcwd() + '/report/' + str(cpf))
            rep = os.getcwd() + '/report/' + str(cpf) + str('/reportOption1.pdf')
            
        doc = SimpleDocTemplate(rep,pagesize=(A4),
                                rightMargin=30,leftMargin=30,
                                topMargin=30,bottomMargin=30)


        styles=getSampleStyleSheet()

        Story=[]
        logo = os.getcwd() + '/payload/' + str('logo.png')
        formatted_time = time.ctime()
        
        
        #### Página 2 ######################################################################


        im = Image(logo, 20*mm, 20*mm)
        im.hAlign = 'LEFT'
        Story.append(im)
        Story.append(Spacer(1, 48))

        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        ptext = '<font size="12">Olá senhor %s</font>' %(name)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        ptext = '<font size="12">Este relatório foi produzido seguindo os seguintes parâmetros de pesquisa:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        ptext = '<font size="12">Placa: %s</font>'%(placa)
        Story.append(Paragraph(ptext, styles["Justify"]))

        
        Story.append(Spacer(1, 36))
        
        styleN = styles["Normal"]
        # Make heading for each column and start data list
        column1Heading = "COLUMN ONE HEADING"
        column2Heading = "COLUMN TWO HEADING"
        # Assemble data for each column using simple loop to append it into data list
        data = [[column1Heading,column2Heading]]

        #for i in table:
        #    data.append([str(i),str(i)])

        data_ = table.drop(columns = ['idMovimento'])

        data = [data_.columns[:,].values.astype(str).tolist()] + data_.values.tolist()

        tableThatSplitsOverPages = Table(data, repeatRows=1)
        tableThatSplitsOverPages.hAlign = 'CENTER'
        tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               ('FONTSIZE',(0,0),(-1,-1),5.5),
                               ('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(-1,-1),1,colors.black)])
        tblStyle.add('BACKGROUND',(0,0),(-1,0),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
        tableThatSplitsOverPages.setStyle(tblStyle)
        Story.append(tableThatSplitsOverPages)
        
        doc.build(Story,onFirstPage=relatorios.addPageNumber, onLaterPages=relatorios.addPageNumber)
        
      


    def relatorioOpcao2(name, cpf, placa, dataInicial, dataFinal, table):

        '''
        Report of Option two. This has data between periods.
        This produce graph.
        '''
        
        if os.path.isdir(os.getcwd() + '/report/' + str(cpf)):
            rep = os.getcwd() + '/report/' + str(cpf) + str('/reportOption2.pdf')
        else: 
            os.makedirs(os.getcwd() + '/report/' + str(cpf))
            rep = os.getcwd() + '/report/' + str(cpf) + str('/reportOption2.pdf')
            
        doc = SimpleDocTemplate(rep,pagesize=(A4),
                                rightMargin=30,leftMargin=30,
                                topMargin=30,bottomMargin=30)


        styles=getSampleStyleSheet()

        Story=[]
        logo = os.getcwd() + '/payload/' + str('logo.png')
        formatted_time = time.ctime()


        #### Página 1 ######################################################################
        cabecalho = ["SECRETARIA DE POLÍCIA CIVIL", 
                     "SUBSECRETARIA DE INTELIGÊNCIA",
                     "COORDENAÇÃO DE P&D"]

        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
        ptext = '<font size="24">RELATÓRIO</font>'
        Story.append(Paragraph(ptext, styles["Center"]))
        Story.append(Spacer(1, 60))

        im = Image(logo, 50*mm, 50*mm)
        Story.append(im)

        Story.append(Spacer(1, 60))


        for part in cabecalho:
            ptext = '<font size="16">%s</font>' % part.strip()
            Story.append(Paragraph(ptext, styles["Center"])) 
            Story.append(Spacer(1, 12))

        Story.append(Spacer(1, 144))

        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        ptext = '<font size="12"> emitido: %s</font>' % formatted_time

        Story.append(Paragraph(ptext, styles["Normal"]))

        ptext = '<font size="12">Para: %s</font>' % name
        Story.append(Paragraph(ptext, styles["Normal"]))  

        Story.append(PageBreak())


        #### Página 2 ######################################################################


        im = Image(logo, 20*mm, 20*mm)
        im.hAlign = 'LEFT'
        Story.append(im)
        Story.append(Spacer(1, 48))

        ptext = '<font size="12">Olá senhor %s</font>' %(name)
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        ptext = '<font size="12">Este relatório foi produzido seguindo os seguintes parâmetros de pesquisa:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        ptext = '<font size="12">Placa: %s</font>'%(placa)
        Story.append(Paragraph(ptext, styles["Justify"]))

        ptext = '<font size="12">Período: De %s até %s</font>'%(dataInicial, dataFinal)
        Story.append(Paragraph(ptext, styles["Justify"]))

        Story.append(Spacer(1, 48))

        graf = os.getcwd() + '/graph/' + str(cpf) + str('/graficos.png')
         
        im = Image(graf, 180*mm, 155*mm)
        Story.append(im)

        Story.append(PageBreak())

        #### Tabela #########################################################################


        #Story.append(landscape(A4))

        styleN = styles["Normal"]
        # Make heading for each column and start data list
        column1Heading = "COLUMN ONE HEADING"
        column2Heading = "COLUMN TWO HEADING"
        # Assemble data for each column using simple loop to append it into data list
        data = [[column1Heading,column2Heading]]

        #for i in table:
        #    data.append([str(i),str(i)])

        data_ = table.drop(columns = ['idMovimento', 'Ano', 'Mes', 'Dia', 'Sem', 'Hora', 'Minuto', 'Segundo'])

        data = [data_.columns[:,].values.astype(str).tolist()] + data_.values.tolist()

        tableThatSplitsOverPages = Table(data, repeatRows=1)
        tableThatSplitsOverPages.hAlign = 'CENTER'
        tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               ('FONTSIZE',(0,0),(-1,-1),5.5),
                               ('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(-1,-1),1,colors.black),
                               ('BOX',(0,0),(-1,-1),1,colors.black)])
        tblStyle.add('BACKGROUND',(0,0),(-1,0),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
        tableThatSplitsOverPages.setStyle(tblStyle)
        Story.append(tableThatSplitsOverPages)
        
        doc.build(Story,onFirstPage=relatorios.addPageNumber, onLaterPages=relatorios.addPageNumber)