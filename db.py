from pymongo import MongoClient
import certifi

myclient = MongoClient(
    "mongodb+srv:/username:password@raspberrypi.rs4kf.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where()

)
mydb=myclient['LOL']
mycol=mydb['Champs']
