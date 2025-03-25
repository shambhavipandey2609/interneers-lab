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