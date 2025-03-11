## Product API (In-Memory) using Django REST Framework

This is a simple **in-memory Product API built using Django REST Framework (DRF)**. It allows users to create, retrieve, update, and delete products without using a database.

# Features

1. Create a Product (POST /api/products/)

2. Retrieve All Products (GET /api/products/)

3. Retrieve a Product by ID (GET /api/products/id/)

4. Update a Product (PUT /api/products/id/)

5. Delete a Product (DELETE /api/products/id/)
---
# Prerequisites

Ensure you have Python 3 installed on your system.

# Installation and Setup

1. Clone the Repository
```
git clone https://github.com/shambhavipandey2609/interneers-lab.git
cd interneers-lab
```
2. Create a Project Directory and Set Up Virtual Environment
```
mkdir product_api  # Create a project directory
cd product_api  # Navigate into the directory
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate it (Mac/Linux)
venv\Scripts\activate  # Activate it (Windows)
``` 
3. Install Dependencies
```
pip install django djangorestframework
```
4. Create Django Project and App
```
django-admin startproject productapi .  # Create a Django project
python manage.py startapp products  # Create a Django app
```
5. Run Migrations
```
python manage.py migrate
```
6. Start the server
```
python manage.py runserver
```
---
# API Endpoints

1. Create a Product

POST ```/api/products/```

Request Body:
```
{
    "name": "Laptop",
    "description": "Gaming Laptop",
    "category": "Electronics",
    "price": 1200,
    "brand": "Dell",
    "quantity": 5
}
```
Response:
```
{
    "id": 1,
    "name": "Laptop",
    "description": "Gaming Laptop",
    "category": "Electronics",
    "price": 1200,
    "brand": "Dell",
    "quantity": 5
}
```
2. Retrieve All Products

GET ```/api/products/```

Request Body:
```
{
    "name": "Laptop",
    "description": "Gaming Laptop",
    "category": "Electronics",
    "price": 1200,
    "brand": "Dell",
    "quantity": 5
}
```
Response:
```
{
    "id": 1,
    "name": "Laptop",
    "description": "Gaming Laptop",
    "category": "Electronics",
    "price": 1200,
    "brand": "Dell",
    "quantity": 5
}
```
3. Retrieve a Product by ID

GET ```/api/products/1/```

Response:
```
{
    "id": 1,
    "name": "Laptop",
    "description": "Gaming Laptop",
    "category": "Electronics",
    "price": 1200,
    "brand": "Dell",
    "quantity": 5
}
```
4. Update a Product

PUT ```/api/products/1/```

Request Body:
```
{
    "price": 1100,
    "quantity": 3
}
```
Response:
```
{
    "id": 1,
    "name": "Laptop",
    "description": "Gaming Laptop",
    "category": "Electronics",
    "price": 1100,
    "brand": "Dell",
    "quantity": 3
}
```
5. Delete a Product

DELETE ```/api/products/1/```

Response:
```
{
    "message": "Product deleted successfully"
}
```
Pushing Changes to GitHub

Once you've set up the project and made modifications, push changes to GitHub:
```
git add .
git commit -m "Added Django REST in-memory product API"
git push origin main
```
