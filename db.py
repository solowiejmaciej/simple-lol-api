from pymongo import MongoClient
import certifi

myclient = MongoClient(
    "mongodb+srv://maciej_solowiej:Ie0VXdGa9vld28hO@raspberrypi.rs4kf.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where()
    #"mongodb+srv://jkusiak:jkusiak@cdv.y71kg.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where()
)
mydb=myclient['LOL']
mycol=mydb['Champs']
