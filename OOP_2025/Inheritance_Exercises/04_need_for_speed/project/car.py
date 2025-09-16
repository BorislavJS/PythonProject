from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def drive(self, kilometers):
        super().drive(kilometers)
