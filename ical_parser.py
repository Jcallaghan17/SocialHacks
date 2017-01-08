from icalendar import Calendar, Event
import requests

# Globals
ICAL_URL = "https://events.nyu.edu/live/ical/events/category/Free%20Food/header/Free%20Food%20Events"

def get_events():
    resp = requests.get(ICAL_URL)
    calFeed = Calendar.from_ical(resp.text)
    events_list = []
    for component in calFeed.walk():
        if component.name == "VEVENT":
            entry = {"title": component['summary'].to_ical(), "timeStart": component["dtstart"].to_ical(),
                     "timeEnd": component["dtend"].to_ical(), "url": component["url"],
                     "uid": component["uid"].to_ical()}
            # Get image if present
            if "x-livewhale-image" in component:
                entry["image"] = component["x-livewhale-image"].to_ical()
            # Get whatever description is present
            if "description" in component:
                entry["description"] = component["description"].to_ical()
            elif "x-livewhale-summary" in component:
                entry["description"] = component["x-livewhale-summary"].to_ical()
            # Try to get location
            if "location" in component:
                entry["location"] = component["location"].to_ical()
            else:
                entry["location"] = "NO LOCATION"
            # Try to get geolocation from iCal or Google API (if location present)
            if "geo" in component:
                entry["geo"] = component["geo"].to_ical()
            elif "location" in component:
                entry["geo"] = get_google_geo(component["location"])
            else:
                entry["geo"] = "NO LOCATION"
            # Add event to events list
            events_list.append(entry)
    return events_list

def get_google_geo(location):
    return "meow"

print get_events()
