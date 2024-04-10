# import firebase_admin
# from firebase_admin import firestore
# from google.cloud.firestore_v1.base_query import FieldFilter
# import math


# if not firebase_admin._apps:
#     firebase_admin.initialize_app()

# db = firestore.client()

# cities_ref = db.collection("houses")
# query = cities_ref.limit(6)
# results = query.stream()

# outputArray = []
# outputDict = {}


# def replace_nan_with_empty(dict):
#     for key, value in dict.items():
#         if value == float("nan"):
#             dict[key] = 0
#     return dict


# for doc in results:
#     # val = json.dumps(doc.to_dict())
#     # outputArray.append(doc.to_dict())
#     test = replace_nan_with_empty(doc.to_dict())
#     outputArray.append(test)
#     outputDict["data"] = outputArray

# print("tets")
