from icalendar import Calendar, Event
import requests
import json
from addEventToDB import addEvent

# install icalendar for python to work

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
TEXT_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# NYU coords
COORDS = (40.7295, 73.9965)


def sync_events():
    events_list = get_events()
    for event in events_list:
        geo = None
        if event["geo"] is not "NO LOCATION":
            geo = event["geo"]
        address = None
        if event["address"] is not "NO LOCATION":
            address = event["address"]
        addEvent(event["uid"], event["title"], event["description"], event[
                 "timeStart"], event["timeEnd"], geo, address)
    print "ical_parser: events synced"


def get_events():
    resp = requests.get(ICAL_URL)
    calFeed = Calendar.from_ical(resp.text)
    events_list = []
    for component in calFeed.walk():
        # if component.name == "VEVENT" and no
        # dbMod.check_presence(component["uid"]):
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
            # Get available location/coords, in order of preferance
            if "geo" in component:
                entry["geo"] = component["geo"].to_ical()
                entry["location"] = component["location"].to_ical()
            elif "location" in component:
                g_guess = get_gplaces_geocode(
                    component["location"].to_ical(), COORDS, 15000)
                db_address = check_building_db(component["location"].to_ical())
                if g_guess != "ERROR":
                    els = g_guess.split(";")
                    entry["geo"] = els[0] + ", " + els[1]
                    entry["location"] = els[2]
                elif db_address != "":
                    els = db_address.split(";")
                    entry["geo"] = els[0] + ", " + els[1]
                    entry["location"] = els[2]
                else:
                    entry["location"] = component["location"].to_ical()
                    entry["geo"] = "NO GEO"
                    # Add address that could not work to database
                    # dbMod.add_failed_addresses(location)
                    print "iCAL_parser ERROR: can't use address, adding to db"
            else:
                entry["location"] = "NO LOCATION"
                entry["geo"] = "NO GEO"
                print "iCAL_parser ERROR: no location given"
            # Add event to events list
            events_list.append(entry)
        # If event is already in db, not being added
    return events_list


def get_gplaces_geocode(location, coords=None, radius=None):
    # Use Google Places Autocomplete API to attempt to predict exact
    # address & coords for an inexact location
    # Returns string with "lat, long; address", or error
    query = {"input": location, "types": "geocode", "key": G_API_KEY}
    if coords is not None and radius is not None:
        query["location"] = str(coords[0]) + "," + str(coords[1])
        query["radius"] = radius
    resp = requests.get(AUTOCOMPLETE_URL, query)
    res_dict = json.loads(resp.text)
    if res_dict["status"] != "OK":
        errstr = "ERROR: get_gplaces_geocode('" + location + "') failed b/c"
        errstr += " " + res_dict["status"]
        print errstr
        return "ERROR"  # Catch-all zero resuts, quota, and other problems
    address = res_dict["predictions"][0]["description"]
    geocode = get_exact_geocode(address)
    if geocode == "ERROR":
        errstr = "ERROR: get_gplaces_geocode('" + location + "') failed b/c"
        errstr += " geocode couldn't be matched to address"
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    return geocode + ";" + address


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
        errstr = "ERROR: get_google_geocode('" + \
            true_address + "') failed b/c"
        errstr += " " + res_dict["status"]
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    lat_long = res_dict["results"][0]["geometry"]["location"]
    # print resp.text
    return str(lat_long["lat"]) + ";" + str(lat_long["lng"])


def check_building_db(name):
    # Find the coords & address for a building in the NYU db
    add_location_str = ""
    with open("utils/a.json", "r") as db:
        b_dict = json.load(db)
        for key in b_dict:
            if key in name:
                # Check if the building name is part of the address string
                add_location_str = str(b_dict[key]["lat"])
                add_location_str += ";" + str(b_dict[key]["long"])
                add_location_str += ";" + b_dict[key]["address"]
                break
    return add_location_str


"""
def get_gtext_geocode(location):
    # DOES NOT WORK FOR ADDRESSES

    # Use Google Places Autocomplete API to attempt to predict exact
    # address & coords for an inexact location
    # Returns string with "lat, long; address", or error
    query = {"query": location, "key": G_API_KEY}
    resp = requests.get(TEXT_URL, query)
    res_dict = json.loads(resp.text)
    if res_dict["status"] != "OK":
        errstr = "ERROR: get_gtext_geocode('" + location + "') failed b/c"
        errstr += " " + res_dict["status"]
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    print resp.text
    address = res_dict["results"][0]["description"]
    geocode = get_exact_geocode(address)
    if geocode == "ERROR":
        errstr = "ERROR: get_gtext_geocode('" + location + "') failed b/c"
        errstr += " geocode couldn't be matched to address"
        print errstr
        return "ERROR"  # Catch-all zero results, quota, and other problems
    return geocode + ";" + address


def get_google_address(location):
    # NOT NEEED ANYMORE

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
"""


# print get_events()
# q = "82 Washington Square East"
# print get_exact_geocode(q)
# print get_gplaces_geocode(q, COORDS, 15000)

print get_events()
