from peewee import *
import datetime

db = SqliteDatabase('betsy.db')

# User info 
       
class Address(Model):
    streetname = CharField()
    number = IntegerField()
    number_add = CharField(max_length=4, null=True, default="")
    zipcode = CharField()
    city = CharField()
    country = CharField()

    class Meta:
        database = db
        
        
class BillInfo(Model): 
    billing_address = ForeignKeyField(Address)
    iban = CharField()
    
    class Meta:
        database = db
    
class User(Model):
    fullname = CharField(max_length=100, unique=True)
    address = ForeignKeyField(Address)
    billing_info = ForeignKeyField(BillInfo)
    
    class Meta:
        database = db
 
class Product(Model):
    owner = ForeignKeyField(User, backref='products', default="none")
    name = CharField(primary_key=True, unique=True)
    description = TextField()
    price_per_product = DecimalField(decimal_places=2)
    quantity = IntegerField()

    class Meta:
        database = db
        
class Tag(Model):
    name = CharField(primary_key=True, unique=True)
    
    class Meta:
        database = db
        
        
class TagHanger(Model):
    tagged = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)
    
    class Meta:
        database = db

        
    
# transactionmodel

class TransactionDetail(Model):
    transaction_date = DateTimeField(default=datetime.datetime.now)
    buyer = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    quantity = IntegerField()  
    
    class Meta:
        database = db