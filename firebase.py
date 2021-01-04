# Imports
#-------------------------------------------------------------------------------
import pyrebase

# Config/Setup
#-------------------------------------------------------------------------------
firebaseConfig = {
    "apiKey": "YOUR_apiKey_HERE",
    "authDomain": "YOUR__HERE",
    "projectId": "YOUR_projectId_HERE",
    "databaseURL": "YOUR_databaseURL_HERE",
    "storageBucket": "YOUR_storageBucket_HERE",
    "messagingSenderId": "YOUR_messagingSenderId_HERE",
    "appId": "YOUR_appId_HERE",
    "measurementId": "YOUR_measurementId_HERE"
 };
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data = {"Age": 21, "Name": "Jenna", "Employed": True}
#-------------------------------------------------------------------------------
# Create Data

db.push(data)
db.child("Users").child("FirstPerson").set(data)

#-------------------------------------------------------------------------------
# Read Data

jenna = db.child("Users").child("FirstPerson").get()
print(jenna.val())
#-------------------------------------------------------------------------------
# Update Data

db.child("Users").child("FirstPerson").update({"Name": "Larry"})

#-------------------------------------------------------------------------------
# Remove Data

#Delete 1 Value
db.child("Users").child("FirstPerson").child("Age").remove()

# Delete whole Node
db.child("Users").child("FirstPerson").remove()

#-------------------------------------------------------------------------------
