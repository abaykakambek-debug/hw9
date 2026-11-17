class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def hit(self, damage: int):
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self.health = max(0, self.health - damage)