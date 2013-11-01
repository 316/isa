#*-* coding: utf-8 *-*

def disertantes():
    db.expositores.presentacion.default=request.vars.id
    db.expositores.presentacion.readable=False
    db.expositores.presentacion.writable=False
    agregar=SQLFORM(db.expositores)
    if agregar.process().accepted:
        session.flash='hecho!'
    elif agregar.errors:
        session.flash='error!!'
    
    return dict(expositores=db((db.expositores.presentacion==request.vars.id)&(db.disertantes.id==db.expositores.expositor)).select(), agregar=agregar)