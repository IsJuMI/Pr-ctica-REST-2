import orm.modelos as modelos
import orm.esquemas as esquemas
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

#put '/alumnos/{id}'
def ctualizar_alumno(sesion:Session,id_alumno:int, alum_esquema:esquemas.AlumnoBase):
    #1.-verificamos si el alumno existe
    alum_bd =alumnos_por_id(sesion, id_alumno)
    if alum_bd is not None:
        #2.-actualizamos los datos del alumno
        alum_bd.nombre=alum_esquema.nombre
        alum_bd.edad=alum_esquema.edad
        alum_bd.domicilio=alum_esquema.domicilio
        alum_bd.carrera=alum_esquema.carrera
        alum_bd.trimestre=alum_esquema.trimestre
        alum_bd.email=alum_esquema.email
        alum_bd.password=alum_esquema.password
        #3.- Confirmamos los cambios
        sesion.commit()
        #4.-Refrecamos la base de datos
        sesion.refresh(alum_bd)
        #5.-Imprimir los nuevos datos
        print(alum_esquema)
        return alum_esquema
    else:
        respuesta={"mensaje: No existe el alumno"}
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

#put '/fotos/{id}'
def ctualizar_fotos(sesion:Session,id_foto:int, fo_esquema:esquemas.FotosBase):
    #1.-verificamos si la foto existe
    fo_bd =fotos_por_id(sesion, id_foto)
    if fo_bd is not None:
        #2.-actualizamos los datos de la foto
        fo_bd.titulo=fo_esquema.titulo
        fo_bd.descripcion=fo_esquema.descripcion
        fo_bd.ruta=fo_esquema.ruta
        #3.- Confirmamos los cambios
        sesion.commit()
        #4.-Refrecamos la base de datos
        sesion.refresh(fo_bd)
        #5.-Imprimir los nuevos datos
        print(fo_esquema)
        return fo_esquema
    else:
        respuesta={"mensaje: No existe la foto"}
        return respuesta


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


#put '/calificaciones/{id}'
def actualizar_calificaciones(sesion:Session,id_calificacion:int, cal_esquema:esquemas.CalificacionBase):
    #1.-verificamos si la calificacion existe, esto es importante
    cal_bd =calificaciones_por_id(sesion, id_calificacion)
    if cal_bd is not None:
        #2.-actualizamos los datos de la calificacion
        cal_bd.uea=cal_esquema.uea
        cal_bd.calificacion=cal_esquema.calificacion
        #3.-cofirmar cambios
        sesion.commit()
        #4.-Refrecar la base
        sesion.refresh(cal_bd)
        #5.-Imprimir los datos nuevos
        print(cal_esquema)
        return cal_esquema
    else:
        respuesta={"mensaje: No existe la calificacion"}
        return respuesta


#post '/alumno'
def guardar_alumno(sesion:Session, alu_nuevo:esquemas.AlumnoBase):
    #1.-un nuevo objeto de la clase modelo alumno
    alu_bd =modelos.Alumnos()
    #2.-llenamos el nuevo objeto
    alu_bd.nombre=alu_nuevo.nombre
    alu_bd.edad=alu_nuevo.edad
    alu_bd.domicilio=alu_nuevo.domicilio
    alu_bd.carrera=alu_nuevo.carrera
    alu_bd.trimestre=alu_nuevo.trimestre
    alu_bd.email=alu_nuevo.email
    alu_bd.password=alu_nuevo.password
    #3,- Insertar el objeto a la Base de datos
    sesion.add(alu_bd)
    #4,.Se confirma el cambio
    sesion.commit()
    #5.-Se hace un refresh
    sesion.refresh(alu_bd)
    return alu_bd

#post '/alumno/{id}/calificaciones'
def guardar_calificaciones_por_id_alumno(sesion:Session, id_alumno:int, cal_nueva:esquemas.CalificacionBase):
    #1.-tenemos que verificar que el alumno existe
    calificacion_bd =alumnos_por_id(sesion,id_alumno)
    #2.-si el alumno existe vamos ha hacer lo siguiente
    if calificacion_bd is not None:
            #3.-un nuevo objeto
            calificacion_bd =modelos.Calificaciones()
            #4.-llenamos el nuevo objeto
            calificacion_bd.id_alumno=id_alumno
            calificacion_bd.uea=cal_nueva.uea
            calificacion_bd.calificacion=cal_nueva.calificacion
           #5,- Insertar el objeto a la Base de datos
            sesion.add(calificacion_bd)
           #6,.Se confirma el cambio
            sesion.commit()
           #7.-Se hace un refresh
            sesion.refresh(calificacion_bd)
            return calificacion_bd
    #si el alumno no existe mostraremos el siguiente mensaje
    else:
            respuesta={"mensaje: No existe el alumno"}# no existe el alumno para guardar calificacion
            return respuesta

#post '/alumno/{id}/fotos'
def guardar_fotos_por_id_alumno(sesion:Session, id_alumno:int, fot_nueva:esquemas.FotosBase):
    #1.-tenemos que verificar que el alumno existe
    fotos_bd =alumnos_por_id(sesion,id_alumno)
    #2.-si el alumno existe vamos ha hacer lo siguiente
    if fotos_bd is not None:
            #3.-un nuevo objeto
            fotos_bd =modelos.Fotos()
            #4.-llenamos el nuevo objeto
            fotos_bd.id_alumno=id_alumno
            fotos_bd.titulo=fot_nueva.titulo
            fotos_bd.descripcion=fot_nueva.descripcion
            fotos_bd.ruta=fot_nueva.ruta
           #5.Insertar el objeto a la Base de datos
            sesion.add(fotos_bd)
           #6,.Se confirma el cambio
            sesion.commit()
           #7.-Se hace un refresh
            sesion.refresh(fotos_bd)
            return fotos_bd
    #si el alumno no existe mostraremos el siguiente mensaje
    else:
            respuesta={"mensaje: No existe el alumno"}# el alumno no existe para guardar calificacion
            return respuesta
