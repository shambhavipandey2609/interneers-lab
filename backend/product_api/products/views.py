from django.shortcuts import render
from mongoengine import connect
from mongoengine.errors import DoesNotExist
from bson import ObjectId
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import ProductService, ProductCategoryService
from .models import Product, ProductCategory
# In-memory storage
products = []
product_id = 1  # Auto-incremented ID

class ProductList(APIView):
    def get(self, request):
        return Response(products, status=status.HTTP_200_OK)

    def post(self, request):
        global product_id
        data = request.data

        # Basic validation
        required_fields = ["name", "description", "category", "price", "brand", "quantity"]
        for field in required_fields:
            if field not in data:
                return Response({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not isinstance(data["price"], (int, float)) or data["price"] < 0:
            return Response({"error": "Invalid price"}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(data["quantity"], int) or data["quantity"] < 0:
            return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)

        new_product = {
            "id": product_id,
            "name": data["name"],
            "description": data["description"],
            "category": data["category"],
            "price": data["price"],
            "brand": data["brand"],
            "quantity": data["quantity"],
        }
        product_id += 1
        products.append(new_product)
        return Response(new_product, status=status.HTTP_201_CREATED)

class ProductDetail(APIView):
    def get(self, request, pk):
        product = next((p for p in products if p["id"] == pk), None)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(product)

    def put(self, request, pk):
        product = next((p for p in products if p["id"] == pk), None)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        product.update({key: data[key] for key in data if key in product})
        return Response(product)

    def delete(self, request, pk):
        global products
        products = [p for p in products if p["id"] != pk]
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_200_OK)

class ProductView(APIView):
    def get(self, request, product_id=None):  
        if product_id:  # If an ID is provided, fetch a single product
            try:
                product = Product.objects.get(id=product_id)  # Fetch by ID

                # Safe category retrieval
                category_title = None
                if product.category and product.category.id:
                    try:
                        category = ProductCategory.objects.get(id=product.category.id)
                        category_title = category.title
                    except DoesNotExist:
                        category_title = None  # Category reference is broken

                product_data = {
                    "id": str(product.id),
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "category": category_title,  # Avoids DBRef dereferencing issues
                    "brand": product.brand,
                    "stock": product.stock,
                }
                return Response(product_data, status=status.HTTP_200_OK)

            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # If no ID is provided, return all products
        products = Product.objects.all()
        product_list = []

        for product in products:
            #Safe category retrieval
            category_title = None
            if product.category and product.category.id:
                try:
                    category = ProductCategory.objects.get(id=product.category.id)
                    category_title = category.title
                except DoesNotExist:
                    category_title = None  

            product_list.append({
                "id": str(product.id),
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category": category_title,  # ✅ Avoids DBRef dereferencing issues
                "brand": product.brand,
                "stock": product.stock,
            })

        return Response(product_list, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()

        # Validate "brand" (Required field)
        if not data.get("brand"):
            return Response({"error": "Brand is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Handle "category" field
        if "category" in data:
            try:
                data["category"] = ObjectId(data["category"])  # Convert string to ObjectId
            except Exception:
                return Response({"error": "Invalid category ID."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data["category"] = None  # Default to None if category is not provided

        # Create product and convert data for response
        product = ProductService.create_product(data)
        product_data = product.to_mongo().to_dict()

        # Convert ObjectIds to strings for JSON response
        product_data["_id"] = str(product_data["_id"])
        if product_data.get("category"):
            product_data["category"] = str(product_data["category"])

        return Response(product_data, status=status.HTTP_201_CREATED)
    def put(self, request, product_id):
        updated_product = ProductService.update_product(product_id, request.data)
        if not updated_product:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        data = updated_product.to_mongo().to_dict()
        data["_id"] = str(data["_id"])  # Convert ObjectId to string
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, product_id):
        success = ProductService.delete_product(product_id)
        return Response(status=status.HTTP_204_NO_CONTENT) if success else Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    



class ProductCategoryListView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        print(categories)

        category_list = [
            {
                "id": str(category.id),
                "title": category.title,
                "description": category.description,
                "products": [
                    {
                        "id": str(product.id),
                        "name": product.name,
                        "description": product.description,
                        "price": product.price,
                        "brand": product.brand
                    }
                    for product in Product.objects(id__in=[ObjectId(p.id) for p in category.products])  # Fetch actual Product objects
                ]
            }
            for category in categories
        ]

        return Response(category_list)

    def post(self, request):
        category = ProductCategoryService.create_category(
            request.data.get("title"), request.data.get("description")
        )

        data = category.to_mongo().to_dict()
        data["_id"] = str(data["_id"])  # Convert ObjectId to string
        return Response(data, status=201)

class ProductCategoryDetailView(APIView):
    def get(self, request, category_id):
        category = ProductCategory.objects(id=category_id).first()
        if not category:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

        category_data = {
            "id": str(category.id),  # Convert ObjectId to string
            "title": category.title,
            "description": category.description,
            "products": [
                {
                    "id": str(product.id),
                    "name": product.name,
                    "description": product.description,  # Add more details if needed
                    "price": product.price,
                    "brand" : product.brand
                }
                for product in category.products
            ]
        }
        return Response(category_data, status=status.HTTP_200_OK)


    def put(self, request, category_title):
        data = request.data
        category = ProductCategoryService.update_category_by_title(category_title, data["title"], data.get("description", ""))
        
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        category_dict = category.to_mongo().to_dict()
        category_dict["_id"] = str(category_dict["_id"])  # Convert ObjectId to string
        
        return Response(category_dict, status=status.HTTP_200_OK)


    def delete(self, request, category_id):
        deleted = ProductCategoryService.delete_category(category_id)
        return Response({"deleted": bool(deleted)}, status=status.HTTP_204_NO_CONTENT)


class AddRemoveProductToCategoryView(APIView):
    def get(self, request, category_id, product_id):
        category = ProductCategory.objects(id=category_id, products=product_id).first()
        if not category:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)

        # product = next((p for p in category.products if str(p.id) == product_id), None)
        return Response({"product_id": product_id, "message": "Product exists in this category."}, status=status.HTTP_200_OK)

    def post(self, request, category_id, product_id):
        category = ProductCategory.objects(id=category_id).first()
        product = Product.objects(id=product_id).first()

        if not category:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        if not product:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        if product not in category.products:
            category.products.append(product)
            product.category = category
            category.save()
            product.save()
            return Response({"message": "Product added to category."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Product is already in this category."}, status=status.HTTP_200_OK)

    def delete(self, request, category_id, product_id):
        category = ProductCategory.objects(id=category_id).first()
        product = Product.objects(id=product_id).first()

        if not category:
            return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        if not product:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        if product in category.products:
            category.products.remove(product)
            product.category = None
            category.save()
            product.save()
            return Response({"message": "Product removed from category."}, status=status.HTTP_200_OK)
        return Response({"message": "Product not found in this category."}, status=status.HTTP_404_NOT_FOUND)