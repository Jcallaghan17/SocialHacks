import facebook

graph = facebook.GraphAPI(access_token='EAARsOJeuDDIBANtqRaYZBlnB6ex4IZCKJUSzi27PvueRzMisYNYsFO68w52xM6U3UnHOfbd4wGYYJYH0nKzFZA7e8qtVLjJBuI9NPKDVbhF68pfmQLeL6RgABsStSApb7L1aveXXsM8upC921Wrd26JBlFAZAHBIpaEgvW8bXgZDZD')

post = graph.get_object(id='post_id')
print(post['message'])

#event = graph.get_object(id='event_id', fields='attending_count,declined_count')
#print(event['attending_count'])
#print(event['declined_count'])



'''
graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
graph.put_object("me", "feed", message="I am writing on my wall!")

'''