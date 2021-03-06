from DateTime import DateTime

request = context.REQUEST
vars = ['problem', 'code', 'started', 'state','note']
problem = {}
for var in vars:
    problem[var] = request[var]

date_vars = ['started']
for var in date_vars:
    problem[var] = DateTime(problem[var], datefmt="international")

member = context.portal_membership.getAuthenticatedMember()
problem['submitted_by'] = member.id
problem['submitted_on'] = DateTime()
if problem['state'] == 'active':
    problem['end_date'] = ''
else:
    problem['end_date'] = DateTime().strftime('%d/%m/%Y')
context.chart_data.save_entry(context, 'problems', **problem)

state.set(portal_status_message='Diagnóstico adicionado.')
return state
