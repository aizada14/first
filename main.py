class Vehicle:
    def __init__(self, type_of_transport, manufacturer, model, year):
        self.type_of_transport = type_of_transport
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Тип траснпорта: {self.type_of_transport}, Производитель: {self.manufacturer}, Модель: {self.model}")
        print(f"Год выпуска: {self.year}")

    def start(self):
        print(f"{self.type_of_transport} начинает движение")


class GroundVehicle(Vehicle):
    def __init__(self, type_of_transport, manufacturer, model, year, color, type_of_engine):
        super().__init__(type_of_transport, manufacturer, model, year)
        self.color = color
        self.type_of_engine = type_of_engine

    def display_info(self):
        super().display_info()
        print(f"Цвет: {self.color}")
        print(f"Коробка передач: {self.type_of_engine}")


class PassengerCar(GroundVehicle):
    def __init__(self, type_of_transport, manufacturer, model, year, color, type_of_engine, engine_capacity):
        super().__init__(type_of_transport, manufacturer, model, year, color, type_of_engine)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Объем двигателя: {self.engine_capacity}")

    def show_engine_capacity(self):
        print(f"{self.model} имеет двигатель объемом {self.engine_capacity} литра.")


toyota_camry = PassengerCar("Легковой автомобиль", "Южная Корея", "Camry", 2023, "Белый", "автомат", 2)
toyota_camry.display_info()
toyota_camry.show_engine_capacity()
toyota_camry.start()