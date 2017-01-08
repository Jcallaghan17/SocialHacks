import facebook
import json
import addEventToDB
import facebookEvents
token = 'EAAC1mYYLrqkBAFVX4KHqZBhf9ZBTwOKtyr2x7NDP59iSkh9DiqOgXMU9xGCed2gURoBAPiLWDO7gpxNmMPPLphAmskuRCJtuvCO9w6taHZBSomoWZA8RMvXT61uytQl4ORHsogURgjMYkwHK20g78Df4ZAZCNxrk0ZD'
graph = facebook.GraphAPI(token)
GROUPID = 358192317896345

feed = graph.get_object(id=str(GROUPID)+'/feed', fields ='id, object_id')
feed_json = json.dumps(feed)
feed_dict = json.loads(feed_json)

def get_object_id(i): #Not to be confused with event id
#This gets the object id which only appears in the feed if its an event
	return feed_dict['data'][i]['object_id'] #This should give a valid event id
def get_shared_name(i):
	return feed_dict['data'][i]['name']
def get_shared_description(i):
	return feed_dict['data'][i]['description']
def get_shared_start(i):
	return feed_dict['data'][i]['start_time']
def get_shared_end(i):
	return feed_dict['data'][i]['end_time']
def get_shared_location(i):
	return feed_dict['data'][i]['location']

def get_shared_events():
 	l = len(group_dict['data'])
    i = 0
    while (i < l):
    	addEventToDB.addEvent(get_object_id(i),get_shared_name(i),get_shared_description(i),get_shared_start(i),get_shared_end(i),None,get_shared_location(i))
        i+=1

#get_object_id() #ID 0,1,4 have Object ID's
'''
while (i < length):
	print feed_dict['data'][i]
	i+=1
'''
#TODO
#GO THROUGH FEED
#FIND SHARED EVENTS
#GRAB THE ACTUAL ID FOR EVENT
#POST EVENT DATA
