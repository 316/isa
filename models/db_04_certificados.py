#*-* coding: utf-8 *-*


db.define_table('certCharlas',
                Field('evento', db.eventos, default=request.vars.id, writable=False, readable=False),
                Field('asistente', db.auth_user, default=request.vars.per, writable=False, readable=False),
)

db.define_table('certTalleres',
                Field('taller', db.talleres),
                Field('asistente', db.auth_user)
)
