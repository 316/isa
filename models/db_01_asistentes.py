#*-* coding: utf-8 *-*

db.define_table('asistentes',
                Field('evento', db.eventos, default=request.vars.id, writable=False, readable=False),
                Field('asistente', db.auth_user, default=request.vars.per, writable=False, readable=False),
                Field('certificado', 'boolean'),
                Field('presente','boolean'),
                Field('pago','boolean'),
                Field('entregado','boolean'),
)
