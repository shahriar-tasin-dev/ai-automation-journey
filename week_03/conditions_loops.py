budget = 650
is_active = True
client_name = "Tasin Corp"


if budget >= 1000:
    print("Premium Client")
elif budget >=500:
    print("Standard Client")
else:
    print("Budget Client")

if budget >=500 and is_active:
    print(f"{client_name} is a qualified lead")
else:
    print(f"{client_name} is not qualified")


services = ["AI Automation", "Chatbot Development", "Lead Generation", "Workflow Integration"]
for i in range(len(services)):
    print(f"service {i+1}: {services[i]}")




clients = [
   {
    "name":"Hasan",
    "budget": 400,
    "city":"Dhaka",
    "active":True
},
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

for client in clients:
    print(f"Client: {client['name']} | Budget: {client['budget']} | City: {client['city']}")

    if client["budget"] >=500:
        print(f"QUALIFIED: {client['name']}")

    else:
        print(f"NOT QUALIFIED: {client['name']}")

