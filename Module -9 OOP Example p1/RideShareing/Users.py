from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.Drivers = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_drivers(self,driver):
        self.Drivers.append(driver)

    def __repr__(self) -> str:
        return (f'{self.company_name} with riders: {len(self.riders)} driver :{len(self.Drivers)}')

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.__nid = nid

        # set user id dynamically
        self.__id = id

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid, current_location,initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        return f'Rider: {self.name} with email:{self.email}'

    def request_ride(self,destination):
        if not self.request_ride:

            
            ride_request = Ride_Request(self,destination)
            ride_matcher = Ride_Matching()
            self.current_ride = ride_matcher.find_Rider(ride_request)


    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location


class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        self.wallet = None
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        return f'Rider: {self.name} with email:{self.email}'

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.driver.wallet -= self.estimated_fare
        self.rider.wallet += self.estimated_fare


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_Matching:
    def __init__(self) -> None:
        self.available_driver = []

    def find_Rider(self):
        if (len(self.available_driver) > 0):
            driver = self.available_driver[0]
            ride = Ride(Ride_Request.rider.current_location,Ride_Request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):

    speed = {
        'car': 590,
        'bike': 60,
        'CNG': 15
    }
    def __init__(self,vehicle_type,license_plate,rate) -> None:
        self.vehicle_type = vehicle_type
        self.license = license
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
        super().__init__()

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    def start_drive(self):
        self.status = 'Unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.start_drive = 'Unavailable'

niyeJao = Ride_Sharing('Niye jao')
sakib = Rider('Shakib','akaib@mail.com',1243,'bonani',1200)
niyeJao.add_rider(sakib)
kalapakhi = Driver('kalaPakhi','kala@gamil.com',124,'Gulsan')
niyeJao.add_drivers(kalapakhi)