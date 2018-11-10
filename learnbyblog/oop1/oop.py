class Character:
    def __init__(self, name, health, damage, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

heros = []
heros.append(Character('한민수', 200, 100, {'gold':500, 'weapon':'glock'}))

print(heros)
print(heros[0])
