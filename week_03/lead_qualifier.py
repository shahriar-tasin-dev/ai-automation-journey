clients = [
    {"name": "Kawser", "budget": 2300, "city": "Dhaka", "active": True},
    {"name": "Asif", "budget": 700, "city": "Tehran", "active": True},
    {"name": "David", "budget": 9000, "city": "New York", "active": False},
    {"name": "Sarah", "budget": 100, "city": "Los Angeles", "active": True},
    {"name": "John", "budget": 800, "city": "Chicago", "active": False},
]

for client in clients:
    print(f"Client: {client['name']} | Budget: {client['budget']} | City: {client['city']} | Active: {client['active']}")
    
    if client["budget"] >= 1000 and client["active"]:
        print(f"TIER 1 - Premium proposal")
    elif client["budget"] >= 500 and client["active"]:
        print(f"TIER 2 - Standard proposal")
    elif client["budget"] >= 200 and client["active"]:
        print(f"TIER 3 - Basic proposal")
    elif client["active"] == False:
        print(f"Inactive client - Do not contact")
    elif client["budget"] < 200:
        print(f"TOO LOW - skip")