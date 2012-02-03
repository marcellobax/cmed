from DateTime import DateTime

request = context.REQUEST
vars = ['allergy', 'reaction', 'date']
allergy = {}
for var in vars:
    allergy[var] = request[var]

member = context.portal_membership.getAuthenticatedMember()
allergy['submitted_by'] = member.id
context.saveAllergy(**allergy)
state.set(portal_status_message='Alergia adicionada.')
return state

