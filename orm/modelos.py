# La clase base de las clases modelos
# los modelos o clases modelo son las clases que mapean a las tablas
from orm.config import BaseClass
# Importar de SQLALchemy los tipos de datos que usan las columnas de las tablas
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
# Para que calcular la hora actual
import datetime
# Por convención las clases tienen nombres en singular y comienzan con mayúsculas
class Alumnos(BaseClass):
    __tablename__="alumnos" #el nombre de la tabla es alumnos
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column("email",String(100))
    password=Column(String(100))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now)

class Calificaciones(BaseClass):
    __tablename__="calificaciones"#el nombre de la tabla es calificaciones
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumnos.id))
    uea=Column(String(100))
    calificacion=Column(String(100))

class Fotos(BaseClass):
    __tablename__="fotos"#el nombre de la tabla fotos
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumnos.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50))