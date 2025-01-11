from typing import Union

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_object(self.customers, customer_id)
        dvd = self.find_object(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return  "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_object(self.customers, customer_id)
        dvd = self.find_object(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    @staticmethod
    def find_object(collection, uid):
        obj = next((obj for obj in collection if obj.id == uid), None)
        return obj

    def __repr__(self):
        result = [repr(c) for c in self.customers]
        result.extend([repr(d) for d in self.dvds])
        return '\n'.join(result)
