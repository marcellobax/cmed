# coding=utf-8
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from wres.archetypes.content.patient import Patient
from wres.policy.utils.utils import getWresSite

portal = getWresSite()
pc = getToolByName(context,'portal_catalog')

#Verify if patient Folder has lastChartSystemID
brains = pc.searchResults({'Type':'PatientFolder'})
pf = brains[0].getObject()
try:
	pf.getLastChartSystemID()
except:
	return "Impossível de preencher o chartSystemID do paciente.\
    Dado que Patient Folder não tem lastChartSystemID"

#Fill chartSystemID patient field
brains = pc.searchResults({'Type':'Patient'})
changed = []

for brain in brains:
	patient = brain.getObject()
	chartID = patient.getChartSystemID()
	nextChartSystemID = pf.getLastChartSystemID()
	
	if chartID == 0 or chartID == None:
		patient.setChartSystemID(nextChartSystemID)
		pf.setLastChartSystemID(nextChartSystemID)
		changed.append(patient.getId())

return '<html><body><div>\
			<b>Agora todos pacientes estão com chartSystemID</b><br/>\
			Pacientes modificados:<br/>\
			%s\
			</div><br/></body></html>' % str(changed)