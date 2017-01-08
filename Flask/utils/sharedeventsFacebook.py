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
length = len(feed_dict['data'])
i = 0
def get_object_id(i): #Not to be confused with event id
#This gets the object id which only appears in the feed if its an event
	print feed_dict['data'][i]['object_id']
	return feed_dict['data'][i]['object_id'] #This should give a valid event id



get_object_id():


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
