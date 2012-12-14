from wres.policy.utils.utils import remove_accents
from wres.policy.utils.utils import strip_accents

class PatientSomeInfo():
	phone = ""
	birth = ""
	name = ""
	comp_name = ""
	chartUrl = ""

pc = context.portal_catalog

brains = pc.search({'meta_type': 'Patient'})
listMetaPatients = []
for brain in brains:
	obj = brain.getObject()
	if obj.getState_cmed() == 'inactive':
			continue
	patient = PatientSomeInfo()
	
	phone = obj.getContactPhone()
	if phone:
		patient.phone = '(' + phone[:2] + ')' +  phone[2:6]+ '-' +phone[6:]
	
	patient.name = obj.getFullName()
	
	birth = obj.getBirthDate()
	if birth:
		patient.birth = birth.strftime('%d/%m/%Y')

	patient.chartUrl = obj.absolute_url() + '/chartFolder'
	patient.comp_name = strip_accents(unicode(patient.name, 'utf-8'))
	listMetaPatients.append(patient)
	
listMetaPatients.sort(key=lambda patient: patient.comp_name, reverse=False)
return listMetaPatients

