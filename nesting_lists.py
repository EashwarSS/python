capitals = {
    "India": "Delhi",
    "Bangladesh": "Dhaka",
    "Pakistan": "Karachi"
}

# Nested List in Dictionary
travel_log = {
    "India": ["Tajmahal", "Charminar", "Goa"],
    "Pakistan": ["Lahore Fort", "Badshahi Mosque", "Hunza Valley"]
}

print(travel_log["India"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2])
print(nested_list[2][1])