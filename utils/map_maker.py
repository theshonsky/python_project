import os
import json
from collections import deque

from locations.location import Location

MAP_FILE_PATH = "./map.json"

def search_location_in_dict(location, seach_title):
    """search location in dict by title BFS"""
    
    queue = deque([location])
    while queue:
        current_location = queue.popleft()
        if current_location["title"] == seach_title:
            return current_location
        queue.extend(current_location["locations"])
    return None
    
    

def get_location_from_console(location: Location):
    current_location_title = input("Enter location title: ")
    new_location_title = input("Enter new location title: ")
    new_location = Location(title=new_location_title, locations=[])
    l = search_location_in_dict(location, current_location_title)
    if l:
        l["locations"].append(new_location.to_dict())
        l["previous_location"] = current_location_title
    else:
        raise ValueError("Location not found")

def map_maker():
    map = Location(locations=[])
    if os.path.isfile(MAP_FILE_PATH):
        with open(MAP_FILE_PATH, "r") as f:
            map = json.load(f)
            get_location_from_console(map)
        with open(MAP_FILE_PATH, "w") as f:
            json.dump(map, f, indent=2)

    else:
        with open(MAP_FILE_PATH, "w") as f:
            json.dump(map.to_dict(), f, indent=2)
