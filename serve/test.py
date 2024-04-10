import firebase_admin
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import json


if not firebase_admin._apps:
    firebase_admin.initialize_app()

db = firestore.client()

cities_ref = db.collection("houses")
query = cities_ref.limit(6)
results = query.stream()

outputArray = []
outputDict = {}

for doc in results:
    # val = json.dumps(doc.to_dict())
    outputArray.append(doc.to_dict())

    outputDict["data"] = outputArray
