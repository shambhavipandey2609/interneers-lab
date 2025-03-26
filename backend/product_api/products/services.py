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
#   method for deleting the product
    @staticmethod
    def delete_product(product_id):
        return ProductRepository.delete_product(product_id)
