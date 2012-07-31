# coding=utf-8

"""Definition of the Patient content type
"""
from DateTime import DateTime
from AccessControl import ClassSecurityInfo

import json

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from ComputedAttribute import ComputedAttribute

from wres.archetypes.interfaces import IPatient
from wres.archetypes.config import PROJECTNAME
from wres.archetypes.content import wresuser
from wres.archetypes.content.chartdata import ChartData, Event #,Prescription, Maintenance, Note, Problem 
from wres.archetypes.content.schemas.patient import PatientSchema

from wres.policy.utils.roles import *

schemata.finalizeATCTSchema(
    PatientSchema,
    folderish=True,
    moveDiscussion=False
)

class Patient(wresuser.WRESUser):
    """Patient type for WRES website"""
    implements(IPatient)

    meta_type = "Patient"
    schema = PatientSchema

    security = ClassSecurityInfo()

    def SearchableText(self):
        """
        Returns strings that can be searched by the SearchableText catalog index.
        Example input:
            pid = jsilva, cpf = 0123456790, fullname = Joao Silva
        Example output:
            ['jsilva', '0123456789', 'Joao Silva']
        """
        pid = self.getId()
        cpf = self.getSocialSecurity()
        fullname = self.getFullName()
        return [pid, cpf, fullname]

    def getInformation(self):
        """
        Retorna um objeto do tipo json (JavaScript Object Notation).
        Utilizado no tipo visita (BuildingBlocksWidget)
        """
        return json.dumps({'getLastDate': self.getLastVisitDate(), 'getContactPhone': self.getContactPhone(), 'UID': self.UID()})
        
    def getGroup(self):
        """
        Return patient group: "Patient"
        """
        return PATIENT_GROUP
        
    def createHiddenKey(self, key):
        """
        Return string: key + '_hidden'
        """
        return key + '_hidden'
    
    def existSubObject(self, key):
        """
        Sees if patient has hidden atributes of the key: key+"_hidden"
        """
        hidden_key = self.createHiddenKey(key)
        return hasattr(self, hidden_key)
    
    def createChartFolder(self, id):
        """
        Create chart folder in patient.
        After execute:
        all_chartfolder = id list of all chartfolders indexed in system
        assertTrue("documents" in all_chartfolders)     assertTrue("impressos" in all_chartfolders) 
        assertTrue("exams" in all_chartfolders)         assertTrue("upload" in all_chartfolders)
        """
        from wres.archetypes.content.chartfolder import addChartFolder
        addChartFolder(self, id=id, title='Chart Folder')

    def createMissingObject(self, key):
        """
        Create object "key" if it doesn't exists
        Obs: Nome fantasia, só funciona para chartFolder
        """
        hidden_key = self.createHiddenKey(key)
        if not self.existSubObject(key):
            if key == 'chartFolder':
                self.createChartFolder(hidden_key)
#            elif key == 'casesFolder':
#                self.createCasesFolder(hidden_key)
        return hidden_key

    def _getSubObject(self, key):
        """
        Return patient's chartFolder (if it doen't exists, chartFolder is created')
        Obs: Nome fantasia, só funciona para chartFolder
        """
        hidden_key = self.createHiddenKey(key)
        if not self.existSubObject(key):
            self.createMissingObject(key)
#        obs: esse trecho considera que essa função será utilizada
#        apenas para objetos chartFolder.
        chart = getattr(self, hidden_key)
        chart.setTitle('Prontuário')
        return chart
    
    def chartFolder(self):
        """ 
        Just create the function used by ComputedAttribute() to create chartFolder attribute.
        """
        return self._getSubObject('chartFolder')
    chartFolder = ComputedAttribute(chartFolder, 1)

#    as duas funcoes abaixo sao necessarias no tipo Visit.
    security.declarePublic('getLastVisitDate')
    def getLastVisitDate(self, strftime='%d/%m/%Y'):
        """
        Return the patient's attribute: lastVisitDate in %d/%m/%Y
        If it not exists return "No visits concluded"
        """
        if not hasattr(self, 'lastVisitDate'):
            return 'No visits concluded'
        else:
            return self.lastVisitDate.strftime(strftime)

    security.declarePublic('setLastVisitDate')
    def setLastVisitDate(self, date):
        """
        Just set the patient's attribute: lastVisitDate
        Obs: O parametro "date" precisar possuir a funcao strftime()
        """
        self.lastVisitDate = date
        if not hasattr(date,"strftime"):
            raise ValueError("Tipo de data invalida")

    def Title(self):
        """
        If patient.firstName = 'Joao' and patient.lastName = 'Silva'
        This function will return 'Joao Silva'
        If it doesn't has a first and a last name, the function will return "Sem Nome"
        """
        if self.getFirstName() == '' and self.getLastName() == '':
            return 'Sem Nome'
        else:
            return '%s %s' %(self.getFirstName(),
                             self.getLastName(),
                            )

    def lower_title(self):
        """
        Return all patient.Title() letters in lower case.
        """
        return self.Title().lower()

    def at_post_create_script(self):
        """
        Just execute WRESUser.at_post_create_script(), basically register
        the patient object as portal member
        """
        self.create_event(Event.CREATION, self.created(), self)
        wresuser.WRESUser.at_post_create_script(self)
        
    def at_post_edit_script(self):
        wresuser.WRESUser.at_post_edit_script(self)


    #the 3 functions bellow are needed to create a patient user
    def getFullName(self):
        return self.Title()

    def get_home_url(self):
        return '/'.join(self.getPhysicalPath()) + '/patient_desktop_view'

    def __create_chart_data(self):
        clean_self = self.aq_base
        if not hasattr(clean_self, 'chart_data_hidden'):
            self.chart_data_hidden = ChartData()
            self._p_changed = 1
        return self.chart_data_hidden
    chart_data = ComputedAttribute(__create_chart_data, 1)

    def create_event(self, ev_type, date, related_obj):
        '''
        register an event. all modules that creates events use this method.
        '''
        chart_data = self.chart_data # garante a criacao do chart_data
        events = chart_data.events
        new_event = Event(self, ev_type, date, related_obj) 
        events[new_event.id] = new_event

    def get_events(self):
        '''
        return a list of events sorted by date.
        '''
        dic = dict(self.chart_data.events)
        events_list = dic.values()
        events_list.sort(cmp=Event._event_cmp)
        return events_list

#   Metodo utilizado apenas no debug_patientchartdata
    def get_chart_data_map(self):
        return ChartData.mapping

    def chart_data_summary(self):
        '''
        method used in migration and in debug_patientchartdata.
        just return the chart_data in format of dictionaries.
        '''
        keys = ['review_of_systems', 'medications', 'prescriptions', 
        'allergies', 'problems', 'not_signed_allergies', 'laboratory']

        dic_chartdata = {}
        dic_chartdata['allergies'] = dict(self.chart_data.allergies)
        dic_chartdata['review_of_systems'] = dict(self.chart_data.review_of_systems)
        dic_chartdata['medications'] = dict(self.chart_data.medications)
        dic_chartdata['prescriptions'] = dict(self.chart_data.prescriptions)
        dic_chartdata['problems'] = dict(self.chart_data.problems)
        dic_chartdata['not_signed_allergies'] = dict(self.chart_data.not_signed_allergies)
        dic_chartdata['laboratory'] = dict(self.chart_data.laboratory)
        return dic_chartdata

    def import_chartdata(self, chart_dic):
        '''
        used exclusively in migration. 
        '''
        from BTrees.OOBTree import OOBTree
        keys = ['review_of_systems', 'medications', 'prescriptions', 
        'allergies', 'problems', 'not_signed_allergies', 'laboratory']

        for key in self.chart_data.mapping.keys():
            if chart_dic.has_key(key): # increase upgrade compatibility
                setattr( self.chart_data, key, OOBTree(chart_dic[key]) )            

atapi.registerType(Patient, PROJECTNAME)
