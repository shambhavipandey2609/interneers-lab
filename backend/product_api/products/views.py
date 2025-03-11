from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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
