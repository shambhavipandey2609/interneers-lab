from .models import Product, ProductCategory

class ProductRepository:
    @staticmethod
    def create_product(data):
        product = Product(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            brand=data.get("brand"),
            stock=data.get("stock"),
            category=data.get("category")
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
            product.brand=data.get("brand", product.brand)
            product.stock = data.get("stock", product.stock)
            product.category = data.get("category", product.category)
            # Save the updated product
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
    

class ProductCategoryRepository:
    @staticmethod
    def create_category(title, description):
        return ProductCategory(title=title, description=description).save()

    @staticmethod
    def get_all_categories():
        return list(ProductCategory.objects)

    @staticmethod
    def get_category_by_id(category_id):
        # without .first() it was returning a query set
        return ProductCategory.objects(id=category_id).first()

    @staticmethod
    def update_category(category_id, title, description):
        category = ProductCategory.objects(id=category_id).first()
        if category:
            category.update(title=title, description=description)
            return category.reload()
        return None

    @staticmethod
    def delete_category(category_id):
        return ProductCategory.objects(id=category_id).delete()

    @staticmethod
    def add_product_to_category(category_id, product_id):
        category = ProductCategory.objects(id=category_id).first()
        product = Product.objects(id=product_id).first()

        if not category:
            return {"error": "Category not found."}
        if not product:
            return {"error": "Product not found."}

        # Add product to category's product list and update product's category
        if product not in category.products:
            category.products.append(product)
            product.category = category
            category.save()
            product.save()

            return {"message": "Product added to category."}
        return {"message": "Product is already in this category."}

    @staticmethod
    def remove_product_from_category(category_id, product_id):
        category = ProductCategory.objects(id=category_id).first()
        product = Product.objects(pid=product_id).first()

        if not category:
            return {"error": "Category not found."}
        if not product:
            return {"error": "Product not found."}

        # Remove product from category and update product's category
        if product in category.products:
            category.products.remove(product)
            product.category = None
            category.save()
            product.save()

            return {"message": "Product removed from category."}
        return {"message": "Product not found in this category."}