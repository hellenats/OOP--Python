from abc import ABC, abstractmethod
from typing import List, Union
from project.products.base_product import BaseProduct


class BaseStore(ABC):
    PERCENTAGE = 0.1

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) <= 0:
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if ' ' in value or len(value) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        total_product_prices = sum(p.price for p in self.products)
        estimated_profit = total_product_prices * BaseStore.PERCENTAGE
        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"


    @property
    @abstractmethod
    def store_type(self):
        pass

    @property
    @abstractmethod
    def type_of_products(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass

    def print_store_stats(self, collection):
        available_items = sorted(collection, key=lambda i: i.model)
        items_models_dict = {}

        for p in available_items:
            if p.model not in items_models_dict.keys():
                items_models_dict[p.model] = []
            items_models_dict[p.model].append(p.price)

        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                  f"{self.get_estimated_profit()}", f"**{self.type_of_products} for sale:"]
        result.extend([f"{model}: {len(prices)}pcs, average price: {sum(prices) / len(prices):.2f}"
                       for model, prices in items_models_dict.items()])

        return '\n'.join(result)