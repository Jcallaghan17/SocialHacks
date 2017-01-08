import facebook
import json
import addEventToDB

token = 'EAAC1mYYLrqkBAFVX4KHqZBhf9ZBTwOKtyr2x7NDP59iSkh9DiqOgXMU9xGCed2gURoBAPiLWDO7gpxNmMPPLphAmskuRCJtuvCO9w6taHZBSomoWZA8RMvXT61uytQl4ORHsogURgjMYkwHK20g78Df4ZAZCNxrk0ZD'
graph = facebook.GraphAPI(token)
GROUPID = 358192317896345

feed = graph.get_object(id=str(GROUPID)+'/feed', fields ='id, object_id')
feed_json = json.dumps(feed)
feed_dict = json.loads(feed_json)


evs = []
for item in feed_dict['data']:
        try:
                evs.append(item['object_id'])
        except KeyError:
                print ""

#print evs



def get_shared_name(i):
	f = graph.get_object(id=i,fields="name")
        return f['name']
def get_shared_description(i):
        f = graph.get_object(id=i,fields="description")
        return f['description']
def get_shared_start(i):
	f = graph.get_object(id=i,fields="start_time")
        return f['start_time']
def get_shared_end(i):
	f = graph.get_object(id=i,fields="end_time")
        return f['end_time']
def get_shared_location(i):
	f = graph.get_object(id=i,fields="location")
        return f['location']




def get_shared_events():
        l = len(evs)
        i = 0
        while (i < l):
    	        addEventToDB.addEvent(evs[i],get_shared_name(evs[i]),get_shared_description(evs[i]),get_shared_start(evs[i]),get_shared_end(evs[i]),None,get_shared_location(evs[i]))
                i+=1

