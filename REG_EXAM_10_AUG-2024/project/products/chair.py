from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIALS = 'Wood'
    SUB_TYPE = 'Furniture'
    DISCOUNT = 0.1

    def __init__(self,  model: str, price: float):
        super().__init__(model, price, Chair.MATERIALS, Chair.SUB_TYPE)

    def discount(self):
        self.price -= (self.price * Chair.DISCOUNT)

    def type(self):
        return 'Chair'