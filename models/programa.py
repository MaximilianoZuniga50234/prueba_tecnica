from odoo import models, fields;

class ProgramaModel(models.Model):
    _name = "programa_model"
    _description = "Modelo de programa"
    
    name = fields.Char("Nombre")
    description = fields.Char("Descripcion")