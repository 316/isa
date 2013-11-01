#*-* coding: utf-8 *-*

###############################################################
#Este archivo es parte de Isa, sistema de gestion de eventos  #
#basado en Sofi de cenditel (http://sofi.cenditel.ve), que    #
#originalmente fue escrito en django. Este archivo se puede   #
#usar, modificar y distribuir bajo las terminos de la licencia#
#GPL V3 o posterior.                                          #
###############################################################

import os

db.define_table('eventos',
                Field('nombre'),
                Field('descripcion','text'),
                Field('lugar'),
                Field('fecha_ini','date', label="Fecha de incio", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                Field('fecha_fin','date', label="Fecha fin de evento", requires = IS_DATE(format=('%d-%m-%Y'))),
                Field('cronograma','text'),
                Field('charlas','boolean'),
                Field('talleres','boolean'),
                Field('suscripciones','boolean'),
                Field('publicar','boolean'),
                Field('certificado','boolean'),
                Field('sponsors','boolean'),
                Field('personal','boolean'),
                Field('installfest','boolean'),
                Field('imagen','upload'),
                format ='%(id)s, %(nombre)s'
)

db.eventos.descripcion.widget=ckeditor.widget
db.eventos.cronograma.widget=ckeditor.widget

db.define_table('categorias',
                Field('evento', db.eventos, default=request.vars.id, writable=False, readable=False),
                Field('nombre'),
                format = '%(nombre)s'
)

db.define_table('organizadores',
                Field('evento', db.eventos),
                Field('nombre'),
                Field('apellido'),
                Field('dni'),
                format = '%(apellido)s, %(nombre)s: %(evento)s'
)

db.define_table('sponsors',
               Field('nombre'),
               Field('categoria', db.categorias, default=request.vars.id, writable=False, readable=False),
               Field('imagen','upload',uploadfolder=os.path.join(request.folder,'upload'), autodelete=False),
               Field('contacto'),
               Field('enlace'),
               format = '%(nombre)s'
)

db.define_table('comentarios',
                Field('evento', db.eventos, default=request.vars.id, writable=False, readable=False),
                Field('nombre', db.auth_user, writable=False, readable=False),
<<<<<<< HEAD:models/db_00_eventos.py
                Field('comentario','text'),
                Field('fecha','datetime', default=request.now, writable=False, readable=False)
)

db.define_table('feedback',
                Field('evento', db.eventos, default=request.vars.id, writable=False, readable=False),
                Field('nombre', db.auth_user, writable=False, readable=False),
=======
>>>>>>> 612adb71e592a1ca63bea09ff93657458ad31203:models/db_tablas.py
                Field('comentario','text'),
                Field('fecha','datetime', default=request.now, writable=False, readable=False)
)

db.define_table('fotos',
                Field('evento', db.eventos),
                Field('titulo'),
                Field('descripcion','text'),
                Field('imagen', 'upload')
)
