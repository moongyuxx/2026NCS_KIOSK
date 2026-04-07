class Poketmon:
    def __init__(self):  # 이렇게만 하면 메모리 주소 나옴.
        self.hp = 100

    def __str__(self):
        return f"Health: {self.hp} hp"


p1 = Poketmon()
print(p1)