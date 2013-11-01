#*-* coding: utf-8 *-*

db.define_table('lugares',
                Field('evento'),
                Field('lugar'),
                Field('capacidad')
)

db.define_table('fechaCharlas',
                Field('presentacion', db.presentaciones),
                Field('fecha', 'date')
)

db.define_table('fechaTalleres',
                Field('taller', db.talleres),
                Field('fechas')
)

db.define_table('locacionCharlas',
                Field('presentacion', db.presentaciones),
                Field('lugar')
)