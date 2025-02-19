from odoo import models, fields
from datetime import datetime

class WizardPointeuse(models.TransientModel):
    _name = 'wizard.pointeuse'

    # Champs par défaut
    mois = fields.Char(string="Mois", default=lambda self: datetime.now().strftime('%m'))
    annee = fields.Char(string="Année", default=lambda self: str(datetime.now().year))
   # centrale_id = fields.Many2one("atm.centrale" ,"centrales")

    def action_pointeuse(self):
        lines = []
        lines2= []
        lines3 = []
        lines4 = []
        lines5 = []
        lines6 = []
        lines7 = []
        lines8 = []
        lines9 = []
        lines10= []
        lines11 = []
        lines12 = []
        lines13 = []
        lines14 = []
        lines15 = []
        lines16 = []
        lines17 = []
        lines18 = []
        lines19 = []
        lines20 = []
        lines21 = []
        lines22 = []
        lines23 = []
        lines24 = []
        lines25 = []
        lines26 = []
        lines27 = []
        lines28 = []
        lines29 = []
        lines30 = []
        lines31 = []

        pointeuse = self.env["atm.pointeuse"].search([("ref","=",'m1'),("mois","=",self.mois),("annee","=",self.annee)])
        pointeuse2 = self.env["atm.pointeuse"].search([('ref', '=','m2'),("mois","=",self.mois),("annee","=",self.annee)])
        pointeuse3 = self.env["atm.pointeuse"].search(  [('ref', '=', 'm3'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse4 = self.env["atm.pointeuse"].search([('ref', '=', 'm4'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse5 = self.env["atm.pointeuse"].search([('ref', '=', 'm5'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse6= self.env["atm.pointeuse"].search([("ref", "=", 'm6'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse7 = self.env["atm.pointeuse"].search([('ref', '=', 'm7'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse8 = self.env["atm.pointeuse"].search([('ref', '=', 'm8'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse9 = self.env["atm.pointeuse"].search([('ref', '=', 'm9'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse10 = self.env["atm.pointeuse"].search([('ref', '=', 'm10'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse11= self.env["atm.pointeuse"].search([("ref", "=", 'm11'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse12= self.env["atm.pointeuse"].search([('ref', '=', 'm12'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse13= self.env["atm.pointeuse"].search([('ref', '=', 'm13'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse14= self.env["atm.pointeuse"].search([('ref', '=', 'm14'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse15= self.env["atm.pointeuse"].search([('ref', '=', 'm15'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse16 = self.env["atm.pointeuse"].search([("ref", "=", 'm16'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse17 = self.env["atm.pointeuse"].search([('ref', '=', 'm17'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse18 = self.env["atm.pointeuse"].search([('ref', '=', 'm18'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse19 = self.env["atm.pointeuse"].search([('ref', '=', 'm19'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse20= self.env["atm.pointeuse"].search([('ref', '=', 'm20'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse21 = self.env["atm.pointeuse"].search([("ref", "=", 'm21'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse22 = self.env["atm.pointeuse"].search( [('ref', '=', 'm22'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse23 = self.env["atm.pointeuse"].search( [('ref', '=', 'm23'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse24 = self.env["atm.pointeuse"].search([('ref', '=', 'm24'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse25= self.env["atm.pointeuse"].search([('ref', '=', 'm25'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse26 = self.env["atm.pointeuse"].search([("ref", "=", 'm26'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse27 = self.env["atm.pointeuse"].search([('ref', '=', 'm27'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse28 = self.env["atm.pointeuse"].search([('ref', '=', 'm28'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse29 = self.env["atm.pointeuse"].search([('ref', '=', 'm29'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse30 = self.env["atm.pointeuse"].search([('ref', '=', 'm30'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse31 = self.env["atm.pointeuse"].search([('ref', '=', 'm31'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        for line in pointeuse:
            vals = {
                'name': line.centrale.name,
                'valeur1':  1 if line.val1 == 'OK' else 0
            }
            lines.append(vals)

        for line in pointeuse2:
            vals = {'valeur1':   1 if line.val1 == 'OK' else 0 }
            lines2.append(vals)

        for line in pointeuse3:
            vals = { 'valeur1':1 if line.val1 == 'OK' else 0,  }
            lines3.append(vals)

        for line in pointeuse4:
            vals = { 'valeur1': 1 if line.val1 == 'OK' else 0 }
            lines4.append(vals)

        for line in pointeuse5:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines5.append(vals)

        for line in pointeuse6:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines6.append(vals)

        for line in pointeuse7:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines7.append(vals)

        for line in pointeuse8:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines8.append(vals)

        for line in pointeuse9:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines9.append(vals)

        for line in pointeuse10:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines10.append(vals)

        for line in pointeuse11:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines11.append(vals)

        for line in pointeuse12:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines12.append(vals)

        for line in pointeuse13:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines13.append(vals)

        for line in pointeuse14:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines14.append(vals)

        for line in pointeuse15:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines15.append(vals)

        for line in pointeuse16:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines16.append(vals)

        for line in pointeuse17:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines17.append(vals)

        for line in pointeuse18:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines18.append(vals)

        for line in pointeuse19:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines19.append(vals)

        for line in pointeuse20:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines20.append(vals)

        for line in pointeuse21:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines21.append(vals)

        for line in pointeuse22:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines22.append(vals)

        for line in pointeuse23:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines23.append(vals)

        for line in pointeuse24:
            vals = {'valeur1': 1 if line.val1 == 'ok' else 0}
            lines24.append(vals)

        for line in pointeuse25:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines25.append(vals)

        for line in pointeuse26:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines26.append(vals)

        for line in pointeuse27:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines27.append(vals)

        for line in pointeuse28:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines28.append(vals)

        for line in pointeuse29:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines29.append(vals)

        for line in pointeuse30:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines30.append(vals)

        for line in pointeuse31:
            vals = {'valeur1': 1 if line.val1 == 'OK' else 0}
            lines31.append(vals)




        # Inclure les champs mois et annee dans les données envoyées au rapport
        data = {
            'form_date': self.read()[0],
            'line_data': lines,
            'data2': lines2,
            'data3': lines3,
            'data4': lines4,
            'data5': lines5,
            'data6': lines6,
            'data7': lines7,
            'data8': lines8,
            'data9': lines9,
            'data10': lines10,
            'data11': lines11,
            'data12': lines12,
            'data13': lines13,
            'data14': lines14,
            'data15': lines15,
            'data16': lines16,
            'data17': lines17,
            'data18': lines18,
            'data19': lines19,
            'data20': lines20,
            'data21': lines21,
            'data22': lines22,
            'data23': lines23,
            'data24': lines24,
            'data25': lines25,
            'data26': lines26,
            'data27': lines27,
            'data28': lines28,
            'data29': lines29,
            'data30': lines30,
            'data31': lines31,
            'mois': self.mois,  # Mois par défaut
            'annee': self.annee  # Année par défaut
        }
        print(data["line_data"])
        return self.env.ref('gestion_pointage.action_pointeuse_xlsx').report_action(self, data=data)
