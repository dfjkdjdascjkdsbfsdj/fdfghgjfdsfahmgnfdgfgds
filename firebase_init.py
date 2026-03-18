# firebase_init.py
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://reseller-panel-d376c-default-rtdb.firebaseio.com/"
})
