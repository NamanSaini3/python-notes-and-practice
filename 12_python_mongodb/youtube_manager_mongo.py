from pymongo import MongoClient

# Connect to MongoDB
# import pymongo



client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.jvlihyv.mongodb.net/ytmanger")

# Not a good idea to include id and password in the code, but for this example, we will do it anyway. 
# In a real application, you should use environment variables or a configuration file to store sensitive information.


db = client["ytmanger"]