from project.trainer import Trainer
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:

    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        self.__add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_obj(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_obj(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_obj(subscription, self.subscriptions)

    @staticmethod
    def __add_obj(obj, collection: list):
        if obj not in collection:
            collection.append(obj)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_obj(subscription_id, self.subscriptions)
        customer = self.__get_obj(subscription.customer_id, self.customers)
        trainer = self.__get_obj(subscription.trainer_id, self.trainers)
        plan = self.__get_obj(subscription.exercise_id, self.plans)
        equipment = self.__get_obj(plan.equipment_id, self.equipment)

        result = [repr(subscription), repr(customer), repr(trainer), repr(equipment), repr(plan)]
        return '\n'.join(result)

    def __get_obj(self, obj_id, collection):
        obj = next((obj for obj in collection if obj.id == obj_id), None)
        return obj