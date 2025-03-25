from django.db import models
from mongoengine import Document, StringField, FloatField, IntField
# Create your models here.
class Product(Document):
    name = StringField(required=True, max_length=200)
    description = StringField()
    price = FloatField(required=True)
    stock = IntField(default=0)
    meta = {'collection': 'product_db'}

# Print properly formatted data    
for item in Product.objects:
    print(item.to_mongo().to_dict())    