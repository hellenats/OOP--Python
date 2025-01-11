from typing import List
from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    INITIAL_CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, ToyStore.INITIAL_CAPACITY)

        self.products: List[BaseProduct] = []

    @property
    def store_type(self):
        return "ToyStore"

    @property
    def type_of_products(self):
        return 'Toys'

    def store_stats(self):
        # available_toys = sorted(self.products, key=lambda t: t.model)
        # toys_models_dict = {}
        #
        # for p in available_toys:
        #     if p.model not in toys_models_dict.keys():
        #         toys_models_dict[p.model] = []
        #     toys_models_dict[p.model].append(p.price)
        #
        # result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
        #           f"{self.get_estimated_profit()}", "**Toys for sale:", ]
        # result.extend([f"{model}: {len(prices)}pcs, average price: {sum(prices) / len(prices):.2f}"
        #                      for model, prices in toys_models_dict.items()])
        #
        # return '\n'.join(result)
        return self.print_store_stats(self.products)