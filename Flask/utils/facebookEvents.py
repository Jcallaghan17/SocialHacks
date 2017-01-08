import facebook


#make sure to:
#    pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

#Documentation:
#https://developers.facebook.com/docs/graph-api/reference/event
#https://developers.facebook.com/docs/graph-api/reference/v2.8/group/events
#https://facebook-sdk.readthedocs.io/en/latest/api.html




#change this: user token
#https://developers.facebook.com/tools/access_token/

token = 'EAARsOJeuDDIBAI0BKktfZB03o5QeZCCkyulINIxoZC1nLPXfC17O5XyOHwvudBFeTbUG6ZCMBbBybvDbY8p1lribqdVa5L0P1aZC569YIpRDal46FrARIwy16EdJYeaFmwXo3t2a2fSB0mMCXucHrmokkBsT9BZC487q8C0DlwVwZDZD'




graph = facebook.GraphAPI(token)


event = graph.get_object(id='374068616302738', fields='description,start_time,end_time,place')
#print(event['description'])
print(event['start_time'])
print(event['end_time'])
#print(event['place'])

#not tested
#page = graph.get_object(id='358192317896345')


#print page



#page1 = graph.get_object(id='358192317896345/feed?metadata=1')

#print page1['type']


#for item in page1:
#    print item
#print page1['description']
#print page1['paging']


#page1 = graph.get_connections(id='358192317896345', connection_name='events')

#print page1

#print list(page1)
