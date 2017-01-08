import facebook
import json
import addEventToDB
token = 'EAAC1mYYLrqkBAFVX4KHqZBhf9ZBTwOKtyr2x7NDP59iSkh9DiqOgXMU9xGCed2gURoBAPiLWDO7gpxNmMPPLphAmskuRCJtuvCO9w6taHZBSomoWZA8RMvXT61uytQl4ORHsogURgjMYkwHK20g78Df4ZAZCNxrk0ZD'
graph = facebook.GraphAPI(token)
GROUPID = 358192317896345

feed = graph.get_object(id=str(GROUPID)+'/feed')
feed_json = json.dumps(feed)
feed_dict = json.loads(feed_json)
length = len(feed_dict['data'])
i = 0
while (i < length):
	print feed_dict['data'][i]
	i+=1
	
#TODO
#GO THROUGH FEED
#FIND SHARED EVENTS
#GRAB THE ACTUAL ID FOR EVENT
#POST EVENT DATA
