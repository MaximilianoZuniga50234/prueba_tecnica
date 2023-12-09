from odoo import models, fields;

class AlumnoModel(models.Model):
    _name = "alumno_model"
    _description = "Modelo de alumno"
    
    name = fields.Char("Nombre")
    last_name = fields.Char("Apellido")
    birthday = fields.Date("Fecha_de_nacimiento")
    file = fields.Integer("Nro_de_legajo")
    email = fields.Char("Email")
    phone = fields.Char("Telefono")
    address = fields.Char("Direccion")
    country_id = fields.Many2one("pais_model","Pais")
