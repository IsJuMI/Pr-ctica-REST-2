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
    return sesion.query(modelos.Fotos).join(modelos.Alumnos).filter(modelos.Alumnos.id==id_al).first() #usamos join para combinar

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
    return sesion.query(modelos.Calificaciones).join(modelos.Alumnos).filter(modelos.Alumnos.id==id_al).first() #usamos join para combinar
