capitals = {
    "India": "Delhi",
    "Bangladesh": "Dhaka",
    "Pakistan": "Karachi"
}

# Nested List in Dictionary
travel_log = {
    "India": {
        "cities_visited": ["Tajmahal", "Charminar", "Goa"],
        "total_visits": 12
    },
    "Pakistan": {
        "cities_visited": ["Lahore Fort", "Badshahi Mosque", "Hunza Valley"],
        "total_visits": 5
    },
}

print(travel_log["India"]["cities_visited"])