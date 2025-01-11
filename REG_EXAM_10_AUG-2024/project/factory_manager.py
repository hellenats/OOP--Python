from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        valid_product_types = {"Chair": Chair, "HobbyHorse": HobbyHorse}

        if product_type not in valid_product_types:
            raise Exception("Invalid product type!")

        item = valid_product_types[product_type](model, price)
        self.products.append(item)
        return f"A product of sub-type {item.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        valid_store_types = {'FurnitureStore': FurnitureStore, 'ToyStore': ToyStore}

        if store_type not in valid_store_types:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = valid_store_types[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [el for el in products if el.sub_type == store.type_of_products]

        if not filtered_products:
            return "Products do not match in type. Nothing sold."

        for product in filtered_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price
        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        try:
            store_to_remove = next(s for s in self.stores if s.name == store_name)
            if len(store_to_remove.products) > 0:
                return "The store is still having products in stock! Unregistering is inadvisable."
            self.stores.remove(store_to_remove)
            return f"Successfully unregistered store {store_name}, location: {store_to_remove.location}."

        except StopIteration:
            raise Exception("No such store!")

    def discount_products(self, product_model: str):
        discounted_products = 0

        for product in self.products:
            if product.model == product_model:
                product.discount()
                discounted_products += 1

        return f"Discount applied to {discounted_products} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        try:
            store = next(s for s in self.stores if s.name == store_name)
            return store.store_stats()
        except StopIteration:
            return "There is no store registered under this name!"

    def statistics(self):
        products_sum_price = sum(p.price for p in self.products)
        products_dict = {}
        for p in sorted(self.products, key=lambda p: p.model):
            if p.model not in products_dict:
                products_dict[p.model] = 0
            products_dict[p.model] += 1

        res = [f"Factory: {self.name}", f"Income: {self.income:.2f}", "***Products Statistics***",
               f"Unsold Products: {len(self.products)}. Total net price: {products_sum_price:.2f}"]

        res.extend([f"{model}: {count}" for model, count in products_dict.items()])
        res.append(f"***Partner Stores: {len(self.stores)}***")
        res.extend([s.name for s in sorted(self.stores, key=lambda s: s.name)])

        return '\n'.join(res)