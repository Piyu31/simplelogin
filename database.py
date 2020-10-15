from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://priyanka:piyu31@cluster0.mdba4.mongodb.net/Users?retryWrites=true&w=majority')
db = client.Users
collection = db.Details

def adduser(newuser):
    collection.insert(newuser)

def verifylogin(email,password):
    user = collection.find_one({"email":email})
 
    try: 
        return user['password'] == password
    except:
        return False

def verifyemail(email): 
    count = collection.find({"email":email}).count()
    return count == 0 

  
