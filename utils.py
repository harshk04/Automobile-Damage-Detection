import firebase_admin
from firebase_admin import credentials, firestore

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

def fetch_car_brand_prices(brand):
    """Fetches price mappings for car parts based on the car's brand from Firestore."""
    collection_ref = db.collection('damage_prices')  # Updated collection name from 'car_brand_prices' to 'damage_prices'

    if not isinstance(brand, str):
        raise TypeError(f"Expected 'brand' to be a string, but got {type(brand)}")
    
    brand = brand.strip()  # Strip whitespace just in case
    
    print(f"Fetching prices for brand: {brand}")  # Debugging line
    
    doc_ref = collection_ref.document(brand)
    doc = doc_ref.get()

    if doc.exists:
        return doc.to_dict().get('damage_prices', {})  # Ensure we're fetching 'damage_prices'
    else:
        raise ValueError(f"No price data found for brand: {brand}")


def calculate_damage_estimation(prediction_json, price_mapping):
    """
    Calculates the total damage cost based on the prediction JSON and price mapping.
    The prediction_json contains parts and their damage level, while price_mapping contains
    part names and their associated prices.
    """
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

    total_price = 0
    price_details = []

    predictions = prediction_json['predictions']

    for pred in predictions:
        confidence = round(pred['confidence'], 3)
        class_id = int(pred['class'])
        class_name = class_mapping.get(class_id, "Unknown")
        price = price_mapping.get(class_name, 0)
        calculated_price = price * confidence
        total_price += calculated_price
        price_details.append((confidence, class_name, calculated_price))

    return total_price, price_details
