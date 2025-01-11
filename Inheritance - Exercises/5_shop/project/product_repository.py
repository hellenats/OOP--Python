from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name: str):
        product = next((p for p in self.products if p.name == product_name), None)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f'{product.name}: {product.quantity}')

        return '\n'.join(result)
