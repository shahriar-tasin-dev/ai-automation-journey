agency_name= "Tasin's AI Lab"
agency_city= "Chittagong"
agency_goal= "Build AI automation business"
active_status= True

print(f"Agency: {agency_name}")
print(f"City: {agency_city}")
print(f"Goal: {agency_goal}")
print(f"Active: {active_status}")

services=["AI Chatbot", "Lead Generation", "AI Consulting", "AI Automation"]

print(f"First Service: {services[0]}")
print(f"Last Service: {services[-1]}")

client= {
    "name":"Hasan",
    "budget": 4000,
    "city":"Dhaka",
    "active":True
}



print(f"Client: {client["name"]}")
print(f"Budget: {client['budget']}")

clients = [
    {
        "name": "Asif",
        "budget":7000,
        "city": "Tehran",
        "active":True
    },
    {
        "name":"David",
        "city":"New York",
        "budget":9000,
        "active": True
    }
]

print(f"Second Client: {clients[1]["name"]}")