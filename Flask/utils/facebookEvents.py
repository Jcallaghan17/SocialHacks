import facebook


#make sure to:
#    pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk

#Documentation:
#https://developers.facebook.com/docs/graph-api/reference/event
#https://developers.facebook.com/docs/graph-api/reference/v2.8/group/events
#https://facebook-sdk.readthedocs.io/en/latest/api.html




#change this: user token
#https://developers.facebook.com/tools/access_token/

token = 'EAAMZAuGqTFEcBAAAXFbEaugyb4ZAZClgwOWRKtltsdZAmjmeWiY0GHZCq8nB7olIZAFRZBlNYpipPNZBCKzuLJtU2V2cQjl8gRni8AMP4wvHjnwI8AxTuqbVZBZCVN3WT05VQa88fVUccZBbNuprlbUlv78QjZBueT22o8CpUDm51CxGZCQZDZD'

graph = facebook.GraphAPI(token)


event = graph.get_object(id='706776926156529', fields='description,start_time,end_time,place')
print(event['description'])
print(event['start_time'])
print(event['end_time']
print(event['place'])

#not tested
page = graph.get_object(id='358192317896345/events')
for thing in page:
    print thing
