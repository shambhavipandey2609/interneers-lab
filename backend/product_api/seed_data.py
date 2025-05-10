from mongoengine import connect

# from productapi.settings import connect 
# ✅ Establish connection
connect(
    db="productdb",  # your database name
    host="mongodb://localhost:27017/productdb",
    alias="default"  # required for MongoEngine to treat this as the default connection
)
from products.models import ProductCategory, Product
def seed_categories():
    ProductCategory.drop_collection()
    ProductCategory(title="Food", description="Edible items").save()
    ProductCategory(title="Electronics", description="Gadgets and devices").save()

def seed_products():
    Product.drop_collection()
    Product(name="Laptop", category="Electronics", price=50000, brand="Dell", stock=10).save()
    Product(name="Bread", category="Food", price=40, brand="Britannia", stock=50).save()

if __name__ == "__main__":
    seed_categories()
    seed_products()
    print("✅ Seeded categories and products.")
