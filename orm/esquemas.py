from pydantic import BaseModel

#definimos el esquema usuario
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str
#definimos el esquema calificaciones
class CalificacionBase(BaseModel):
    uea:str
    calificacion:str
#definimos el esquema fotos
class FotosBase(BaseModel):
    titulo:str
    descripcion:str
    ruta:str