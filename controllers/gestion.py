# -*- coding: utf-8 -*-

###################################################
#controladores de gestion publica del evento
###################################################

from gluon.tools import Crud

crud=Crud(db)

#formulario para registro de asistentes
def asistentes():
    q=db((db.asistentes.asistente==request.vars.aid)&(db.asistentes.evento==request.vars.id)).select()
    if not(len(q)):
        db.asistentes.insert(evento=request.vars.id, asistente=request.vars.aid)
        session.flash = 'Usted se ha registrado exitosamente'
        redirect(URL('gestion', 'evento', vars=dict(id=request.vars.eid, sponsors=request.vars.esp)))
    else:
        session.flash = 'Usted ya estaba registrado en el evento'
        redirect(URL('default','index'))

    return dict()
#lista las presentaciones que haran durante el evento
def presentaciones():

    return dict(lista=db(db.presentaciones.evento==request.vars.id).select())

#selector para eventos anteriores, los separa de los proximos, se puede tener mas de un evento proximo en portada y lo mismo con los anteriores
def eanteriores():

    return dict(eventos=db(db.eventos.fecha_ini < request.now).select(orderby=db.eventos.fecha_ini))

#genera una suerte de pagina de evento que tiene las opciones para los asistenes y permite leer/escribir comentarios
@auth.requires_login()
def evento():
    if session.auth.user.id:
        db.comentarios.nombre.default=session.auth.user.id
<<<<<<< HEAD
        db.instalaciones.usuario.default=session.auth.user.id
=======
>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203
        comentar = SQLFORM(db.comentarios, _class='form form-horizontal')

        if comentar.process().accepted:
            response.flash = 'Gracias por su comentario'
        elif comentar.errors:
            response.flash = 'Por favor revise el formulario'
        else:
<<<<<<< HEAD
            response.flash = 'Detalles del evento'
=======
            response.flash = 'Aqui se muestran los detalles del evento seleccionado'
>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203
    
    queryuser=db((db.asistentes.evento==request.vars.id)&(db.asistentes.asistente==session.auth.user.id)).select()
    queryeventos = db(db.eventos.id==request.vars.id).select()
    querycategorias = db(db.categorias.evento==request.vars.id).select()
    querycomentarios = db((db.comentarios.evento==request.vars.id)&(db.comentarios.nombre==db.auth_user.id)).select(orderby=db.comentarios.fecha)
    querysponsors = db((db.sponsors.categoria==db.categorias.id) & (db.categorias.evento==request.vars.id)).select()
    installfest =SQLFORM(db.instalaciones)
    return dict(comentario=comentar, categorias=querycategorias, comentarios=querycomentarios, sponsors=querysponsors, evento=queryeventos, queryuser=queryuser, instalaciones=installfest)

def disertante():
    form= crud.read(db.disertantes, request.args[0])

    return dict(form=form)

def eventopreview():
    queryeventos = db(db.eventos.id==request.vars.id).select()
    querycategorias = db(db.categorias.evento==request.vars.id).select()
    querysponsors = db((db.sponsors.categoria==db.categorias.id) & (db.categorias.evento==request.vars.id)).select()
    return dict(categorias=querycategorias, sponsors=querysponsors, evento=queryeventos)
<<<<<<< HEAD

def certificado():
    if db(db.asistentes.id==request.vars.id).update(certificado='True'):
        redirect(URL('gestion', 'evento', vars=dict(id=request.vars.eid, sponsors=request.vars.esp)))
    return dict()
=======
>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203
