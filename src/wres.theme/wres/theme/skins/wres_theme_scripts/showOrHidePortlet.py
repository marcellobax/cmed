##parameters=portlet_id, default='expanded'
request = context.REQUEST
session = request.SESSION
state = session.get(portlet_id, default)
##from Products.zdb import set_trace; set_trace()
if state == 'collapsed':
    return 'display: none'
else:
    return None
