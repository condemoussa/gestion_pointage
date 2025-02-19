# -*-coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class AtmPointeuse(models.Model):
    _name = 'atm.pointeuse'
    _description = "Gestion de la pointeuse"
    _rename='name'



    def create(self, val):
        res = super(AtmPointeuse, self).create(val)
        if res :
            reference = res.name[-2:]
            if reference =="01":
                res.update({"ref":"m1"})
            elif reference =="02":
                res.update({"ref": "m2"})
            elif  reference =="03":
                res.update({"ref": "m3"})
            elif  reference =="04":
                res.update({"ref": "m4"})
            elif  reference =="05":
                res.update({"ref": "m5"})
            elif reference == "06":
                res.update({"ref": "m6"})
            elif reference == "07":
                res.update({"ref": "m7"})
            elif reference == "08":
                res.update({"ref": "m8"})
            elif reference == "09":
                res.update({"ref": "m9"})
            elif reference == "10":
                res.update({"ref": "m10"})
            elif reference == "11":
                res.update({"ref": "m11"})
            elif reference == "12":
                res.update({"ref": "m12"})
            elif reference == "13":
                res.update({"ref": "m13"})
            elif reference == "14":
                res.update({"ref": "m14"})
            elif reference == "15":
                res.update({"ref": "m15"})
            elif reference == "16":
                res.update({"ref": "m16"})
            elif reference == "17":
                res.update({"ref": "m17"})
            elif reference == "18":
                res.update({"ref": "m18"})
            elif reference == "19":
                res.update({"ref": "m19"})
            elif reference == "20":
                res.update({"ref": "m20"})
            elif reference == "21":
                res.update({"ref": "m21"})
            elif reference == "22":
                res.update({"ref": "m22"})
            elif reference == "23":
                res.update({"ref": "m23"})
            elif reference == "24":
                res.update({"ref": "m24"})
            elif reference == "25":
                res.update({"ref": "m25"})
            elif reference == "26":
                res.update({"ref": "m26"})
            elif reference == "27":
                res.update({"ref": "m27"})
            elif reference == "28":
                res.update({"ref": "m28"})
            elif reference == "29":
                res.update({"ref": "m29"})
            elif reference == "30":
                res.update({"ref": "m30"})
            elif reference == "31":
                res.update({"ref": "m31"})

        return res




    name= fields.Char("Libelle de la pointeuse")
    val1 = fields.Selection([
        ("OK","OK"),
        ("KO", "KO")
    ],string="Valeur rélévé")
    ref = fields.Selection([
        ("m1","J1"),
        ("m2", "J2"),
        ("m3", "J3"),
        ("m4", "J4"),
        ("m5", "J5"),
        ("m6", "J6"),
        ("m7", "J7"),
        ("m8", "J8"),
        ("m9", "J9"),
        ("m10", "J10"),
        ("m11", "J11"),
        ("m12", "J12"),
        ("m13", "J13"),
        ("m14", "J14"),
        ("m15", "J15"),
        ("m16", "J16"),
        ("m17", "J17"),
        ("m18", "J18"),
        ("m19", "J19"),
        ("m20", "J20"),
        ("m21", "J21"),
        ("m22", "J22"),
        ("m23", "J23"),
        ("m24", "J24"),
        ("m25", "J25"),
        ("m26", "J26"),
        ("m27", "J27"),
        ("m28", "J28"),
        ("m29", "J29"),
        ("m30", "J30"),
        ("m31", "J31"),
    ] ,string="Référence")
    centrale = fields.Many2one("atm.centrale" ,"Centrale")
    mois = fields.Char(string="Mois", default=lambda self: datetime.now().strftime('%m'))
    annee = fields.Char(string="Année", default=lambda self: str(datetime.now().year))