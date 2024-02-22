class Train:
    def __init__(self):
        self.engine = Carriage()
        self.carriages = []

    def add_carriage(self, carriage):
        self.carriages.append(carriage)

    def __len__(self):
        return len(self.carriages)

    def __str__(self):
        train_structure = "-".join([f"[{n}]" for n in range(1, len(self.carriages) + 1)])
        return f"<=[HEAD]-{train_structure}"


class Carriage:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print("The carriage is full. Wait for another one, please")

    def __len__(self):
        return len(self.passengers)


if __name__ == "__main__":
    train = Train()

    carriage1 = Carriage()
    for p in range(6):
        carriage1.add_passenger(f"Passenger_{p+1}")

    carriage2 = Carriage()
    for p in range(4):
        carriage2.add_passenger(f"Passenger_{p+1}")

    train.add_carriage(carriage1)
    train.add_carriage(carriage2)

    print(f"Number of carriages: {len(train)}")
    print(f"{train}")

    print(f"Number of passengers in carriage 1: {len(carriage1)}")
    print(f"Number of passengers in carriage 2: {len(carriage2)}")
