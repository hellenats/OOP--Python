
from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, FurnitureStore.INITIAL_CAPACITY)

        self.products = []

    @property
    def store_type(self):
        return "FurnitureStore"

    @property
    def type_of_products(self):
        return 'Furniture'

    def store_stats(self):
        # available_furniture = sorted(self.products, key=lambda f: f.model)
        # furniture_models_dict= {}
        #
        # for p in available_furniture:
        #     if p.model not in furniture_models_dict.keys():
        #         furniture_models_dict[p.model] = []
        #     furniture_models_dict[p.model].append(p.price)
        #
        # result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        # result += self.get_estimated_profit() + '\n'
        # result += "**Furniture for sale:" + '\n' if furniture_models_dict else ''
        # result += '\n'.join(f"{model}: {len(prices)}pcs, average price: {sum(prices) / len(prices):.2f}"
        #            for model, prices in furniture_models_dict.items())
        #
        # return result
        return self.print_store_stats(self.products)