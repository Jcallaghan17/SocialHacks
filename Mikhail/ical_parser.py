from icalendar import Calendar, Event
import requests
import json

# NOTE: get_events() is being run periodically & only returns new events
# TODO: modularize get()s
# TODO: check events for existence in database
# TODO: check if coorindates/exact address present, use those
# TODO: if not present, attempt to geocode
# NOTE: should we try assuming if direct geocoding fails?
# TODO: ask database-r to create table of faulty addresses
# TODO: add failed address into database
# TODO: save whatever location is available, ask users to correct addresses
# TODO: remind interface to check for those rare cases where location is absent

# NOTE: GEOCODE IS NOT EXACT! First choice isnt always the best for us.

# IDEA: limit geocode results using location + radius?

# Globals
ICAL_URL = "https://events.nyu.edu/live/ical/events/category/Free%20Food/header/Free%20Food%20Events"
G_API_KEY = "AIzaSyAVMs2KCYw3Qp34BEip-A-T78Nejd-J5W4"
AUTOCOMPLETE_URL = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
TEXT_URL = "https://maps.googleapis.com/maps/api/place/textsearch/output"


def get_events():
    resp = requests.get(ICAL_URL)
    calFeed = Calendar.from_ical(resp.text)
    events_list = []
    for component in calFeed.walk():
        if component.name == "VEVENT":
            entry = {"title": component['summary'].to_ical(),
                     "timeStart": component["dtstart"].to_ical(),
                     "timeEnd": component["dtend"].to_ical(),
                     "url": component["url"],
                     "uid": component["uid"].to_ical()}
            # Get image if present
            if "x-livewhale-image" in component:
                entry["image"] = component["x-livewhale-image"].to_ical()
            # Get whatever description is present
            if "description" in component:
                entry["description"] = component["description"].to_ical()
            elif "x-livewhale-summary" in component:
                entry["description"] = component[
                    "x-livewhale-summary"].to_ical()
            # Try to get location
            if "location" in component:
                entry["location"] = component["location"].to_ical()
            else:
                entry["location"] = "NO LOCATION"
            # Try to get geolocation from iCal or Google API (if location
            # present)
            if "geo" in component:
                entry["geo"] = component["geo"].to_ical()
            elif "location" in component:
                entry["geo"] = get_google_geo(component["location"])
            else:
                entry["geo"] = "NO LOCATION"
            # Add event to events list
            events_list.append(entry)
    return events_list


def get_gplaces_geocode(location):
    # Use Google Places Autocomplete API to attempt to predict exact
    # address & coords for an inexact location
    # Returns string with "lat, long; address", or error
    query = {"input": location, "types": "geocode", "key": G_API_KEY}
    resp = requests.get(AUTOCOMPLETE_URL, query)
    res_dict = json.loads(resp.text)
    if res_dict["status"] != "OK":
        errstr = "ERROR: get_gplaces_geocode('" + location + "') failed b/c"
        errstr += " " + res_dict["status"]
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    address = res_dict["predictions"][0]["description"]
    geocode = get_exact_geocode(address)
    if geocode == "ERROR":
        errstr = "ERROR: get_gplaces_geocode('" + location + "') failed b/c"
        errstr += " geocode couldn't be matched to address"
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    return geocode + ";" + address


def get_gtext_geocode(location):
    # Use
    id_query = {"input": location, "types": "geocode", "key": G_API_KEY}
    id_resp = requests.get(AUTOCOMPLETE_URL, id_query)
    print id_resp.tex
    id_res_dict = json.loads(id_resp.text)
    if id_res_dict["status"] != "OK":
        print "###########"
        return "error"  # Catch-all zero results, quota, and other problems
    res_place_id = id_res_dict["predictions"][0]["place_id"]
    print id_res_dict["predictions"][0]["description"]
    print res_place_id


def get_google_address(location):
    # Used to get a true address for an event location
    # Assumes that the first result is the correct one

    # Get true address using place_id
    add_query = {"place_id": res_place_id, "key": G_API_KEY}
    add_resp = requests.get(GEOCODE_URL, add_query)
    print add_resp.text
    add_res_dict = json.loads(add_resp.text)
    if add_res_dict["status"] != "OK":
        print "------------------------"
        # Just-in-case error check, a true problem would be near impossible
        return "error"  # Catch-all zero results, quota, and other problems
    # return the address
    # print add_resp.text
    return add_res_dict["predictions"][0]["description"]


def get_exact_geocode(true_address):
    """
        Arg: (str) an address
            If address is exact, geocoding almost guaranteed to succeed
            If inexact, most likely will fail & return error
        Returns: (str) comma-separated lat & long (on success), or "ERROR"
            on fail
    """
    query = {"address": true_address, "key": G_API_KEY}
    resp = requests.get(GEOCODE_URL, query)
    res_dict = json.loads(resp.text)
    if res_dict["status"] != "OK":
        errstr = "ERROR: get_google_geocode('" + true_address + "') failed b/c"
        errstr += " " + res_dict["status"]
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    lat_long = res_dict["results"][0]["geometry"]["location"]
    # print resp.text
    return str(lat_long["lat"]) + ", " + str(lat_long["lng"])


# print get_events()
q = "82 Washington Square E"
print get_exact_geocode(q)
print get_gplaces_geocode(q)
