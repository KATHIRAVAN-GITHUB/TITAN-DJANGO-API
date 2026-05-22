from .models import ProductCard

class ProductCardService:

    @staticmethod
    def get_all_products():
        print("Fetching all products from database...")
        return ProductCard.objects.all()

    @staticmethod
    def get_product_by_id(id):
        print("Fetching from database...")
        try:
            return ProductCard.objects.get(id=id)
        except ProductCard.DoesNotExist:
            return None

    @staticmethod
    def save_product(data):
        product = ProductCard.objects.create(**data)
        return product