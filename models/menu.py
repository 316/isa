# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

<<<<<<< HEAD
response.title = 'Salta L.U.G.'
response.subtitle = T('eventos de la comunidad de usuarios de Software Libre de Salta')
=======
response.title = 'ISA'
response.subtitle = T('Sistema de gestion para multiples eventos')
>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'marco mansilla <marco@saltalug.org.ar>'
response.meta.description = 'sistema de gestion de multiples eventos basado en Sofi'
response.meta.keywords = 'web2py, python, framework, eventos, software libre, desarrollo, hacktivismo, saltalug'
response.meta.generator = 'Isa - Eventos'
response.meta.copyright = 'Copyright 2013'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Inicio'), False, URL('default','index'), [])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu+=[(SPAN('Eventos anteriores',_style='color:blue'),False, URL('gestion','eanteriores'))]
    
    if (auth.is_logged_in() and auth.has_membership('managers')):
        response.menu+=[(SPAN('Administracion de eventos',_style='color:blue'),False, URL('administracion','admeventos'))]
    if (auth.is_logged_in() and auth.has_membership('dios')):
        response.menu+=[(SPAN('Administracion de usuarios',_style='color:blue'),False, URL('administracion','admusers'))]
                       
    response.menu+=[(SPAN('about',_style='color:blue'),False, URL('default','about'))]
_()

