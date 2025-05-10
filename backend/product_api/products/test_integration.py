import unittest

# Assuming you have a Product class with a category attribute
class Product:
    def __init__(self, category):
        if not category:  # Check if the category is invalid (empty)
            raise ValueError("Category cannot be empty")
        self.category = category

# The test class for product integration
class ProductIntegrationTest(unittest.TestCase):

    def setUp(self):
        # Initialize the category attribute
        self.category = "Electronics"  # You can change this to whatever category you need
        # Create a product instance with the category
        self.product = Product(category=self.category)

    def test_product_creation(self):
        # Test if the product category is correctly set
        self.assertEqual(self.product.category, self.category)

    def test_product_category_is_not_empty(self):
        # Test if the category is not empty
        self.assertTrue(len(self.product.category) > 0)

    def test_invalid_category(self):
        # Test for an invalid category (if your application needs this check)
        invalid_category = ""
        with self.assertRaises(ValueError):  # Expecting ValueError when category is empty
            # This should now raise a ValueError
            Product(category=invalid_category)

if __name__ == '__main__':
    unittest.main()
