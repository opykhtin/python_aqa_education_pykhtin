"""OOP - Hierarchy"""


class Transport:

    def __init__(self, brand, year):
        """Transport characteristics"""
        self.brand = brand
        # self.color = color
        # self.speed = speed
        self.year = year

    @staticmethod
    def price_cost(country, cost):
        currency = {'europe': 'EUR', 'asia': 'CNY', 'america': 'USD'}
        """Cost in the world"""
        if country == 'europe':
            cost *= 1.5
            return str(cost) + ' ' + currency['europe']
        elif country.lower == 'asia':
            cost /= 2
            return str(cost) + ' ' + currency['asia']
        elif country.lower == 'america':
            return str(cost) + ' ' + currency['america']
        else:
            return "Sale of vehicles in this country is not available."

    def transport_type(self):
        """Type of transport"""
        print(f'Transport type. Brand: {self.brand}. Year: {self.year}.')


class Car(Transport):
    def __init__(self, cost, brand, year, passengers=4):
        """Cars characteristics"""
        super().__init__(brand, year)
        self.passengers = passengers
        self.cost = cost

    def car_type(self):
        """Type of car"""
        print(f'Car type. Brand: {self.brand}. Year: {self.year}. Passengers: {self.passengers}.')


class Plane(Transport):
    def __init__(self, brand, year, seats):
        """Planes characteristics"""
        super().__init__(brand, year)
        self.seats = seats
        # self.weight = weight

    def plane_type(self):
        """Type of plane"""
        print(f'Plane type. Brand: {self.brand}. Year: {self.year}. Seats: {self.seats}.')


class Ship(Transport):
    def __init__(self, brand, year, pool):
        """Ships characteristics"""
        super().__init__(brand, year)
        self.pool = pool
        # self.sail = sail

    def transport_type(self):
        """Type of ship"""
        print(f'Ship type. Brand: {self.brand}. Year: {self.year}. Pool: {self.pool}.')


class Truck(Transport):
    def __init__(self, brand, year, sleeping_place):
        """Trucks characteristics"""
        super().__init__(brand, year)
        self.sleeping_place = sleeping_place
        # self.cargo_weight = cargo_weight

    def truck_type(self):
        """Type of truck"""
        print(f'Truck type. Brand: {self.brand}. Year: {self.year}. Place to sleep: {self.sleeping_place}.')


class FutureVehicle(Car, Plane):
    def __init__(self, cost, brand, year, passenger, seats):
        """Future vehicles characteristics"""
        Car.__init__(self, cost, brand, year, passenger)
        Plane.__init__(self, brand, year, seats)

    def future_type(self):
        """Type of future vehicle"""
        print(f'Type of future vehicle. Brand: {self.brand}. Year: {self.year}. Seats: {self.seats}.')


def main():
    # car1 = Car(1000, 'BMW', 2020)
    # car2 = Car(2000, 'Seat', 2019, 5)
    # car1.transport_type()
    # car1.car_type()
    # car2.car_type()
    # plane1 = Plane('Boeing-740', 2006, 136)
    # plane1.transport_type()
    # plane1.plane_type()
    # ship1 = Ship('Titanic', 1457, 'Yes')
    # ship1.transport_type()
    # truck1 = Truck('Optimus', 2008, 'Yes')
    # truck1.truck_type()
    future1 = FutureVehicle(cost=10000, brand='ICar', year=2079, passenger=99, seats=1)
    future1.future_type()
    # print(car1.price_cost('europe', car1.cost))


if __name__ == '__main__':
    main()