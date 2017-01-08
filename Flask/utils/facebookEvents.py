
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

token = 'EAAC1mYYLrqkBABaBQxO0pFKN9aoGSC8fZC6r2TQ8gEm5lS1RCzmARermEJGP1pPQdtoFuBl0jDrCeC7v584hcoZAscZC0q3R6ZAbWmNE9ZAarnrlSdXrniJjJHNZBpZBtdxRw0v6GTcki11BlUGnl0HXiDXOKEVM8A1V7jVIn5oVgZDZD'

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

print group_dict['data']

l = len(group_dict['data'])
i = 0
event_name = []
event_location = []
event_start_time = []
event_end_time = []
event_id = []
def get_event_name(intLen): #gets event name from dictionary
	i = 0
	l = intLen
	while i < l:
		event_name.append(group_dict['data'][i]['name'])
		i+=1
		#print i
	print event_name
def get_event_location(intLen):#gets event location from dictionary
	i = 0
	l = intLen
	while i < l: 
		event_location.append(group_dict['data'][i]['location'])
		i+=1
	print event_location
def get_event_start_time(intLen):#gets event start time from dictionary
	i = 0
	l = intLen
	while i < l: 
		event_location.append(group_dict['data'][i]['start_time'])
		i+=1
	print event_location
def get_event_end_time(intLen):#gets event end time from dictionary
	i = 0
	l = intLen
	while i < l: 
		event_location.append(group_dict['data'][i]['end_time'])
		i+=1
	print event_end_time
def get_event_id(intLen):	#gets event id from dictionary
	i = 0
	l = intLen
	while i < l: 
		event_location.append(group_dict['data'][i]['id'])
		i+=1
	print event_id
get_event_location(l)
