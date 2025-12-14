# Singleton Implementation
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Factory Method Implementation
from abc import ABC, abstractmethod

class Transport(ABC):
    """Abstract base class for transport implementations."""
    @abstractmethod
    def deliver(self):
        pass
        
class Truck(Transport):
    def deliver(self):
        return "Deliver by road"

class Ship(Transport):
    def deliver(self):
        return "Deliver by sea"

class Logistics(ABC):
    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()

    @abstractmethod
    def create_transport(self):
        pass

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


# Abstract Factory Implementation
class Button(ABC):
    @abstractmethod
    def render(self): pass

class Checkbox(ABC):
    @abstractmethod
    def render(self): pass

class WindowsButton(Button):
    def render(self): return "Windows Button"

class MacButton(Button):
    def render(self): return "Mac Button"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): pass

    @abstractmethod
    def create_checkbox(self): pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Builder Implementation
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.garage = None

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "brick"
        return self

    def build_roof(self):
        self.house.roof = "tile"
        return self

    def build_garage(self):
        self.house.garage = True
        return self

    def build(self):
        return self.house

house = (
    HouseBuilder()
    .build_walls()
    .build_roof()
    .build_garage()
    .build()
)
