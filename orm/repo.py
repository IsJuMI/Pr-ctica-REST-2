import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_ 
#para lo de alumnos
#para consultar todos los alumnos
def alumnos(sesion:Session):
    print("select * from app.alumnos ")
    return sesion.query(modelos.Alumnos).all()

# select * from app.alumnos where id = id_al
def alumnos_por_id(sesion:Session,id_al:int):
    print("select * from app.alumnos where id = ", id_al)
    return sesion.query(modelos.Alumnos).filter(modelos.Alumnos.id==id_al).first()

#Delete '/alumnos/{id}'
# delete from app.alumno where id=id_al
def borra_alumno_por_id(sesion:Session, id_alumno:int):
    print("delete from app.alumno where id=", id_alumno)
    #1.-borrar fotos del alumno
    borrar_fotos_por_id_alumno(sesion,id_alumno)
    #2.-borrar calificaciones del alumno
    borrar_calificaciones_por_id_alumno(sesion,id_alumno)
    #3.- Select para verificar si existe el alumno
    alum=alumnos_por_id(sesion, id_alumno)
    #-Borramos 
    if alum is not None:
        #Borramos usuario
        sesion.delete(alum)
        #confirmar cambios
        sesion.commit()
    respuesta ={
        "mensaje": "usuario eliminado"
    }
    return respuesta


#Para hacer lo de fotos
#para consultar todos las fotos
def fotos(sesion:Session):
    print("select * from app.fotos ")
    return sesion.query(modelos.Fotos).all()

# para consultar select * from app.fotos where id = id_fo
def fotos_por_id(sesion:Session,id_fo:int):
    print("select * from app.fotos where id = ", id_fo)
    return sesion.query(modelos.Fotos).filter(modelos.Fotos.id==id_fo).first()

# para consultar select * from app.fotos where id = id_al
def fotos_por_id_alumno(sesion:Session,id_al:int):
    print("select * from app.fotos where id = ", id_al)
    return sesion.query(modelos.Fotos).filter(modelos.Fotos.id_alumno==id_al).all()#se usa all() para que muestre todos


#Delete '/fotos/{id}'
# delete from app.fotos where id=id_fo
def borra_foto_por_id(sesion:Session, id_fo:int):
    print("delete from app.foto where id=", id_fo)
    #2.- Select para verificar si existe la foto
    fot=fotos_por_id(sesion, id_fo)
    #-Borramos 
    if fot is not None:
        #Borramos foto
        sesion.delete(fot)
        #confirmar cambios
        sesion.commit()
    respuesta ={
        "mensaje": "foto elimiada"
    }
    return respuesta
#borrar fotos por id de alumno
#delete '/alumnos/{id}/fotos'
#delete from app.fotos where id_alumno=id
def borrar_fotos_por_id_alumno(sesion:Session, id_alumno:int):
    print("delete from app.fotos where id_alumno=",id_alumno)
    fotos_alum=fotos_por_id_alumno(sesion,id_alumno)
    if fotos_alum is not None:
        for fotos_alumno in fotos_alum:
            sesion.delete(fotos_alumno)
            sesion.commit()



#para hacer lo de calificaciones
#para consultar todos las calificaciones
def calificaciones(sesion:Session):
    print("select * from app.calificaciones ")
    return sesion.query(modelos.Calificaciones).all()

# para consultar select * from app.calificaciones where id = id_ca
#en la practica venia para hacer la consulta por id foto sin embargo dado a que no hay una relacion  supuso que la consulta era por id_ calificacion
def calificaciones_por_id(sesion:Session,id_ca:int):
    print("select * from app.calificaciones where id = ", id_ca)
    return sesion.query(modelos.Calificaciones).filter(modelos.Calificaciones.id==id_ca).first()


# para consultar select * from app.calificaciones where id = id_alumno
def calificaciones_por_id_alumno(sesion:Session,id_al:int):
    print("select * from app.calificaciones where id = ", id_al)
    return sesion.query(modelos.Calificaciones).filter(modelos.Calificaciones.id_alumno==id_al).all() #usamos nuevamente all()

#Delete '/calificaciones/{id}'
# delete from app.calificaciones where id=id_ca
def borra_calificaciones_por_id(sesion:Session, id_ca:int):
    print("delete from app.calificaciones where id=", id_ca)
    #2.- Select para verificar si existe la foto
    cali=calificaciones_por_id(sesion, id_ca)
    #-Borramos 
    if cali is not None:
        #Borramos foto
        sesion.delete(cali)
        #confirmar cambios
        sesion.commit()
    respuesta ={
        "mensaje": "calificacion elimiada"
    }
    return respuesta

#borrar calificaciones por id de alumno
#delete '/alumnos/{id}/calificaciones'
#delete from app.calificaciones where id_alumno=id
def borrar_calificaciones_por_id_alumno(sesion:Session, id_alumno:int):
    print("delete from app.calificaciones where id_alumno=",id_alumno)
    calificaciones_alum=calificaciones_por_id_alumno(sesion,id_alumno)
    if calificaciones_alum is not None:
        for calificaciones_alumno in calificaciones_alum:
            sesion.delete(calificaciones_alumno)
            sesion.commit()