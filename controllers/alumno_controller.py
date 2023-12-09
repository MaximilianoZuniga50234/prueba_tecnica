from odoo import http
from odoo.http import request, Response
from datetime import date
import json

class Codificador(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

class Alumno_controller(http.Controller):
    @http.route('/get_a/<int:id>', auth='public', type="http")
    def obtenerAlumnosPorPrograma(self, id):
        
        todas_inscripciones = request.env['inscripcion_model'].search([("programa_id", "=", id)]);
        alumnosJson = []
        
        for ins in todas_inscripciones:
            alumno = ins.alumno_id;
            pais_temp = alumno.country_id;
            temporal = {
                "id": alumno.id,
                "nombre": alumno.name,
                "apellido": alumno.last_name,
                "legajo": alumno.file,
                "fecha_nacimiento": alumno.birthday,
                "email": alumno.email,
                "telefono": alumno.phone,
                "pais": {
                   "id": pais_temp.id,
                   "nombre": pais_temp.name
                }
           }
            alumnosJson.append(temporal);
            
        respuesta = json.dumps(alumnosJson, cls=Codificador);
            
        return Response(respuesta, content_type='application/json');