import pymongo
from urllib.parse import quote_plus
raw_psw='fathaah@123'
username='mohammedfathaah_db_user'
password=quote_plus(raw_psw)

uri=f'mongodb+srv://{username}:{password}@cluster0.xcwigfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
myclient=pymongo.MongoClient(uri)
print(myclient)
mydb=myclient['mydatabase']
mycol=mydb['mycollection']
# mydata={'name':'nihal','age':21,'course':'wordpress'}
# x=mycol.insert_one(mydata)
users = [
    {"name": "Aarav", "age": 23, "email": "aarav23@gmail.com", "city": "Kochi"},
    {"name": "Diya", "age": 21, "email": "diya21@yahoo.com", "city": "Trivandrum"},
    {"name": "Rahul", "age": 25, "email": "rahul25@gmail.com", "city": "Kozhikode"},
    {"name": "Neha", "age": 22, "email": "neha22@outlook.com", "city": "Thrissur"},
    {"name": "Vishnu", "age": 24, "email": "vishnu24@gmail.com", "city": "Aluva"},
    {"name": "Sneha", "age": 20, "email": "sneha20@yahoo.com", "city": "Kottayam"},
    {"name": "Aditya", "age": 23, "email": "aditya23@gmail.com", "city": "Palakkad"},
    {"name": "Meera", "age": 26, "email": "meera26@hotmail.com", "city": "Ernakulam"},
    {"name": "Arjun", "age": 22, "email": "arjun22@gmail.com", "city": "Kannur"},
    {"name": "Lakshmi", "age": 24, "email": "lakshmi24@gmail.com", "city": "Alappuzha"}
]
x=mycol.insert_many(users)
data=mycol.find()
for i in data:
    print(i)
# print(data)
print('-'*60)
# mydata=mycol.find().sort('age',-1)
# for i in mydata:
#     print(i)
# myquery={'email':'aarav23@gmail.com'}
# newvalue={"$set":{'name':'naruto'}}
# mycol.update_many(myquery,newvalue)
# data=mycol.find()
# for i in data:
#     print(i)

# myquery={'email':'aarav23@gmail.com'}
# mycol.delete_many(myquery)
# for i in mycol.find():
#     print(i)

mycol.delete_many({})
print('document is deleted')