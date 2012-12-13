# coding=utf-8

from Products.Archetypes.atapi import *
from archetypes.referencebrowserwidget import ReferenceBrowserWidget
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import event

from wres.policy.utils.utils import set_schemata_properties, finalizeSchema

from zope.i18nmessageid import MessageFactory, Message

from wres.brfields.content.BrFieldsAndWidgets import *
from wres.brfields.validators import *

from wres.archetypes.validators import *
from wres.archetypes.widgets.BuildingBlocksWidget import BuildingBlocksWidget

_ = MessageFactory("cmfuemr")

MAIN = Schema((

        ReferenceField('patient',
            required = 1,
            relationship='patient',
            allowed_types=('Patient',),
            validators = ('isValidReference',),
            widget=BuildingBlocksWidget(label='Paciente',
                                        blocks=({'id':'popup_search', 'value':_('Search'), 'search_template': 'popup_choose_patient'},
                                                {'id':'popup_quick_register', 'value':_('Quick Register'), 'extra_fields':('birthDate', 'homePhone', 'mobile'), 'location':'/Patients'}),
                                        helper_js=('buildingblockwidget.js',),
                                        ),
        ),        
        
        IntegerField('duration',
            required=1,
            widget=IntegerWidget(
                label=_('Duration'),
                description=_('Duration in minutes'),
            ),
        ),
               
        BrPhoneField('contactPhone',
            index=':schema',
            widget=BrPhoneWidget(label=_('Contact Phone'),
                                     description='You must enter only numbers',
                                     description_msgid='cmfuemr_help_contact_phone',
                                     i18n_domain='cmfuemr',
            ),
        ),        

        StringField('visit_type',
            required=True,
            default="1a Consulta",
            vocabulary = "getTypesOfVisit",
            widget = SelectionWidget(
                    label = 'Tipo de Visita',
            ),
        ),

        StringField('visit_reason',
            required=False,
            vocabulary = "getVisitReason",
            widget = SelectionWidget(
                    label = 'Razão da Visita',
                    macro_edit='generic_selection_edit_macro',
                    helper_js=('generic_selection_edit.js', ),             
            ),
        ),        
      
        StringField('insurance',
		required=False,
        vocabulary = "getInsurancesNames",
        widget = SelectionWidget(
                label = 'Plano de Saúde',
                macro_edit='insurance_selection_edit_macro',
                helper_js=('insurance_selection_edit.js', ),             
                ),
        ),
        #TODO: Remove comment (03/07/2012)
        #StringField('note',
            #widget=TextAreaWidget(label=_('Note'),
            #),
        #),                
        
))

set_schemata_properties(MAIN, schemata='default')

baseSchema = finalizeSchema(event.ATEventSchema.copy(), type='Visit')

VisitSchema = baseSchema + MAIN                       

# move os campos patient e doctor para a 1a e 2a posicao, respectivamente.
VisitSchema._moveFieldToPosition('patient', 1)
# VisitSchema._moveFieldToPosition('doctor', 2)
VisitSchema._moveFieldToPosition('startDate', 2)
VisitSchema._moveFieldToPosition('duration', 3)
