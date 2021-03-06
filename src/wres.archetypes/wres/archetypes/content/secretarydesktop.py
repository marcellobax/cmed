## coding=utf-8

from zope.app.component.hooks import getSite
from DateTime import DateTime

class SecretaryDesktopData():

    P_TRANSITIONS = {
        'scheduled': [('confirm', 'Confirmar'), ('non show', 'Ausente'), ('start visit', 'Presente'), ('unconfirm', 'Desmarcar')],
        'concluded': [], 
        'confirmed': [('non show', 'Ausente'), ('start visit', 'Presente')],
        'hided': [],
        'non-show': [],
        'not scheduled': [('schedule', 'Agendar')],
        'running': [('conclude', 'Concluir')],
        'unscheduled': [('hide', 'Esconder')],
    }

    def __init__(self, context, doctor_id):

        # pesquisa o catálogo por visitas de hoje e amanhã
        today = DateTime().earliestTime()
        tomorrow = today+1
        query = {'meta_type' : 'Visit', 'start' : {'query': [today, tomorrow.latestTime()], 'range' : 'min:max'},}
        if doctor_id:
            query['getProviderId'] = doctor_id
        brains = context.portal_catalog.search(query, sort_index='start')

        # separa entre hoje e amanhã
        self.today = []
        self.tomorrow = []
        for br in brains:
            if br.start > tomorrow:
                self.tomorrow.append(br)
            else:
                self.today.append(br)

    def parse_visits(self, visits):
        """
        PAREI: Preenchendo o dicionário abaixo. Vou precisar adicionar algumas colunas de metadado
        """

        data = []
        for br in visits:
            v = {}
            v['doctor'] = ''
            v['doctor_id'] = br.getProviderId
            v['getReviewState'] = br.review_state
            v['raw_status'] = br.review_state
            v['possible_transitions'] = self.P_TRANSITIONS[br.review_state]
            v['absolute_url'] = br.getPath()
            v['patient'] = ''
            v['patient_title'] = br.Title
            v['patient_absolute_url'] = br.getRemoteUrl
            v['start'] = br.start
            v['visit_type'] = br.Subject[0]
            v['visit_reason'] = br.getVisit_reason
            v['insurance'] = br.getInsurance
            data.append(v)
        return data

    def getVisitsFromToday(self):
        return self.parse_visits(self.today)

    def getVisitsFromTomorrow(self):
        return self.parse_visits(self.tomorrow)


#TODO Remover: 1/2015

# def event_between(eventstart, start, end):
#     return eventstart.greaterThanEqualTo(start) and \
#            eventstart.lessThanEqualTo(end)

# def filter_events_between(events, start, end):
#     return filter(lambda x: event_between(x.start(), start, end), events)

# class SecretaryDesktopData():
    
#     def __init__(self, context, doctor_id):
#         self.portal = getSite()
#         self.context = context
#         self.doctor_id = doctor_id
#         self.date = DateTime()
#         self.today_visits = None
#         self.visits = self.getTodayTomorrowVisits()
#         import ipdb; ipdb.set_trace()
        
#     def getTodayTomorrowVisits(self):
#         start = self.date.earliestTime()
#         end = (self.date+1).latestTime()
#         brains = self.getBrains(start, end)
#         return [VisitWrapper(brain) for brain in brains]

#     def getDayVisits(self, date):
#         visits = filter_events_between(self.visits, date.earliestTime(), date.latestTime())
#         visits_list= []
#         for visit in visits:
#             visit_dic = {}
#             visit_dic['absolute_url'] = visit.absolute_url()
#             visit_dic['getContactPhone'] = visit.getContactPhoneVisit()
#             visit_dic['getDoctor'] = visit.getDoctor()
#             visit_dic['getPatient'] = visit.getPatient()
#             visit_dic['getReviewState'] = visit.getReviewState()
#             visit_dic['getWorkflowActions'] = visit.getWorkflowActions()
#             if visit.getInsurance() == "":
#                 visit_dic['getInsurance'] = '---'
#             else:
#                 visit_dic['getInsurance'] = visit.getInsurance()
#             visit_dic['start'] = visit.start()
#             visit_dic['getVisit_type'] = visit.getVisit_type()
#             visit_dic['getVisit_reason'] = visit.getVisit_reason()
#             visits_list.append(visit_dic)
#         return visits_list

#     def getVisitsFromDate(self, days=0):
#         date = self.date + days
#         return self.getDayVisits(date)

#     def getVisitsFromToday(self):
#         if self.today_visits is None:
#             self.today_visits = self.getVisitsFromDate()
#         return self.today_visits
    
#     def getVisitsFromTomorrow(self):
#         return self.getVisitsFromDate(days=1)    
        
#     def getBrains(self, start, end):
#         query = {'meta_type' : 'Visit',
#                  'start' : {'query': [start, end], 'range' : 'min:max'},
#                  }
#         if self.doctor_id:
#             query['getProviderId'] = self.doctor_id
#         return self.portal.portal_catalog.search(query, sort_index='start')
    
#     def returnNone(self):
#         return None
    
# class VisitWrapper():
#     __allow_access_to_unprotected_subobjects__ = 1
#     workflow_action = {}
    
#     def __init__(self, brain):
#         self.brain_obj = brain.getObject()
#         self.brain = brain
#         self.estado = None
#         self.state_id = brain.review_state
#         self.patient = None
#         self.wf = None
    
#     def __getattr__(self, name):
#         if not name.startswith('__'):
#             if hasattr(self.brain, name):
#                 return getattr(self.brain, name)

#     def __eq__(self, other):
#         result = self.brain.getPath() == other.brain.getPath()
#         return result    
    
#     # modifica a string que representa o objeto.
#     def __repr__(self):
#         return "<VisitWrapper %s>" % str(self.brain)
        
#     def absolute_url(self, arg=None):
#         return self.brain.getURL()
    
#     def getContactPhoneVisit(self):
#         return self.brain_obj.getContactPhoneVisit()   
    
#     def getInsurance(self):
#         return self.brain_obj.getInsurance()

#     def getDoctor(self):
#         return self.brain_obj.getDoctor()         
        
#     def getPatient(self):
#         if self.patient is None:
#             self.patient = PatientWrapper(self.brain_obj)
#         return self.patient
    
#     def getReviewState(self):
#         if self.wf == None:
#             portal = getSite()
#             pw = portal.portal_workflow
#             self.wf = getattr(pw, 'appointment_workflow')
#         self.estado = getattr(self.wf.states, self.review_state)
#         self.state_id = self.estado.id        
#         return self.estado.title_or_id()

#     def getVisit_type(self):
#         return self.brain_obj.getVisit_type()   

#     def getVisit_reason(self):
#         return self.brain_obj.getVisit_reason()           
    
#     def getWorkflowActions(self):
#         if self.wf == None:
#             portal = getSite()
#             pw = portal.portal_workflow
#             self.wf = getattr(pw, 'appointment_workflow')        
#         if not VisitWrapper.workflow_action.has_key(self.state_id):
#             transitions_list = []
#             # pega as transicoes possiveis do estado
#             for t in self.wf.transitions:
#                 transition = getattr(self.wf.transitions, t)
#                 if t in self.estado.transitions:
#                     transitions_list.append({'id': t, 'name': transition.title_or_id()})
    
#             nl = [{'id': item['id'], 'name': item['name']} for item in transitions_list]
#             VisitWrapper.workflow_action[self.state_id] = nl
#         retorno = VisitWrapper.workflow_action[self.state_id]
#         return retorno
    
#     def start(self):
#         return self.brain.start    
    
# class PatientWrapper():
#     __allow_access_to_unprotected_subobjects__ = 1
    
#     def __init__(self, brain_obj):
#         self.brain_obj = brain_obj
#         self.patient = brain_obj.getPatientInfo()
#         self.obj = None
        
#     def __eq__(self, other):
#         return self.absolute_url_path() == other.absolute_url_path()

#     def __repr__(self):
#         return "<PatientWrapper '%s'>" % str(self.Title())    

#     def __getattr__(self, name):
#         if not name.startswith('__'):
#             if self.obj is None:
#                 visit = self.visit_brain.getObject()
#                 self.obj = self.brain_obj.getPatient()
#             return getattr(self.obj, name)        

#     def absolute_url(self):
#         return self.patient['absolute_url_path']

#     def absolute_url_path(self):
#         return self.patient['absolute_url_path']

#     def getHomePhone(self):
#         return self.patient['getHomePhone']

#     def getContactPhone(self):
#         return self.patient['getContactPhone']

#     def getConfirmedChartNumber(self):
#         return self.patient['getConfirmedChartNumber']

#     def Title(self):
#         return self.patient['Title']

