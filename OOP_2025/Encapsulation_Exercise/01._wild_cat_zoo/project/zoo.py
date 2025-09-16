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
        if self.__animal_capacity <= len(self.animals):
            return 'Not enough space for animal'
        if self.__budget < price:
            return 'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary = sum(w.salary for w in self.workers)
        if self.__budget < total_salary:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= total_salary
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        total_money_for_care = sum(a.money_for_care for a in self.animals)
        if self.__budget < total_money_for_care:
            return f'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= total_money_for_care
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self):
        return self.__print_status(self.animals, "Lions", "Tigers", "Cheetahs")

    def workers_status(self):
        return self.__print_status(self.workers, "Keepers", "Caretakers", "Vets")

    @staticmethod
    def __print_status(category: list[Animal | Worker], *args):
        result = [f'You have {len(category)} {category[0].__class__.__bases__[0].__name__.lower()}s']
        for type_name in args:
            filtered = [repr(obj) for obj in category if obj.__class__.__name__ == type_name[:-1]]  # "Lions" -> "Lion"
            result.append(f"----- {len(filtered)} {type_name}:")
            result.extend(filtered)
        return "\n".join(result)








