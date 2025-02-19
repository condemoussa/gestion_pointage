# -*-coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class AtmCentrale(models.Model):
    _name = 'atm.centrale'
    _description = "Gestion de la centrale"
    _rename='name'


    def nettoyer_la_table_centrale(self):
        centrale = self.env["atm.centrale"].seach([])
        if centrale:
            centrale.unlink()


    name= fields.Char("Centrale")