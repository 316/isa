#*-* coding: utf-8 *-*

def verificar():

    return dict()

def confirmar():
    evento=request.vars.eid

    form=SQLFORM.factory(Field('buscar', requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        if db(db.auth_user.email==form.vars.buscar):
            response.flash="El dni existe"
        elif db(db.auth_user.dni==form.vars.buscar):
            response.flash='Encontrado por email'
    else:
        response.flash='No existe el usuario'
    return dict(form=form)
