from odoo import models, fields;

class PaisModel(models.Model):
    _name = "pais_model"
    _description = "Modelo de país"
    
    name = fields.Char("Nombre")