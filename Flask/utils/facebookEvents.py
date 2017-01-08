
import facebook
import json
import addEventToDB
#make sure to:
#    pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

#Documentation:
#https://developers.facebook.com/docs/graph-api/reference/event
#https://developers.facebook.com/docs/graph-api/reference/v2.8/group/events
#https://facebook-sdk.readthedocs.io/en/latest/api.html
#TODO
# ADD GROUP ID SO ITS PRETTIER

#change this: user token
#https://developers.facebook.com/tools/access_token/

token = 'EAAC1mYYLrqkBAFVX4KHqZBhf9ZBTwOKtyr2x7NDP59iSkh9DiqOgXMU9xGCed2gURoBAPiLWDO7gpxNmMPPLphAmskuRCJtuvCO9w6taHZBSomoWZA8RMvXT61uytQl4ORHsogURgjMYkwHK20g78Df4ZAZCNxrk0ZD'


graph = facebook.GraphAPI(token)

def get_event():
	event = graph.get_object(id='706776926156529', fields='description,start_time,end_time,place')
	#print(event['description']) Windows refuses to print a character so it breaks
	print(event['start_time'])
	print(event['end_time'])
	print(event['place'])

group = graph.get_object(id='358192317896345/events',fields="name,id,location,start_time,end_time,description")
group_json = json.dumps(group) #takes nasty data into json
#print group_json
group_dict = json.loads(group_json) #takes less nasty json into dict
#for key, value in group_dict.iteritems():
#	print key


#print group_dict['data']


#event_name 
#event_location 
#event_start_time 
#event_end_time 
#event_description
#event_id

def get_event_name(i): #gets event name from i element in data
	return  group_dict['data'][i]['name']

def get_event_location(i):#gets event location from i element in data
	return group_dict['data'][i]['location']
		
def get_event_start_time(i):#gets event start time from i element in data
        return group_dict['data'][i]['start_time']

def get_event_end_time(i):#gets event end time from i element in data
	return group_dict['data'][i]['end_time']

def get_event_description(i): #gets event description from i element in data
	return group_dict['data'][i]['description']

def get_event_id(i):  #gets event id from i element in data
        return group_dict['data'][i]['id']


def getEvents():
        l = len(group_dict['data'])
        i = 0
        while (i < l):
                addEventToDB.addEvent(get_event_id(i),get_event_name(i),get_event_description(i),get_event_start_time(i),get_event_end_time(i),None,get_event_location(i))
                i+=1
	


getEvents()
#addEvent(event_id[i],event_name,event_description,event_start_time,event_end_time, 'geolocationplaceholder', event_location)
