from odoo import models, fields;

class InscripcionModel(models.Model):
    _name = "inscripcion_model"
    _description = "Modelo de inscripción"
    
    inscription_date = fields.Date("Fecha de inscripción")
    alumno_id = fields.Many2one("alumno_model", "Alumno")
    programa_id = fields.Many2one("programa_model", "Programa")