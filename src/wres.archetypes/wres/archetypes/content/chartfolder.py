# coding=utf8

"""Definition of the ChartFolder content type
"""

from DateTime import DateTime
from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from Products.CMFPlone.utils import _createObjectByType

from ComputedAttribute import ComputedAttribute

from wres.policy.utils.roles import MANAGER_ROLE, UEMRADMIN_ROLE, DOCTOR_ROLE, TRANSCRIPTIONIST_ROLE
# -*- Message Factory Imported Here -*-

from wres.archetypes.interfaces import IChartFolder
from wres.archetypes.config import PROJECTNAME
#from wres.archetypes.content.documentfolder import DocumentFolder

ChartFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

schemata.finalizeATCTSchema(
    ChartFolderSchema,
    folderish=True,
    moveDiscussion=False
)


def str2DateTime(date):
    """
    o Trasforma '31/01/2013' em um objetivo Datetime() correspondente.
    o Usado para ordenar chart datas. (vide listExams por exmeplo)
    """
    # trasforma "31/01/2013" em "01/31/2013", formato US, que é usado
    # pelo DateTime.
    date = date[3:6] + date[:3] + date[-4:]
    return DateTime(date)

class ChartFolder(folder.ATFolder):
    """Chart Folder of Patients"""
    implements(IChartFolder)

    meta_type = "ChartFolder"
    schema = ChartFolderSchema
    
#    def create_hidden_object(self, obj_id, title, type='UemrFolder',
#                             layout='documents_view', allowed_types=['Doc']):
#        obj = getattr(self, obj_id, None)
#        if obj is None:
#            _createObjectByType(type, self, obj_id, title=title)
#            obj = getattr(self, obj_id)
#        if layout != obj.getLayout():
#            obj.setLayout(layout)
#        if tuple(allowed_types) != tuple(obj.getLocallyAllowedTypes()):
#            from Products.CMFUEMR.compatibility import set_field_value
#            set_field_value(obj, 'enableConstrainMixin', True)
#            obj.setLocallyAllowedTypes(allowed_types)
#        if obj.title != title:
#            obj.title = title
#        return obj
    
    def create_hidden_object(self, obj_id, title, type):
        obj = getattr(self, obj_id, None)
        if obj is None:
            _createObjectByType(type, self, obj_id, title=title)
            obj = getattr(self, obj_id)
        return obj 
    
#    def at_post_create_script(self):
#        self.create_hidden_object('upload', 'Upload', 'Folder')

    def getPrescriptionsData(self):
        """
        o Retorna a lista de medicamentos ordenado pela data.
        o Usado no show_medications.cpt para mostra o histórico de prescrições.
        """

        def presc_cmp(presc1, presc2):
            """
            used for sorting exams by date.
            """
            date1 = str2DateTime(presc1["data"]["date"])
            date2 = str2DateTime(presc2["data"]["date"])
            if date1 < date2:
                return -1
            if date1 == date2:
                return 0
            else:
                return 1

        prescriptions = self.chart_data.get_entry('prescriptions')
        prescriptions = prescriptions.values()
        prescriptions.sort(cmp=presc_cmp)
        return prescriptions

    def listExams(self):
        """
        Retorna uma lista de exames (usado por show_exams e chart_summary).
        """

        def exam_cmp(exam1, exam2):
            """
            used for sorting exams by date.
            """
            date1 = str2DateTime(exam1["date"])
            date2 = str2DateTime(exam2["date"])
            if date1 < date2:
                return -1
            if date1 == date2:
                return 0
            else:
                return 1

        labs = self.chart_data.get_entry('laboratory').values()
        labs = [exam["data"] for exam in labs]
        labs.sort(cmp=exam_cmp)
        return labs

    def manage_afterAdd(self, item=None, container=None):
        """ Essa funcao e' chamada logo apos a adicao (addChartFolder) de um archetype """ 
        self.manage_permission('View', [MANAGER_ROLE, UEMRADMIN_ROLE, DOCTOR_ROLE, TRANSCRIPTIONIST_ROLE], acquire = False)
        self.create_hidden_object('documents', 'Consultas', 'DocumentFolder')
        self.documents.title = 'Consultas'
        self.documents.setLocallyAllowedTypes('GenericDocument')
        self.documents.setImmediatelyAddableTypes('GenericDocument')
        self.documents.setConstrainTypesMode(1)
        self.documents.reindexObject()

        self.create_hidden_object('impressos', 'Impressos', 'DocumentFolder')
        self.impressos.title = 'Impressos'
        self.impressos.setLocallyAllowedTypes('Impresso')
        self.impressos.setImmediatelyAddableTypes('Impresso')
        self.impressos.setConstrainTypesMode(1)
        self.impressos.reindexObject()        
            
        self.create_hidden_object('exams', 'Exames', 'UploadChartFolder')
        self.exams.title = 'Exames'               
                   
        self.create_hidden_object('upload', 'Documentos Externos', 'UploadChartFolder')
        self.upload.title = 'Documentos Externos'

    def printPrescriptionMedicationsData(self, pid):
        """
        o Calcula a largura da linha (conjunto de underscores) na prescrição.
        o Agrupa os medicamentos em Uso interno e externo.
        """
        prescription = self.chart_data.get_entry_item(pid, 'prescriptions')

        # calcula o valor da largura do maior campo concentração entre os
        # medicamentos da prescrição.
        max_quantity_len = 0
        for medication in prescription['data']['medications']:
            if len(medication['data']['quantity']) > max_quantity_len:
                max_quantity_len = len(medication['data']['quantity'])

        def undescore_len(medication):
            max_line_size = 65
            undescore_len = max_line_size - max_quantity_len
            undescore_len -= len(medication['data']['medication'])
            undescore_len -= len(medication['data']['concentration'])

            return undescore_len

        medications = {"externos": [], "internos": []}
        for medication in prescription['data']['medications']:
            if medication['data']['use_type'] == "Externo":
                medications["externos"].append((medication, undescore_len(medication)))
            else:
                medications["internos"].append((medication, undescore_len(medication)))

        return medications

atapi.registerType(ChartFolder, PROJECTNAME)
