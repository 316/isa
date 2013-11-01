#*-* coding: utf-8 *-*

db.define_table('disertantes',
                Field('nombre'),
                Field('apellido'),
                Field('dni'),
                Field('empresa'),
                Field('curriculum','text'),
                Field('imagen','upload'),
                format = '%(apellido)s, %(nombre)s: %(empresa)s'
)

db.define_table('presentaciones',
                Field('evento', db.eventos, default=request.vars.id, writable=False,readable=False),
                Field('titulo'),
                Field('duracion'),
                Field('resumen','text'),
                Field('nivel', requires=IS_IN_SET(NIVEL)),
                Field('detalle','text'),
                format = '%(titulo)s: %(evento)s'
)

db.define_table('talleres',
                Field('evento', db.eventos, default=request.vars.id, writable=False,readable=False),
                Field('titulo'),
                Field('duracion', 'integer', comment='Total horas'),
                Field('resumen','text'),
                Field('nivel'),
                Field('detalle', 'text'),
                Field('costo'),
                Field('cupo'),
                Field('archivo','upload'),
                format = '%(titulo): %(evento)s'
)

db.define_table('expositores',
                Field('presentacion', db.presentaciones),
                Field('expositor', db.disertantes),
)

db.define_table('instructores',
                Field('taller', db.presentaciones),
                Field('instructor', db.disertantes),
)

db.define_table('asistencia_talleres',
                Field('taller',db.talleres),
                Field('asistente'),
)

db.define_table('instalaciones',
                Field('evento',db.eventos, default=request.vars.id, writable=False, readable=False),
                Field('usuario',db.auth_user, writable=False, readable=False),
                Field('dispositivo',requires=IS_IN_SET(DISPOSITIVOS)),
                Field('so', requires=IS_IN_SET(SO), label='Sistema operativo'),
                Field('comentarios','text')
)