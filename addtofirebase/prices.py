import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (only once in your application)
if not firebase_admin._apps:
    cred = credentials.Certificate(r"vehicle-damage-detection-d0828-firebase-adminsdk-gpwij-85174bc76a.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def add_brand_damage_prices(brand, damage_prices):
    # Add a new document for each brand with its price mapping
    doc_ref = db.collection('damage_prices').document(brand)
    doc_ref.set({
        'brand': brand,
        'damage_prices': damage_prices
    })
    print(f"Added/Updated prices for {brand}")

# Example: Add prices for Honda and Toyota
if __name__ == "__main__":
    honda_prices = {
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
    
    toyota_prices = {
        "Bonnet Dent/Damage": 5700,
        "Boot Dent/Damage": 6200,
        "Door Outer Panel Dent": 4600,
        "Fender Dent/Damage": 5200,
        "Front Bumper Damage": 6300,
        "Front Windshield Damage": 5200,
        "Headlight Assembly Damage": 6200,
        "Quarter Panel Dent/Damage": 5700,
        "Rear Bumper Damage": 4700,
        "Rear Windshield Damage": 4200,
        "Roof Dent/Damage": 3700,
        "Running Board Damage": 4200,
        "Side Mirror Damage": 4200,
        "Taillight Assembly Damage": 5200
    }

    add_brand_damage_prices("Honda", honda_prices)
    add_brand_damage_prices("Toyota", toyota_prices)
