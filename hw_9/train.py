class Train:
    def __init__(self):
        self.engine = Carriage(is_engine=True)
        self.carriages = []

    def add_carriage(self, carriage):
        self.carriages.append(carriage)

    def add_passenger(self, name, carriage_number):
        if carriage_number == 0:
            self.engine.add_passenger(name)
        elif 0 < carriage_number <= len(self.carriages):
            self.carriages[carriage_number - 1].add_passenger(name)
        else:
            print("Invalid carriage number. Please choose a valid carriage.")

    def __len__(self):
        return len(self.carriages)

    def __str__(self):
        train_structure = "-".join([f"[{n}]" for n in range(1, len(self.carriages) + 1)])
        return f"<=[HEAD]-{train_structure}"


class Carriage:
    def __init__(self, is_engine=False):
        self.passengers = []
        self.is_engine = is_engine

    def add_passenger(self, passenger):
        if not self.is_engine:
            if len(self.passengers) < 10:
                self.passengers.append(passenger)
            else:
                print("The carriage is full. Wait for another one, please")
        else:
            print("Forbidden to add passengers to the Engine carriage.")

    def __len__(self):
        return len(self.passengers)


if __name__ == "__main__":
    train = Train()

    carriage1 = Carriage()
    carriage2 = Carriage()
    train.add_carriage(carriage1)
    train.add_carriage(carriage2)

    # Add passengers to the carriages
    train.add_passenger("Alice", 1)
    train.add_passenger("Bob", 2)
    train.add_passenger("Charlie", 0)  # Trying to add Charlie to the engine carriage

    # Print the train's structure
    print("Train structure:")
    print(train)

    # Print the number of passengers in each carriage
    print(f"Number of passengers in carriage 1: {len(carriage1)}")
    print(f"Number of passengers in carriage 2: {len(carriage2)}")
