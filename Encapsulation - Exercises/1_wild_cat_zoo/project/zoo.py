from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget <= price:
            return 'Not enough budget'
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries_paid = sum(w.salary for w in self.workers)
        if self.__budget < total_salaries_paid:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries_paid
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = sum(a.money_for_care for a in self.animals)
        if self.__budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return self.__print_status(self.animals, 'Lion', 'Tiger', 'Cheetah')

    def workers_status(self):
        return self.__print_status(self.workers, 'Keeper', 'Caretaker', 'Vet')

    @staticmethod
    def __print_status(obj_list: list, *class_names):
        obj_dict = {cls_name: [] for cls_name in class_names}

        for obj in obj_list:
            obj_dict[obj.__class__.__name__].append(repr(obj))

        info = [f"You have {len(obj_list)} {obj_list[0].__class__.__bases__[0].__name__.lower()}s"]

        for key, value in obj_dict.items():
            info.append(f"----- {len(value)} {key}s:")
            info.extend(value)

        return '\n'.join(info)