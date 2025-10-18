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
# users = [
#     {"_id": 1, "name": "Aarav", "age": 23, "email": "aarav23@gmail.com", "city": "Kochi"},
#     {"_id": 2, "name": "Diya", "age": 21, "email": "diya21@yahoo.com", "city": "Trivandrum"},
#     {"_id": 3, "name": "Rahul", "age": 25, "email": "rahul25@gmail.com", "city": "Kozhikode"},
#     {"_id": 4, "name": "Neha", "age": 22, "email": "neha22@outlook.com", "city": "Thrissur"},
#     {"_id": 5, "name": "Vishnu", "age": 24, "email": "vishnu24@gmail.com", "city": "Aluva"},
#     {"_id": 6, "name": "Sneha", "age": 20, "email": "sneha20@yahoo.com", "city": "Kottayam"},
#     {"_id": 7, "name": "Aditya", "age": 23, "email": "aditya23@gmail.com", "city": "Palakkad"},
#     {"_id": 8, "name": "Meera", "age": 26, "email": "meera26@hotmail.com", "city": "Ernakulam"},
#     {"_id": 9, "name": "Arjun", "age": 22, "email": "arjun22@gmail.com", "city": "Kannur"},
#     {"_id": 10, "name": "Lakshmi", "age": 24, "email": "lakshmi24@gmail.com", "city": "Alappuzha"}
# ]
# x=mycol.insert_many(users)
data=mycol.find_one({'email':'lakshmi24@gmail.com'})
# for i in data:
#     print(i)
print(data)
