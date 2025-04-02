from .repository import ProductRepository, ProductCategoryRepository, Product, ProductCategory

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



class ProductCategoryService:
    @staticmethod
    def create_category(title, description):
        return ProductCategoryRepository.create_category(title, description)

    @staticmethod
    def get_all_categories():
        return ProductCategoryRepository.get_all_categories()

    @staticmethod
    def get_category_by_id(category_id):
        return ProductCategoryRepository.get_category_by_id(category_id)

    @staticmethod
    def update_category(category_id, title, description):
        return ProductCategoryRepository.update_category(category_id, title, description)

    @staticmethod
    def delete_category(category_id):
        return ProductCategoryRepository.delete_category(category_id)

    @staticmethod
    def add_product_to_category(category_id, product_id):
        return ProductCategoryRepository.add_product_to_category(category_id, product_id)
    @staticmethod
    def remove_product_from_category(category_id, product_id):
        return ProductCategoryRepository.remove_product_from_category(category_id, product_id)
