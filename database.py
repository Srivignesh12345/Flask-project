from flask_mongoengine import MongoEngine

mydata=MongoEngine()

url="mongodb+srv://Srivignesh:sri12345*@cluster0.2pgxwru.mongodb.net/Srivignesh?retryWrites=true&w=majority"

class laptop(mydata.Document):
   model=mydata.StringField()
   serial=mydata.StringField()
   ram=mydata.IntField()
   ssd=mydata.IntField()
   stock=mydata.IntField()
   price=mydata.IntField()
   type=mydata.StringField()