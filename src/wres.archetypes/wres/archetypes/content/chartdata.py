from Persistence import Persistent
from BTrees.OOBTree import OOBTree
from ZODB.PersistentList import PersistentList
from DateTime import DateTime
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass


#class MedicalHistories(Persistent):
    #__allow_access_to_unprotected_subobjects__ = 1
    #security = ClassSecurityInfo()

    #def __init__(self):
        #self.histories = OOBTree()

    #def __getitem__(self, item):
        #return self.histories[item]

    #security.declarePublic('items')
    #def items(self):
        #temp = [(key, value) for key, value in self.histories.items()]
        #return temp

    #security.declarePublic('add_entry')
    #def add_entry(self, history_id, date, came_from, data):
        #hlist = self.histories.get(history_id, None)
        #if hlist is None:
             #self.histories[history_id] = PersistentList()
        #hlist = self.histories[history_id]
        #entry = {'date': date, 'came_from': came_from, 'data': data}
        #hlist.append(entry)

class ChartData(Persistent):
    __allow_access_to_unprotected_subobjects__ = 1
    #TODO alguns atributos nao estao sendo usados. Limpar posteriormente.
    mapping = {
               #'questionnaire': OOBTree,
               #'family_history': OOBTree,
               #'past_medical_history': OOBTree,
               'allergies': OOBTree,
               'not_signed_allergies': OOBTree,
               #'tests': OOBTree,
               'immunizations': OOBTree,
               'medications': OOBTree,
               'review_of_systems': OOBTree,
               #'social_history': OOBTree,
               #'maintenances': OOBTree,
               #'notes': OOBTree,
               'problems': OOBTree,
               'prescriptions': OOBTree,
               #'encounters': OOBTree,
               #'plans': OOBTree,
               #'follow_up_notes': OOBTree,
               'vital_signs': OOBTree,
               'laboratory': OOBTree,
               #'histories': MedicalHistories,
              }
    security = ClassSecurityInfo()
    def __init__(self):
        self.clean_chart()

    def __getattr__(self, attr):
        mapping = self.mapping
        if attr in mapping:
            setattr(self, attr, mapping[attr]())
        else:
            raise AttributeError
        return getattr(self, attr)
    #Roteamento dos documentos
    def add_not_signed_allergies(self, date, came_from, allergies):
        entry = {'date': date, 'came_from': came_from, 'data': allergies}
        entry['id'] = '/'.join(entry['came_from'])
        container = getattr(self, 'not_signed_allergies')
        saved = container.get(entry['id'], [])
        if saved != allergies:
            container[entry['id']] = entry
    #Roteamento dos documentos
    def del_not_signed_allergies(self, came_from):
        key = '/'.join(came_from)
        container = getattr(self, 'not_signed_allergies')
        if container.has_key(key):
            del container[key]

    def clean_chart(self):
        mapping = self.mapping
        for key, value in mapping.items():
            setattr(self, key, value())

    def update_chart(self):
        mapping = self.mapping
        for key, value in mapping.items():
            if not hasattr(self, key):
                setattr(self, key, value())
    #Roteamento dos documentos
    def add_entry_to(self, place_id, date, came_from, data):
        self.__add_entry_to(place_id, date, came_from, data)
    #Roteamento dos documentos
    def add_entry_to_problems(self, id, date, came_from, data):
        entry = {'date': date, 'came_from': came_from, 'data': data}
        entry['id'] = id
        place = getattr(self, 'problems')
        place[entry['id']] = entry
    #Roteamento dos documentos
    def __add_entry_to(self, place_id, date, came_from, data):
        entry = {'date': date, 'came_from': came_from, 'data': data}
        entry['id'] = str(entry['date'].aCommon()) + str(DateTime())
        place = getattr(self, place_id)
        place[entry['id']] = entry

    #def distribute_questionnaire(self, quest=None):
        #if quest is None:
            #quest = {}
            #for key in self.questionnaire.keys():
                #quest[key] = self.questionnaire[key]

        #date = DateTime()
        #def add_entry(place_id, data):
            #self.__add_entry_to(place_id, date, 'questionnaire', data)
        #family_history = quest.get('family_history', [])
        #family_diseases = quest.get('family_diseases', [])
        #fh = {'fh': family_history,
              #'fd': family_diseases
              #}
        #add_entry('family_history', fh)
        #self_diseases = quest.get('self_diseases', [])
        #additional_illness = quest.get('additional_illness', [])
        #hospitalizations = quest.get('hospitalizations', [])
        #mtfh = quest.get('more_than_four_hospitalizations', False)
        #pmh = {'sd': self_diseases,
               #'ai': additional_illness,
               #'ho': hospitalizations,
               #'mtfh': mtfh,
               #}
        #add_entry('past_medical_history', pmh)
        #medicines = quest.get('medicines', {}).values()
        #medicines = [medicine for medicine in medicines if medicine != ['']]
        #allergies = [medicine[1] for medicine in medicines \
                    #if medicine[0] == 'allergic']
        #allergies = [{'allergy': allergy, 'reaction': ''} for allergy in allergies]
        #add_entry('allergies', allergies)
        #medicines = [medicine[1] for medicine in medicines \
                     #if medicine[0] == 'taking']
        #add_entry('medications', medicines)
        #tests = quest.get('tests', {}).values()
        #tests = [test for test in tests if len(test) == 3]
        #add_entry('tests', tests)
        #immunizations = quest.get('immunizations', {}).values()
        #immunizations = [item for item in immunizations if len(item) == 3]
        #add_entry('immunizations', immunizations)
        #ros = extract_review_of_systems(quest)
        #add_entry('review_of_systems', ros)
        #social_history = extract_social_history(quest)
        #add_entry('social_history', social_history)

#def extract_groups(quest, group_keys_mapping):
    #result = {}
    #for group, keys in group_keys_mapping.items():
        #result[group] = [quest[key] for key in keys]
    #return result

#def extract_review_of_systems(quest):
    #mapping = {'musculoskeletal': [str(i) for i in xrange(1, 6)],
            #'skin': [str(i) for i in xrange(6, 10)],
            #'neurological': [str(i) for i in xrange(10, 15)],
            #'mood': [str(i) for i in xrange(15, 32)],
            #'digestive': [str(i) for i in xrange(49, 62)],
            #'urinary': [str(i) for i in xrange(62, 69)],
            #'male genital': [str(i) for i in xrange(69, 74)],
            #'female genital': [str(i) for i in xrange(74, 86)],
            #'obstetric history': [str(i) for i in xrange(86, 92)],
            #'head and neck': [str(i) for i in xrange(92, 95)],
            #'eyes': [str(i) for i in xrange(95, 103)],
            #'ears': [str(i) for i in xrange(103, 108)],
            #'mouth': [str(i) for i in xrange(108, 112)],
            #'nose and throat': [str(i) for i in xrange(112, 120)],
            #'respiratory': [str(i) for i in xrange(120, 126)],
            #'cardiovascular': [str(i) for i in xrange(126, 136)],
            #}
    #return extract_groups(quest, mapping)

#def extract_social_history(quest):
    #mapping = {'general': [str(i) for i in xrange(32, 49)] \
               #+ ['additional_comments'],
               #}
    #return extract_groups(quest, mapping)

#class Maintenance:
    #__allow_access_to_unprotected_subobjects__ = 1
    #def __init__(self, **kwargs):
        #self.maintenance = kwargs.get('maintenance', '')
        #self.creation_date = kwargs.get('creation_date', None)
        #self.recommended_for = kwargs.get('recommended_for', '')
        #self.due_by = kwargs.get('due_by', None)
        #self.state = kwargs.get('state', 'current')
        #self.encounters = []

    #def toDict(self):
        #result = {}
        #attrs = ['maintenance', 'creation_date', 'recommended_for', 'due_by',\
                 #'state', 'encounters']
        #for attr in attrs:
            #result[attr] = getattr(self, attr)
        #return result

#class Note:
    #__allow_access_to_unprotected_subobjects__ = 1
    #def __init__(self, **kwargs):
        #self.id = kwargs['id']
        #self.submitted_by = kwargs.get('submitted_by', '')
        #self.submitted_on = kwargs.get('submitted_on', None)
        #self.state = kwargs.get('state', 'active')
        #self.note = kwargs.get('note', '')

    #def toDict(self):
        #result = {}
        #attrs = ['id', 'submitted_by', 'submitted_on', 'state', 'note']
        #for attr in attrs:
            #result[attr] = getattr(self, attr)
        #return result

class Problem:
    __allow_access_to_unprotected_subobjects__ = 1
    attrs = {'problem': '',
             'code': '',
             'started': None,
             'reported': None,
             'chronicity': '',
             'submitted_on': None,
             'submitted_by': '',
             'id': '',
             'state': 'active',
             'end_date': None,
             'note': '',
             }
    def __init__(self, **kwargs):
        if not 'id' in kwargs:
            self.id = kwargs['problem']
        else:
            self.id = kwargs['id']
        for attr, default in self.attrs.items():
            if attr != 'id':
                setattr(self, attr, kwargs.get(attr, default))

    def toDict(self):
        result = {}
        for attr in self.attrs.keys():
            result[attr] = getattr(self, attr)
        return result

#class Prescription:
    #__allow_access_to_unprotected_subobjects__ = 1
    #attrs = {'id': '',
             #'medication': '',
             #'mg': '',
             #'sol': '',
             #'sig': '',
             #'number': '',
             #'refills': '',
             #'start': None,
             #'end': None,
             #'dea': '',
             #'dont_substitute': True,
             #'state': 'current',
             #'renewed': False,
             #'reason': '',
             #'signed': False,
             #'signed_by': '',
             #'submitted_by': '',
             ##atributos adicionados pelo uso de Datagrid
             #'valid': '',
             #'instructions': '',
           #}

    #def __init__(self, **kwargs):
        #for attr, default in self.attrs.items():
            #setattr(self, attr, kwargs.get(attr, default))
    
    #def toDict(self):
        #result = {}
        #for attr in self.attrs.keys():
            #result[attr] = getattr(self, attr, self.attrs[attr])
        #return result

#class Encounter:
    #attrs = {'id': '',
             #'doctor_id': '',
             #'date_of_visit': None,
             #'visit': None,
            #}
    
    #def __init__(self, **kwargs):
        #self.id = kwargs['id']
        #self.doctor_id = kwargs.get('doctor_id', 'none')
        #self.date_of_visit = kwargs.get('date_of_visit', None)
        #self.visit = kwargs.get('visit', None)

    #def toDict(self):
        #result = {}
        #for attr in self.attrs.keys():
            #result[attr] = getattr(self, attr, self.attrs[attr])
        #return result

InitializeClass(ChartData)
#InitializeClass(MedicalHistories)
