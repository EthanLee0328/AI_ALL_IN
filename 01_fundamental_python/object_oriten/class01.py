class Dish:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        pass


class Salad(Dish):
    def prepare(self):
        print(f"为 {self.name} 购买食材。")
        print(f"清洗 {self.name} 的蔬菜。")
        print(f"切 {self.name} 的蔬菜。")


class Stew(Dish):


 def prepare(self):
    print(f"为 {self.name} 购买食材。")
    print(f"切 {self.name} 的肉。")
    print(f"烹饪 {self.name}。")


class Soup(Dish):

    def prepare(self):
        print(f"为 {self.name} 购买食材。")
        print(f"煮 {self.name}。")


salad = Salad("蔬菜沙拉")
stew = Stew("炖肉")
soup = Soup("西红柿鸡蛋汤")

salad.prepare()
stew.prepare()
soup.prepare()
