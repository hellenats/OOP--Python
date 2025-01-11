from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    MATERIALS = 'Wood/Plastic'
    SUB_TYPE = 'Toys'
    DISCOUNT = 0.2

    def __init__(self,  model: str, price: float):
        super().__init__(model, price, HobbyHorse.MATERIALS, HobbyHorse.SUB_TYPE)

    def discount(self):
        self.price -= (self.price * HobbyHorse.DISCOUNT)

    def type(self):
        return 'HobbyHorse'