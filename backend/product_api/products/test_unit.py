from django.test import TestCase
from .models import Product, ProductCategory
from .repository import ProductRepository
from django.test import TestCase


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product(name="Test", price=10.0, stock=5)
        self.assertEqual(product.name, "Test")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.stock, 5)

class ProductRepositoryTest(TestCase):
    def setUp(self):
        Product.objects.delete() 
    def test_create_product_success(self):
        data = {
            "name": "Phone",
            "description": "Smartphone",
            "price": 499.99,
            "brand": "XYZ",
            "stock": 50,
            "category": None,
        }
        product = ProductRepository.create_product(data)
        self.assertEqual(product.name, "Phone")
        self.assertEqual(product.description, "Smartphone")
        self.assertEqual(product.stock, 50)
        self.assertIsNone(product.category)