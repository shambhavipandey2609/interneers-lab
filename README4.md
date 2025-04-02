# Product & Category Management API 

## Setup and Installation ##

## 1. Clone the repository: ##
    ````
    git clone "https://github.com/shambhavipandey2609/interneers-lab.git"
    cd backend
    ````

## 2. Set up MongoDB:  ##

    Ensure MongoDB is running (or use Docker Compose if configured).

## 3. Run the Django development server: ##
    ````
    python manage.py runserver
    ````
Access the API at:
    ````
    http://127.0.0.1:8000/api/
    ````

# API Endpoints #

## Product Category Endpoints ##

1. ````POST /api/categories/ ```` - Create a new product category.

2. ````GET /api/categories/```` - Retrieve all product categories.

3. ````GET /api/categories/{category_id}/```` - Retrieve details of a specific category.

4. ````PUT /api/categories/{category_id}/````- Update an existing category.

5. ````DELETE /api/categories/{category_id}/````- Delete a category.

## Product Endpoints ##

1. ````POST /api/new-products/```` - Create a new product.

2. ````GET /api/new-products/````- Retrieve all products.

3. ````GET /api/new-products/{product_id}/```` - Retrieve details of a specific product.

4. ````PUT /api/products/{product_id}/```` - Update an existing product.

5. ````DELETE /api/products/{product_id}/```` - Delete a product.

## Category-Product Management ##

1. ````POST /api/categories/{category_id}/products/{product_id}/```` - Add a product to a category.

2. ````DELETE /api/categories/{category_id}/products/{product_id}/````- Remove a product from a category.

3. ````GET /api/categories/{category_id}/```` - List all products in a category.