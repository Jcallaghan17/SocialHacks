
import facebook
import json

#make sure to:
#    pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

#Documentation:
#https://developers.facebook.com/docs/graph-api/reference/event
#https://developers.facebook.com/docs/graph-api/reference/v2.8/group/events
#https://facebook-sdk.readthedocs.io/en/latest/api.html




#change this: user token
#https://developers.facebook.com/tools/access_token/

token = 'EAAC1mYYLrqkBACm5KZCHswZBathr2jEGRfLNGJdTSHXTLZBg2Ui99U3H6ZAGqPKbXeZAAIrhzZB1ZAlzBLXMaHXN4myoYDEe9ZBSpv5tLq9FEaXvFUO222tr6TZBEn4yqz9Sf1HcZANyHn5waJfQL0mxiJtMFtT5wVMWIlZCPOJZBBZCu7wZDZD'

graph = facebook.GraphAPI(token)

def get_event():
	event = graph.get_object(id='706776926156529', fields='description,start_time,end_time,place')
	#print(event['description']) Windows refuses to print a character so it breaks
	print(event['start_time'])
	print(event['end_time'])
	print(event['place'])

group = graph.get_object(id='358192317896345/events')
group_json = json.dumps(group) #takes nasty data into json
#print group_json
group_dict = json.loads(group_json) #takes less nasty json into dict
#for key, value in group_dict.iteritems():
#	print key

#print group_dict['data']

l = len(group_dict['data'])
i = 0
#while i < 2:
	#group_array = []
	#group_array.append(group_dict['data'][i]['name'])
	#i+=1
	#print i
print group_array

