from dataclasses import dataclass

@dataclass
class Hero:
    name: str
    health: int

    def take_damage(self, damage: int):
        if damage < 0:
            raise ValueError("damage must not be negative")
        self.health = max(0, self.health - damage)

@dataclass
class Product:
    name: str
    price: float

    def discounted_price(self, percent: float):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return round(self.price * (1 - percent / 100), 2)
