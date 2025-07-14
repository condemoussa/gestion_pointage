import base64
import io
from odoo import models
from datetime import datetime

class StatistiquePointeuse(models.AbstractModel):
    _name = 'report.gestion_pointage.statistiquea_pointeuse'
    _inherit = 'report.report_xlsx.abstract'



    def generate_xlsx_report(self, workbook, data, partners):
        # form_data=data['form_date']
        data_test = data['test12']
        data_payroll=data['line_data']
        data2 = data['data2']
        data3 = data['data3']
        data4 = data['data4']
        data5 = data['data5']
        data6 = data['data6']
        data7 = data['data7']
        data8 = data['data8']
        data9 = data['data9']
        data10 = data['data10']
        data11 = data['data11']
        data12 = data['data12']
        data13 = data['data13']
        data14 = data['data14']
        data15 = data['data15']

        data16 = data['data16']
        data17 = data['data17']
        data18 = data['data18']
        data19 = data['data19']
        data20 = data['data20']

        data21 = data['data21']
        data22 = data['data22']
        data23 = data['data23']
        data24 = data['data24']
        data25 = data['data25']

        data26 = data['data26']
        data27 = data['data27']
        data28 = data['data28']
        data29 = data['data29']
        data30 = data['data30']
        data31 = data['data31']

        sheet = workbook.add_worksheet('STATISTIQUE DE LA POINTEUSE')

        #styles de livre de paie
        header_format = workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size':16,'color':'blue'})
        header_format_titre = workbook.add_format(
            {'border': 2, 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 7})
        header_format11 = workbook.add_format(
            {'border': 1,'color':'blue', 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 13})
        header_taux = workbook.add_format(
            {'border': 2, 'bg_color': 'orange', 'color': 'black', 'align': 'center', 'valign': 'vcenter',
             'bold': 'TRUE', 'size': 10})
        header_numero_dossier = workbook.add_format(
            {'border':1, 'color': 'black', 'align': 'center', 'valign': 'vcenter',
              'size': 12})
        header_autres = workbook.add_format(
            {'border': 1, 'color': 'black', 'align': 'center', 'valign': 'vcenter',
              'size': 12})




        sheet.merge_range('J3:X3', "STATISTIQUE DE LA POINTEUSE DES CENTRALES", header_format)
        sheet.set_column('B:B', 18)
        sheet.set_column('C:C', 5)
        sheet.set_column('D:D', 5)
        sheet.set_column('E:E', 5)
        sheet.set_column('F:F', 5)
        sheet.set_column('G:G', 5)
        sheet.set_column('H:H', 5)
        sheet.set_column('I:I', 5)
        sheet.set_column('J:J', 5)
        sheet.set_column('K:K', 5)
        sheet.set_column('L:L', 5)
        sheet.set_column('M:M', 5)
        sheet.set_column('N:N', 5)
        sheet.set_column('O:O', 5)
        sheet.set_column('P:P', 5)
        sheet.set_column('Q:Q', 5)
        sheet.set_column('R:R', 5)
        sheet.set_column('S:S', 5)
        sheet.set_column('T:T', 5)
        sheet.set_column('U:U', 5)
        sheet.set_column('V:V', 5)
        sheet.set_column('W:W', 5)

        sheet.set_column('X:X', 5)
        sheet.set_column('Y:Y', 5)
        sheet.set_column('Z:Z', 5)
        sheet.set_column('AA:AA', 5)
        sheet.set_column('AB:AB', 5)
        sheet.set_column('AC:AC', 5)

        sheet.set_column('AD:AD', 5)
        sheet.set_column('AE:AE', 5)
        sheet.set_column('AF:AF', 5)
        sheet.set_column('AG:AG', 5)
        row=5
        col=1

        sheet.write(row, col, 'CENTRALES', header_format11)
        sheet.write(row, col + 1, '01', header_format11)
        sheet.write(row, col + 2, '02', header_format11)
        sheet.write(row, col + 3, '03', header_format11)
        sheet.write(row, col + 4, '04', header_format11)
        sheet.write(row, col + 5, '05', header_format11)
        sheet.write(row, col + 6, "06", header_format11)
        sheet.write(row, col + 7, "07", header_format11)
        sheet.write(row, col + 8, "08", header_format11)
        sheet.write(row, col + 9, "09", header_format11)
        sheet.write(row, col + 10, '10', header_format11)
        sheet.write(row, col + 11, '11', header_format11)
        sheet.write(row, col + 12, '12', header_format11)
        sheet.write(row, col + 13, '13', header_format11)
        sheet.write(row, col + 14, "14", header_format11)
        sheet.write(row, col + 15, "15", header_format11)
        sheet.write(row, col + 16, '16', header_format11)
        sheet.write(row, col + 17, '17', header_format11)
        sheet.write(row, col + 18, '18', header_format11)
        sheet.write(row, col + 19, '19', header_format11)
        sheet.write(row, col + 20, '20', header_format11)
        sheet.write(row, col + 21, '21', header_format11)
        sheet.write(row, col + 22, "22", header_format11)
        sheet.write(row, col + 23, '23', header_format11)
        sheet.write(row, col + 24, '24', header_format11)
        sheet.write(row, col + 25, '25', header_format11)
        sheet.write(row, col + 26, '26', header_format11)
        sheet.write(row, col + 27, '27', header_format11)
        sheet.write(row, col + 28, '28', header_format11)
        sheet.write(row, col + 29, '29', header_format11)
        sheet.write(row, col + 30, '30', header_format11)
        sheet.write(row, col + 31, '31', header_format11)
        sheet.write(row, col + 32, 'TAUX', header_format11)
        row+=1

        # Combiner les deux boucles sur une même ligne
        for i in range(max(len(data_payroll), len(data2), len(data3), len(data4), len(data5), len(data6), len(data7), len(data8), len(data9), len(data10), len(data12), len(data13), len(data14), len(data15),len(data16),len(data17),len(data18),len(data19),len(data20),len(data21),len(data22),len(data23),len(data24),len(data25),len(data26),len(data27),len(data28),len(data29),len(data30),len(data31))):
            col = 1  # Réinitialiser la colonne au début de chaque ligne

            # Initialisation de total_pointuse
            total_pointuse = 0

            if i < len(data_payroll):  # Ajouter les données de data_payroll
                total_pointuse += data_payroll[i]['valeur1']
                sheet.write(row, col, data_payroll[i]['name'], header_numero_dossier)

                if data_payroll[i]['valeur1'] == 1 :
                    background1 = workbook.add_format({'bg_color': 'green', 'align': 'center','valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 1, data_payroll[i]['valeur1'], background1)
                else:
                    background1 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 1, data_payroll[i]['valeur1'], background1)



            if i < len(data2):  # Ajouter les données de data2
                total_pointuse += data2[i]['valeur1']
                if data2[i]['valeur1'] == 1 :
                    if data2[i]['valeur1'] == 1:
                        background2 = workbook.add_format({'bg_color': 'green', 'align': 'center','valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                        sheet.write(row, col + 2, data2[i]['valeur1'],background2 )
                else :
                    background2 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 2, data2[i]['valeur1'], background2)





            if i < len(data3):  # Ajouter les données de data3
                total_pointuse += data3[i]['valeur1']
                if data3[i]['valeur1'] == 1:
                    background3 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})

                    sheet.write(row, col + 3, data3[i]['valeur1'],background3 )
                else :
                    background3 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})

                    sheet.write(row, col + 3, data3[i]['valeur1'], background3)



            if i < len(data4):  # Ajouter les données de data2
                total_pointuse += data4[i]['valeur1']
                if data4[i]['valeur1']==1:
                    background4 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 4, data4[i]['valeur1'],background4 )
                else:
                    background4 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 4, data4[i]['valeur1'], background4)


            if i < len(data5):  # Ajouter les données de data2
                total_pointuse += data5[i]['valeur1']
                if data5[i]['valeur1'] == 1 :
                    background5 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 5, data5[i]['valeur1'], background5)
                else :
                    background5 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 5, data5[i]['valeur1'], background5)




            if i < len(data6):  # Ajouter les données de data2
                total_pointuse += data6[i]['valeur1']
                if data6[i]['valeur1']==1:
                    background6 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 6, data6[i]['valeur1'], background6)
                else:
                    background6 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 6, data6[i]['valeur1'], background6)


            if i < len(data7):  # Ajouter les données de data2
                total_pointuse += data7[i]['valeur1']
                if data7[i]['valeur1'] ==1 :
                    background7 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 7, data7[i]['valeur1'],background7 )
                else :
                    background7 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 7, data7[i]['valeur1'],background7 )


            if i < len(data8):  # Ajouter les données de data2

                total_pointuse += data8[i]['valeur1']
                if data8[i]['valeur1']==1 :
                    background8 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 8, data8[i]['valeur1'],background8)
                else :
                    background8 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 8, data8[i]['valeur1'],background8 )


            if i < len(data9):  # Ajouter les données de data2
                total_pointuse += data9[i]['valeur1']
                if data9[i]['valeur1']==1:
                    background9 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 9, data9[i]['valeur1'], background9)
                else :
                    background9 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 9, data9[i]['valeur1'], background9)


            if i < len(data10):  # Ajouter les données de data2
                total_pointuse += data10[i]['valeur1']
                if data10[i]['valeur1']==1:
                    background10 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 10, data10[i]['valeur1'],background10 )
                else :
                    background10 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 10, data10[i]['valeur1'],background10 )

            if i < len(data11):  # Ajouter les données de data2
                total_pointuse += data11[i]['valeur1']
                if data11[i]['valeur1']==1:
                    background11 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 11, data11[i]['valeur1'],background11 )
                else :
                    background11 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 11, data11[i]['valeur1'],background11 )

            if i < len(data12):  # Ajouter les données de data2
                total_pointuse += data12[i]['valeur1']
                if data12[i]['valeur1']==1 :
                    background12 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 12, data12[i]['valeur1'],background12 )
                else :
                    background12 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 12, data12[i]['valeur1'],background12 )

            if i < len(data13):  # Ajouter les données de data2
                total_pointuse += data13[i]['valeur1']
                if data13[i]['valeur1'] ==1:
                    background13 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 13, data13[i]['valeur1'],background13 )
                else:
                    background13 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 13, data13[i]['valeur1'],background13 )

            if i < len(data14):  # Ajouter les données de data2
                total_pointuse += data14[i]['valeur1']
                if data14[i]['valeur1']==1:
                    background14 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 14, data14[i]['valeur1'],background14 )
                else:
                    background14 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 14, data14[i]['valeur1'],background14 )

            if i < len(data15):  # Ajouter les données de data2
                total_pointuse += data15[i]['valeur1']
                if data15[i]['valeur1']==1 :
                    background15 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 15, data15[i]['valeur1'],background15 )
                else:
                    background15 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 15, data15[i]['valeur1'], background15)

            if i < len(data16):  # Ajouter les données de data2
                total_pointuse += data16[i]['valeur1']
                if data16[i]['valeur1']==1:
                    background16 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 16, data16[i]['valeur1'],background16 )
                else :
                    background16 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 16, data16[i]['valeur1'], background16)

            if i < len(data17):  # Ajouter les données de data2
                total_pointuse += data17[i]['valeur1']
                if data17[i]['valeur1']==1:
                    background17 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 17, data17[i]['valeur1'], background17)
                else :
                    background17 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 17, data17[i]['valeur1'], background17)

            if i < len(data18):  # Ajouter les données de data2
                total_pointuse += data18[i]['valeur1']
                if data18[i]['valeur1']==1:
                    background18 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 18, data18[i]['valeur1'],background18 )
                else:
                    background18 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 18, data18[i]['valeur1'],background18 )

            if i < len(data19):  # Ajouter les données de data2
                total_pointuse += data19[i]['valeur1']
                if data19[i]['valeur1']==1:
                    background19 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 19, data19[i]['valeur1'],background19 )
                else :
                    background19 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 19, data19[i]['valeur1'], background19)

            if i < len(data20):  # Ajouter les données de data2
                total_pointuse += data20[i]['valeur1']
                if data20[i]['valeur1']==1:
                    background20 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 20, data20[i]['valeur1'],background20 )
                else:
                    background20 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',   'border': '1'})
                    sheet.write(row, col + 20, data20[i]['valeur1'], background20)

            if i < len(data21):  # Ajouter les données de data2
                total_pointuse += data21[i]['valeur1']
                if data21[i]['valeur1']==1:
                    background21 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 21, data21[i]['valeur1'],background21 )
                else :
                    background21 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 21, data21[i]['valeur1'], background21)

            if i < len(data22):  # Ajouter les données de data2
                total_pointuse += data22[i]['valeur1']
                if data22[i]['valeur1']==1:
                    background22= workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 22, data22[i]['valeur1'], background22)
                else :
                    background22 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 22, data22[i]['valeur1'],background22 )

            if i < len(data23):  # Ajouter les données de data2
                total_pointuse += data23[i]['valeur1']
                if data23[i]['valeur1']==1:
                    background23 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',   'border': '1'})
                    sheet.write(row, col + 23, data23[i]['valeur1'], background23)
                else :
                    background23 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 23, data23[i]['valeur1'], background23)

            if i < len(data24):  # Ajouter les données de data2
                total_pointuse += data24[i]['valeur1']
                if data24[i]['valeur1']==1:
                    background24 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 24, data24[i]['valeur1'], background24)
                else:
                    background24 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 24, data24[i]['valeur1'],background24 )

            if i < len(data25):  # Ajouter les données de data2
                total_pointuse += data25[i]['valeur1']
                if data25[i]['valeur1']==1:
                    background25 = workbook.add_format( {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 25, data25[i]['valeur1'], background25)
                else :
                    background25 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 25, data25[i]['valeur1'],background25 )

            if i < len(data26):  # Ajouter les données de data2
                total_pointuse += data26[i]['valeur1']
                if data26[i]['valeur1']==1 :
                    background26 = workbook.add_format(  {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',     'border': '1'})
                    sheet.write(row, col + 26, data26[i]['valeur1'],background26 )
                else :
                    background26 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 26, data26[i]['valeur1'], background26)

            if i < len(data27):  # Ajouter les données de data2
                total_pointuse += data27[i]['valeur1']
                if data27[i]['valeur1']==1:
                    background27 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 27, data27[i]['valeur1'], background27)
                else :
                    background27 = workbook.add_format(   {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 27, data27[i]['valeur1'], background27)

            if i < len(data28):  # Ajouter les données de data2
                total_pointuse += data28[i]['valeur1']
                if data28[i]['valeur1']==1:
                    background28 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 28, data28[i]['valeur1'],background28 )
                else :
                    background28 = workbook.add_format( {'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 28, data28[i]['valeur1'],background28 )

            if i < len(data29):  # Ajouter les données de data2
                total_pointuse += data29[i]['valeur1']
                if data29[i]['valeur1']==1 :
                    background29 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 29, data29[i]['valeur1'], background29)
                else :
                    background29 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 29, data29[i]['valeur1'],background29 )

            if i < len(data30):  # Ajouter les données de data2
                total_pointuse += data30[i]['valeur1']
                if data30[i]['valeur1']==1:
                    background30 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black',  'border': '1'})
                    sheet.write(row, col + 30, data30[i]['valeur1'], background30)
                else :
                    background30 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black','border': '1'})
                    sheet.write(row, col + 30, data30[i]['valeur1'], background30)

            if i < len(data31):  # Ajouter les données de data2
                total_pointuse += data31[i]['valeur1']
                if data31[i]['valeur1']==1 :
                    background31 = workbook.add_format({'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 31, data31[i]['valeur1'], background31)
                else :
                    background31 = workbook.add_format({'bg_color': 'red', 'align': 'center', 'valign': 'vcenter', 'size': 8, 'color': 'black', 'border': '1'})
                    sheet.write(row, col + 31, data31[i]['valeur1'],background31 )



            percentage = (total_pointuse / 31) * 100

            sheet.write(row, col + 32, f"{percentage:.2f}%",header_autres)

            row += 1






