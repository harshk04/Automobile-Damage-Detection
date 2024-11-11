import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (only once in your application)
if not firebase_admin._apps:
    cred = credentials.Certificate(r"vehicle-damage-detection-d0828-firebase-adminsdk-gpwij-85174bc76a.json")
    firebase_admin.initialize_app(cred)

# Get the Firestore client
db = firestore.client()

# Data for 10 vehicles
vehicles_data = [
    {
        "Car Brand": "Honda",
        "Car Price": 150000,
        "Colour": "Brown",
        "Fuel": "Petrol",
        "Model": "City",
        "Registration": "RJ14CH2439",
        "Type": "Sedan",
        "Year of Manufacture": 2009
    },
    {
        "Car Brand": "Hyundai",
        "Car Price": 85000,
        "Colour": "Golden",
        "Fuel": "Petrol",
        "Model": "i-10",
        "Registration": "RJ02CA4571",
        "Type": "Hatchback",
        "Year of Manufacture": 2009
    },
    {
        "Car Brand": "Ford",
        "Car Price": 65000,
        "Colour": "Blue",
        "Fuel": "Diesel",
        "Model": "Fiesta",
        "Registration": "MH20BC5124",
        "Type": "Hatchback",
        "Year of Manufacture": 2016
    },
    {
        "Car Brand": "Hyundai",
        "Car Price": 70000,
        "Colour": "Grey",
        "Fuel": "Petrol",
        "Model": "i20",
        "Registration": "MH20BC5125",
        "Type": "Hatchback",
        "Year of Manufacture": 2015
    },
    {
        "Car Brand": "Maruti",
        "Car Price": 50000,
        "Colour": "Silver",
        "Fuel": "Petrol",
        "Model": "Swift",
        "Registration": "MH20BC5126",
        "Type": "Hatchback",
        "Year of Manufacture": 2014
    },
    {
        "Car Brand": "Nissan",
        "Car Price": 55000,
        "Colour": "Black",
        "Fuel": "Diesel",
        "Model": "Sunny",
        "Registration": "MH20BC5127",
        "Type": "Sedan",
        "Year of Manufacture": 2013
    },
    {
        "Car Brand": "Chevrolet",
        "Car Price": 60000,
        "Colour": "Red",
        "Fuel": "Petrol",
        "Model": "Spark",
        "Registration": "MH20BC5128",
        "Type": "Hatchback",
        "Year of Manufacture": 2012
    },
    {
        "Car Brand": "Renault",
        "Car Price": 72000,
        "Colour": "Green",
        "Fuel": "Diesel",
        "Model": "Duster",
        "Registration": "MH20BC5129",
        "Type": "SUV",
        "Year of Manufacture": 2019
    },
    {
        "Car Brand": "Volkswagen",
        "Car Price": 95000,
        "Colour": "Yellow",
        "Fuel": "Petrol",
        "Model": "Polo",
        "Registration": "MH20BC5130",
        "Type": "Hatchback",
        "Year of Manufacture": 2020
    },
    {
        "Car Brand": "Skoda",
        "Car Price": 98000,
        "Colour": "White",
        "Fuel": "Diesel",
        "Model": "Rapid",
        "Registration": "MH20BC5131",
        "Type": "Sedan",
        "Year of Manufacture": 2021
    }
]

# Add each vehicle to Firestore with the registration number as the document ID
for vehicle in vehicles_data:
    registration_id = vehicle["Registration"]  # Use registration as document ID
    doc_ref = db.collection("cardata").document(registration_id)
    doc_ref.set(vehicle)
    print(f"Data for {registration_id} added successfully.")
