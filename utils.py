import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (only once in your application)
if not firebase_admin._apps:
    cred = credentials.Certificate(r"automobile-damage-detection-firebase-adminsdk-k160e-9e5d21ccf0.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def fetch_car_data(car_number):
    collection_ref = db.collection("cardata")
    query = collection_ref.where('Registration', '==', car_number).limit(1)
    results = query.stream()

    for doc in results:
        return doc.to_dict()

    return None

def fetch_all_car_data():
    collection_ref = db.collection("cardata")
    docs = collection_ref.stream()
    car_data = [doc.to_dict() for doc in docs]
    return car_data

def add_car_data(car_data):
    doc_ref = db.collection('cardata').document()
    doc_ref.set(car_data)





def calculate_damage_estimation(prediction_json):
    class_mapping = {
        0: "Bonnet Dent/Damage",
        1: "Boot Dent/Damage",
        2: "Door Outer Panel Dent",
        3: "Fender Dent/Damage",
        4: "Front Bumper Damage",
        5: "Front Windshield Damage",
        6: "Headlight Assembly Damage",
        7: "Quarter Panel Dent/Damage",
        8: "Rear Bumper Damage",
        9: "Rear Windshield Damage",
        10: "Roof Dent/Damage",
        11: "Running Board Damage",
        12: "Side Mirror Damage",
        13: "Taillight Assembly Damage"
    }

    price_mapping = {
        "Bonnet Dent/Damage": 5500,
        "Boot Dent/Damage": 6000,
        "Door Outer Panel Dent": 4500,
        "Fender Dent/Damage": 5000,
        "Front Bumper Damage": 6000,
        "Front Windshield Damage": 5000,
        "Headlight Assembly Damage": 6000,
        "Quarter Panel Dent/Damage": 5500,
        "Rear Bumper Damage": 4500,
        "Rear Windshield Damage": 4000,
        "Roof Dent/Damage": 3500,
        "Running Board Damage": 4000,
        "Side Mirror Damage": 4000,
        "Taillight Assembly Damage": 5000
    }


    predictions = prediction_json['predictions']
    total_price = 0
    price_details = []

    for pred in predictions:
        confidence = round(pred['confidence'], 3)
        class_id = int(pred['class'])  # Convert class to integer
        class_name = class_mapping.get(class_id, "Unknown")
        price = price_mapping.get(class_name, 0)
        calculated_price = price * confidence
        total_price += calculated_price
        price_details.append((confidence, class_name, calculated_price))

    return total_price, price_details
