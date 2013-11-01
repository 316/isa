#*-* coding: utf-8 *-*

###############################################################
# controladores administrativos de gestion general para ISA   #
###############################################################

from gluon.tools import Crud
crud = Crud(db)

#crear nuevo evento
@auth.requires_membership('managers')
def nuevoevento():
    form = SQLFORM(db.eventos)

    if form.process().accepted:

        db.categorias.insert(evento=form.vars.id, nombre='Organiza')
        #session.flash='funciona'
        session.flash='El evento ha sido registrado'
        redirect(URL('administracion','admeventos'))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor complete el formulario'

    return dict(form=form)

@auth.requires_membership('managers')
def editaevento():
<<<<<<< HEAD
    db.eventos.id.readable=False
    clave= int(request.vars.eid)
    form = SQLFORM(db.eventos, clave)
=======
    form = SQLFORM(db.eventos, request.args(0))
>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203

    if form.process().accepted:
        session.flash='El evento se ha actualizado correctamente'
        redirect(URL('administracion','admevento', vars=dict(eid=clave)))
    elif form.errors:
        response.flash='El formulario tiene errores, por favor revise los datos'
    else:
        response.flash='Puede editar el evento'
    return dict(form=form)

#Selecciona las categorias disponibles para los sponsors del evento
@auth.requires_membership('managers')
def vercategorias():

    return dict(categorias=db(db.categorias.evento==request.vars.id).select())

#agrega una nueva categoria al evento
@auth.requires_membership('managers')
def addcategoria():
    form = SQLFORM(db.categorias)
    if form.process().accepted:
        session.flash = 'La categoria se ha agregado'
        redirect(URL('administracion','admeventos'))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor agregue una nueva categoria'

    return dict(form=form)

#de aqui en adelante se pone feo


#muestra el menu de administracion de eventos, solo se muestran los que estan en curso
@auth.requires_membership('managers')
def admeventos():

    return dict(eventos=db(db.eventos.fecha_fin>=request.now).select())

#administracion de eventos individuales
@auth.requires_membership('managers')
def admevento():

    return dict(seleccionado=db(db.eventos.id==request.vars.eid).select())

#muestra el listado de asistentes de un evento
@auth.requires_membership('managers')
def admasistentes():
    query=db((db.asistentes.evento==request.vars.eid)&(db.auth_user.id==db.asistentes.asistente)).select()
    cuenta=db((db.asistentes.evento==request.vars.eid)&(db.auth_user.id==db.asistentes.asistente)).count()
    return dict(personas=query, cuenta=cuenta)

#muestra las presentaciones/ actividades, de un evento
@auth.requires_membership('managers')
def admpresentaciones():
    id=request.vars.id
<<<<<<< HEAD
#    return dict(presentaciones=db((db.presentaciones.evento==request.vars.id)&(db.presentaciones.id==db.expositores.presentacion)&(db.disertantes.id==db.expositores.expositor)).select(),llave=id)
    return dict(presentaciones=db(db.presentaciones.evento==request.vars.id).select(),llave=id)
    
=======
    return dict(presentaciones=db((db.presentaciones.evento==request.vars.id)&(db.presentaciones.disertante==db.disertantes.id)).select(),llave=id)

>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203
#agregar presentacion
@auth.requires_membership('managers')
def addpresentacion():
    form=SQLFORM(db.presentaciones)

    if form.process().accepted:
        session.flash = 'Actividad agregada'
        redirect(URL('administracion','admevento', vars=dict(eid=request.vars.id)))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Agregar nueva presentacion'

    return dict(form=form)

#listado de expositores para todos los eventos
@auth.requires_membership('managers')
def listexpositores():

    return dict(db().select(db.disertantes.ALL))

#agregar expositor para poder asignar a las actividades
@auth.requires_membership('managers')
def addexpositor():
    form=SQLFORM.grid(db.disertantes)

    # if form.process().accepted:
    #     session.flash = 'Se ha agregado el expositor'
    #     redirect(URL('administracion', 'admeventos'))
    # elif form.errors:
    #     response.flash = 'El formulario tiene errores'
    # else:
    #     response.flash = 'Agregar nuevo disertante'

    return dict(form=form)


#muestra los sponsors del evento
@auth.requires_membership('managers')
def versponsors():

    return dict(sponsors=db((db.categorias.evento==request.vars.id)&(db.sponsors.categoria==db.categorias.id)).select())

#modifica el sponsor
@auth.requires_membership('managers')
def modsponsor():
    #    form = crud.update(db.sponsors, request.args(0))
    form = SQLFORM(db.sponsors, request.args(0))
    if form.process().accepted:
        session.flash = 'El sponsor ha sido modificado'
        redirect(URL('administracion', 'admeventos'))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Puede modificar el formulario'

    return dict(modificar= form)

#primero hago se que elija la categoria para el sponsor, eso no se puede modificar, para hacerlo se debe eliminar y volver a crear el sponsor
@auth.requires_membership('managers')
def lscategorias():

    return dict(listado=db(db.categorias.evento==request.args(0)).select())

#edicion de categorias
@auth.requires_membership('managers')
def editcategoria():

    return dict(form=crud.update(db.categorias, request.args(0)))

#Tengo que buscar la forma de integrar bien el formulario con los elementos de db.categorias
@auth.requires_membership('managers')
def addsponsor():
    form = SQLFORM(db.sponsors)

    if form.process().accepted:
        session.flash = 'Se ha agregado el nuevo sponsor'
        redirect(URL('administracion','admeventos'))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Agregue un nuevo Sponsor al evento'

    return dict(form=form)

# #Impresion de certificados e identificaciones
# @auth.requires_membership('managers')
# def certificados():

#     return dict()

#@auth.requires_membership("admin") # uncomment to enable security
@auth.requires_membership('managers')
def admusers():

    btn = lambda row: A("Edit", _href=URL('admuser', args=row.auth_user.id))
    db.auth_user.edit = Field.Virtual(btn)
    rows = db(db.auth_user).select()
    headers = ["ID", "Name", "Last Name", "Email", "Edit"]
    fields = ['id', 'first_name', 'last_name', "email", "edit"]
    table = TABLE(THEAD(TR(*[B(header) for header in headers])),
                  TBODY(*[TR(*[TD(row[field]) for field in fields]) \
                          for row in rows]))
    table["_class"] = "table table-striped table-bordered table-condensed"
    return dict(table=table)

#@auth.requires_membership("admin") # uncomment to enable security
@auth.requires_membership('dios')
def admuser():

    user_id = request.args(0) or redirect(URL('list_users'))
    form = SQLFORM(db.auth_user, user_id)
    membership_panel = LOAD(request.controller,
                            'manage_membership.html',
                            args=[user_id],
                            ajax=True)
    return dict(form=form,membership_panel=membership_panel)

#@auth.requires_membership("admin") # uncomment to enable security
@auth.requires_membership('managers')
def manage_membership():
    user_id = request.args(0) or redirect(URL('list_users'))
    db.auth_membership.user_id.default = int(user_id)
    db.auth_membership.user_id.writable = False
    form = SQLFORM.grid(db.auth_membership.user_id == user_id,
                        args=[user_id],
                        searchable=False,
                        deletable=False,
                        details=False,
                        selectable=False,
                        csv=False)
    return form

@auth.requires_membership('managers')
def certificados():
    consulta=db((db.asistentes.evento==request.vars.eid)&(db.auth_user.id==db.asistentes.asistente)&(db.eventos.id==db.asistentes.evento)).select()
    return dict(datos=consulta)

@auth.requires_membership('managers')
def certificado():
    consulta=db((db.asistentes.asistente==request.vars.uid)&(db.auth_user.id==request.vars.uid)&(db.asistentes.evento==request.vars.eid)&(db.eventos.id==request.vars.eid)&(db.asistentes.certificado==True)&(db.auth_user.dni!=None)).select()
    return dict(datos=consulta)

@auth.requires_membership('managers')
def admlugares():
    db.lugares.evento.default=request.vars.id
    db.lugares.evento.writable=False
    db.lugares.evento.readable=False
    form = SQLFORM(db.lugares)

    if form.process().accepted:
        session.flash='Agregado'
        redirect(URL('administracion','admevento', vars=dict(eid=request.vars.id)))
    elif form.errors:
        response.flash='Oops, something went wrong'

    return dict(form=form)
