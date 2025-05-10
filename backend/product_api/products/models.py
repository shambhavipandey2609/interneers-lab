from django.db import models
from mongoengine import Document, StringField, FloatField, IntField, ListField, ReferenceField
# Create your models here.
class ProductCategory(Document):
    title = StringField(required=True, unique=True)
    description = StringField()
    products = ListField(ReferenceField('Product'))
    meta = {'collection': 'categories'}
    def to_dict(self):
        data = self.to_mongo().to_dict()
        # Convert ObjectId to string
        if '_id' in data:
            data['_id'] = str(data['_id'])
        return data 

class Product(Document):
    name = StringField(required=True, max_length=200, unique= True)
    description = StringField()
    price = FloatField(required=True)
    brand = StringField(required=True)
    stock = IntField(default=0)
    category = ReferenceField(ProductCategory)
    meta = {'collection': 'product_db'}
    
# Print properly formatted data    
# for item in Product.objects:
#     print(item.to_mongo().to_dict()) 

