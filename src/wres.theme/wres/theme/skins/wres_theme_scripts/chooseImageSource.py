##parameters=portlet_id, expanded, collapsed, default='expanded'
request = context.REQUEST
session = request.SESSION
state = session.get(portlet_id, default)
##from Products.zdb import set_trace; set_trace()
if state == 'collapsed':
    return collapsed
else:
    return expanded
