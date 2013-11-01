# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite')

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

auth.settings.extra_fields['auth_user']= [
    Field('trato', requires=IS_IN_SET(TRATO),comment='Requerido para imprimir el certificado'),
    Field('occupation', requires=IS_IN_SET(OCUPACION)),
    Field('entidad'),
    Field('ciudad', default='Salta', requires=IS_IN_SET(PROVINCIA)),
    Field('tdoc',requires=IS_IN_SET(TIPO_DOCUMENTO),comment='Requerido para imprimir el certificado',label='Tipo de documento'),
    Field('dni','integer',comment='Requerido para imprimir el certificado',label='Número de documento'),]


## create all tables needed by auth if not custom tables
auth.define_tables()

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# from gluon.contrib.login_methods.rpx_account import RPXAccount
# auth.settings.actions_disabled=['register','change_password','request_reset_password']
# auth.settings.login_form = RPXAccount(request,
#         api_key='7347638d1c35067d094983c06d017c7869c45efa',
#         domain='isa',
#         url = "http://localhost:8000/%s/default/user/login" % request.application)

from plugin_ckeditor import CKEditor
ckeditor = CKEditor(db)
ckeditor.define_tables()
