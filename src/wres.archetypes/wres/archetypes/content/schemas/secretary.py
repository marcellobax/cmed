# coding=utf-8

from Products.Archetypes.atapi import *
from wres.archetypes.content import wresuser
from wres.policy.utils.utils import set_schemata_properties, finalizeSchema
from wres.policy.utils.permissions import SET_CHART_ACCESS


from wres.brfields.content.BrFieldsAndWidgets import*
from wres.brfields.validators import *

from zope.i18nmessageid import MessageFactory

_ = MessageFactory("cmfuemr")

MAIN = Schema((

        BooleanField('isTranscriptionist', 
            read_permission=SET_CHART_ACCESS,
            write_permission=SET_CHART_ACCESS,
            widget = BooleanWidget(label=_(u'Transcritora?'),
                                   visible={'view': 'invisible'},
                                   description=_('Check if secretary will be able to transcript documents.'),
            ),
        ),
                                                                        
        StringField('firstName',
            required=1, 
            widget=StringWidget(label=_('First Name'),
            ),
        ),

        StringField('lastName',
            required=1, 
            widget=StringWidget(label=_('Last Name'),
            ),
        ),
            
        CPFField('ssn',
                required=0,
                searchable=1,
                widget=CPFWidget(label=_('SSN'),
                ),
        ),
        
        StringField('email',
            required=1,      
            validators = ('isEmail',),
            widget=StringWidget(label=_('Email'),
            ),
        ),         

        StringField('address1',
            widget=StringWidget(
                label=_('Address 1'),
            ),
        ),

        StringField('city',
            widget=StringWidget(
                label=_('City'),
            ),
        ),

        StringField('state',
            widget=StringWidget(
                label=_('State'),
            ),
        ),   

        BrPhoneField('phone',
            widget=BrPhoneWidget(label=_('Phone'),
                                 description='You must enter only numbers',
                                 description_msgid='cmfuemr_help_you_must_enter_only_numbers',
                                 i18n_domain='cmfuemr',
                             ),
            searchable=1,
            ),      

        BrPhoneField('cel',
            widget=BrPhoneWidget(label=_('Cel'),
                                     description='You must enter only numbers',
                                     description_msgid='cmfuemr_help_you_must_enter_only_numbers',
                                     i18n_domain='cmfuemr',
            ),
        ),                                                     
                                                                        
))
set_schemata_properties(MAIN, schemata='Principal')
        
PASSWORD = Schema((
         StringField('password',
            validators = ('isCurrentPassword',),
            widget=PasswordWidget(
                label='Senha Atual',
                condition='python:object.showPasswordCondition()',
            ),
        ),
         StringField('newPassword',
            required=False,
            widget=PasswordWidget(
                label='Nova Senha',
                macro_edit='cmed_password_widget',
            ),
        ),
         StringField('newPasswordConfirmation',
            required=False,
            widget=PasswordWidget(
                label='Confirmação da Senha',
                macro_edit='cmed_password_widget',
            ),
        ),
))
set_schemata_properties(PASSWORD, schemata='Senha')

baseSchema = finalizeSchema(wresuser.WRESUserSchema.copy())

SecretarySchema = baseSchema + MAIN + PASSWORD
