# Product Service with MongoDB and Docker #

## Setup and Installation ##

1️. Install Dependencies
  Ensure you have Docker and Python 3.x installed.

2️. Clone the Repository
```
  $ git clone https://github.com/shambhavipandey2609/interneers-lab.git
  $ cd backend
```
3.Run MongoDB with Docker Compose
```
$ docker-compose up -d mongodb
```
This will start a MongoDB container that the Python service will connect to.

4️. Set Up Python Virtual Environment
```
$ python -m venv venv
$ source venv/bin/activate  # On Windows use: venv\Scripts\activate
$ pip install -r requirements.txt
```
5️. Define MongoDB Connection in Python

Modify settings.py to connect to the running MongoDB container:
```
from mongoengine import connect
connect(db="productdb", host="mongodb://localhost:27017/productdb")
```
6️. Create MongoEngine Models

Example models.py:
```
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
```
7️. Implement Repository Layer

Example repository.py:
```
from .models import Product

class ProductRepository:
    @staticmethod
    def create_product(data):
        product = Product(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            stock=data.get("stock")
        )
        product.save()
        return product

    @staticmethod
    def get_all_products():
        return list(Product.objects)

    @staticmethod
    def get_product_by_id(product_id):
        return Product.objects(id=product_id).first()

    @staticmethod
    def update_product(product_id, data):
        product = Product.objects(id=product_id).first()
        if product:
            product.name = data.get("name", product.name)
            product.description = data.get("description", product.description)
            product.price = data.get("price", product.price)
            product.stock = data.get("stock", product.stock)
            product.save()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = Product.objects(id=product_id).first()
        if product:
            product.delete()
            return True
        return False
```
8️. Implement ProductService Layer

Example service.py:
```
from .repository import ProductRepository

class ProductService:
    @staticmethod
    def create_product(data):
        return ProductRepository.create_product(data)

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def update_product(product_id, data):
        return ProductRepository.update_product(product_id, data)

    @staticmethod
    def delete_product(product_id):
        return ProductRepository.delete_product(product_id)
```
9️. Create API Endpoints

in urls.py in products:
```
from django.urls import path
from .views import ProductList, ProductDetail, ProductView

urlpatterns = [
    path("products/", ProductList.as_view(), name="product-list"),  # /api/products/
    path("products/<int:pk>/", ProductDetail.as_view(), name="product-detail"),  # /api/products/<id>/

    #week3 for mongodb
    path("new-products/",ProductView.as_view(),name="new-product"),
    path("new-products/<str:product_id>/",ProductView.as_view(),name="new-product"),
]

```
10. Test API Calls

Run the server:
```
python manage.py runserver
```
Then test with Postman or cURL:
```
curl -X POST "http://127.0.0.1:8000/api/new-products"
```
View Data in MongoDB Compass

Connect to MongoDB Compass at mongodb://localhost:27017.

Browse product_db to verify stored products.

# Summary #

Run MongoDB using Docker Compose

Set up MongoDB connection in Python

Create models using MongoEngine

Implement repository & service layers

Develop API endpoints using Flask

Test API calls and analyze data in Compass


