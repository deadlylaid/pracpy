class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        return '아이템 : {}, 가격: {}'.format(self.name, self.price)

food_1 = Food('아이스크림', 3000)
food_2 = Food('햄버거', 5000)

print(food_1 < food_2)
print(food_1 > food_2)

print(food_1 + food_2)
