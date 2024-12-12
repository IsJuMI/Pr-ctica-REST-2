from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
import orm.esquemas as esquemas #importamos esquemas
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

# creación del servidor
app = FastAPI()

# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "Práctica ALUMNOS REST 2"
    }

    return respuesta

#se hizo para consultar todos los alumnos
@app.get("/alumnos")
def alumnos(sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumnos")
    return repo.alumnos(sesion)
#se hizo para consultar alumnos por id_al
@app.get("/alumnos/{id}")
def alumnos_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumnos por Id")
    return repo.alumnos_por_id(sesion, id)
#para borrar alumnos por id
@app.delete("/alumnos/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id(sesion,id)
    return{"usuario borrado","ok"}

#para actualizar los datos del alumno por id
@app.put("/alumnos/{id}")
def actualizar_alumno(id:int, info_alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    return repo.ctualizar_alumno(sesion,id, info_alumno)

#se hizo para consultar todas las fotos
@app.get("/fotos")
def fotos(sesion:Session=Depends(generador_sesion)):
    print("Api consultando todas las fotos")
    return repo.fotos(sesion)
#se hizo para consultar fotos por id_fo
@app.get("/fotos/{id}")
def fotos_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por  Id")
    return repo.fotos_por_id(sesion, id)

#se hizo para consultar fotos por id_al
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumnos(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por  Id_alumnos",id)
    return repo.fotos_por_id_alumno(sesion, id)

#para borrar fotos por id
@app.delete("/fotos/{id}")
def borrar_foto(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_foto_por_id(sesion,id)
    return{"foto borrada","ok"}

#para borrar fotos por id alumno
@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_id_alumnos(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion,id)
    return{"foto borrada","ok"}

#para actualizar los datos de la foto por id
@app.put("/fotos/{id}")
def actualizar_foto(id:int, info_foto:esquemas.FotosBase,sesion:Session=Depends(generador_sesion)):
    return repo.ctualizar_fotos(sesion,id, info_foto)




#para consultar todas las calificaciones
@app.get("/calificaciones")
def calificaciones(sesion:Session=Depends(generador_sesion)):
    print("Api consultando todas las calificaciones")
    return repo.calificaciones(sesion)

#se hizo para consultar calificaciones por id_ca
@app.get("/calificaciones/{id}")
def calificaciones_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por  Id")
    return repo.calificaciones_por_id(sesion, id)

#se hizo para consultar calificaciones por id_al
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por  Id_alumnos",id)
    return repo.calificaciones_por_id_alumno(sesion, id)

#para borrar calificaciones por id
@app.delete("/calificaciones/{id}")
def borrar_calificacion(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id(sesion,id)
    return{"calificacion borrada","ok"}
#para borrar calificaciones por id alumno
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_id_alumnos(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    return{"calificación borrada","ok"}

#para actualizar los datos de la calificacion por id
@app.put("/calificaciones/{id}")
def actualizar_calificaciones(id:int, info_calificacion:esquemas.CalificacionBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualizar_calificaciones(sesion,id, info_calificacion)

@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    print(alumno)
    return repo.guardar_alumno(sesion, alumno)

@app.post("/alumnos/{id}/calificaciones")
def guardar_calificacion(id:int, calificacion:esquemas.CalificacionBase,sesion:Session=Depends(generador_sesion)):
    print(calificacion)
    return repo.guardar_calificaciones_por_id_alumno(sesion, id,calificacion)

@app.post("/alumnos/{id}/fotos")
def guardar_fotos(id:int, foto:esquemas.FotosBase,sesion:Session=Depends(generador_sesion)):
    print(foto)
    return repo.guardar_fotos_por_id_alumno(sesion, id,foto)
