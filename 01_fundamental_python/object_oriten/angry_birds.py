# define birds base class

class Birds:
    def __init__(self, name, color, skill_desc):
        self.name = name
        self.color = color
        self.skill_desc = skill_desc

    def fly(self):
        print(f"{self.name} is flying")

    def call(self):
        print(f"{self.name} is calling")

    def use_skill(self):
        print(f"{self.name} is using skill: {self.skill_desc}")


# defin child red birds class
class RedBirds(Birds):
    def __init__(self):
        super().__init__("red bird", "red", "crash into an obstacle and suffer massive damage")

    def fly(self):
        print("red bird fly in  stable speed")

    def call(self):
        print("red bird call in a stable way")


# defin child blue birds class
class BlueBirds(Birds):
    def __init__(self):
        super().__init__("blue bird", "blue", "split to three birds distribute damage")

    def fly(self):
        print("blue bird fly in a graceful way")

    def call(self):
        print("blue bird call in a graceful way")


# defin child yellow birds class
class YellowBirds(Birds):
    def __init__(self):
        super().__init__("yellow bird", "yellow", "throw a stone and cause damage")

    def fly(self):
        print("yellow bird fly in a loud way")

    def call(self):
        print("yellow bird call in a loud way")


# define obstacle class
class Obstacle:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def be_attacked(self, bird):
        print(f"{bird.name} fly to {self.name}")
        bird.use_skill()

        if isinstance(bird, RedBirds):
            damage = 80
        elif isinstance(bird, YellowBirds):
            damage = 50
        elif isinstance(bird, BlueBirds):
            damage = 30 * 3

        self.strength -= damage

        if self.strength <= 0:
            print(f"{self.name} is destroyed")
        else:
            print(f"{self.name} remain {self.strength} strength")


if __name__ == '__main__':
    red_bird = RedBirds()
    yellow_bird = YellowBirds()
    blue_bird = BlueBirds()

    obstacle1 = Obstacle("tree", 100)
    obstacle2 = Obstacle("house", 200)

    obstacle1.be_attacked(red_bird)
    obstacle2.be_attacked(yellow_bird)
    obstacle2.be_attacked(blue_bird)
