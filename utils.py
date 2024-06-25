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
        0: "bonnet dent",
        1: "boot dent",
        2: "doorouter dent",
        3: "fender dent",
        4: "front bumper dent",
        5: "Front windscreen damage",
        6: "Headlight Damage",
        7: "quaterpanel dent",
        8: "rear bumper dent",
        9: "Rear windscreen Damage",
        10: "roof dent",
        11: "Runningboard Damage",
        12: "Sidemirror Damage",
        13: "Taillight Damage"
    }

    price_mapping = {
        "bonnet dent": 4000,
        "boot dent": 3500,
        "doorouter dent": 4500,
        "fender dent": 5000,
        "front bumper dent": 6000,
        "Front windscreen damage": 7000,
        "Headlight Damage": 3000,
        "quaterpanel dent": 5500,
        "rear bumper dent": 6500,
        "Rear windscreen Damage": 7500,
        "roof dent": 4000,
        "Runningboard Damage": 5000,
        "Sidemirror Damage": 2000,
        "Taillight Damage": 2500
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
