import requests
import json

# Globals
NODE_URL = "http://localhost:3000/events"


def get_by_location(lat, lng):
    query_d = {"lat": lat, "lng": lng, "accessToken": "EAAC1mYYLrqkBAFVX4KHqZBhf9ZBTwOKtyr2x7NDP59iSkh9DiqOgXMU9xGCed2gURoBAPiLWDO7gpxNmMPPLphAmskuRCJtuvCO9w6taHZBSomoWZA8RMvXT61uytQl4ORHsogURgjMYkwHK20g78Df4ZAZCNxrk0ZD"}
    resp = requests.get(NODE_URL, params=query_d)
    return resp.text

print get_by_location("40.7447", "-73.871456")
