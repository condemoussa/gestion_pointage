from odoo import models, fields
from datetime import datetime

class ViderCentrale(models.TransientModel):
    _name = 'vider.centrale'


    def vider_centrale(self):

        centrale = self.env["atm.centrale"].search([])
        centrale.unlink()
        pointage = self.env["atm.pointeuse"].search([])
        pointage.unlink()




