"""Module lab4_more_patterns

Лабораторная работа 4 рассматривает дополнительные паттерны проектирования,
такие как:
- Стратегия
- Цепочка обязанностей
- Итератор
- Прокси
- Мост
- Адаптер
"""

# Отключаем некоторые проверки линтера для учебных целей
# pylint: disable=missing-class-docstring, missing-function-docstring, too-few-public-methods

from abc import ABC, abstractmethod

# Стратегия
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:

        pass

class CardPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} by card")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} in crypto")

class Order:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: int):
        self.strategy.pay(amount)

order = Order(CardPayment())
order.checkout(100)

order.strategy = CryptoPayment()
order.checkout(100)

# Цепочка обязанностей
class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        if self.next:
            return self.next.handle(request)

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("user"):
            return "Unauthorized"
        return super().handle(request)

class PermissionHandler(Handler):
    def handle(self, request):
        if request.get("role") != "admin":
            return "Forbidden"
        return "Access granted"

chain = AuthHandler(PermissionHandler())
print(chain.handle({"user": "egor", "role": "admin"}))

# Итератор
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for number in MyRange(1, 5):
    print(number)

# Прокси
class RealService:
    def request(self):
        return "Real response"

class ProxyService:
    def __init__(self):
        self._service = None

    def request(self):
        if self._service is None:
            self._service = RealService()
        return self._service.request()

proxy = ProxyService()
print(proxy.request())

# Мост

class Renderer(ABC):
    @abstractmethod
    def render(self, shape: str): pass

class VectorRenderer(Renderer):
    def render(self, shape):
        return f"Drawing {shape} as vector"

class RasterRenderer(Renderer):
    def render(self, shape):
        return f"Drawing {shape} as pixels"

class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

class Circle(Shape):
    def draw(self):
        return self.renderer.render("circle")

circle = Circle(VectorRenderer())
print(circle.draw())

# Адаптер
class OldAPI:
    def specific_request(self):
        return "Old API response"

class Adapter:
    def __init__(self, adaptee: OldAPI):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

def client_code(api):
    print(api.request())

client_code(Adapter(OldAPI()))
