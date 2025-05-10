from django.contrib import admin
from django.urls import path,include
from django.http import JsonResponse 

def hello_name(request):
    """""
    A simple view that returns 'Hello, {name}' in JSON format.
    Uses a query parameter named 'name'.
    """
    # Get 'name' from the query string, default to 'World' if missing
    name = request.GET.get("name", "World")
    greeting =request.GET.get("greeting","Hello")
    return JsonResponse({"message": f"{greeting}, {name}!"})

def Bye_name(request):
    name = request.GET.get("name", "World")
    greeting=request.GET.get("greeting","Bye")
    return JsonResponse({"message": f"{greeting}, {name}!"})


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', hello_name), 
    path('Bye/',Bye_name),
    path("", include("product_api.productapi.urls")),
    # Example usage: /hello/?name=Bob
    # returns {"message": "Hello, Bob!"}
]
