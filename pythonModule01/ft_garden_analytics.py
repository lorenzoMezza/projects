#!/usr/bin/env python3

class Plant:

    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self):
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.stats = Plant.Stats()

    # static method
    @staticmethod
    def is_more_than_a_year(days):
        return days > 365

    # class method (anonymous plant)
    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        self.height += 1
        self.stats._grow_calls += 1

    def age_up(self):
        self.age += 1
        self.stats._age_calls += 1

    def show(self):
        self.stats._show_calls += 1
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")



class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self):
        self.shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")



class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def grow(self):
        super().grow()
        self.seeds += 10

    def age_up(self):
        super().age_up()
        self.seeds += 1

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")



def show_stats(plant):
    plant.stats.display()
    if isinstance(plant, Tree):
        print(f"{plant.shade_calls} shade")



if __name__ == "__main__":

    print("=== Garden statistics ===")

    # Static method
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_more_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_more_than_a_year(400)}")

    # ---------------- Flower ----------------
    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_stats(rose)

    # ---------------- Tree ----------------
    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)

    # ---------------- Seed ----------------
    print("\n=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    show_stats(sunflower)

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()

    sunflower.show()
    show_stats(sunflower)

    # ---------------- Anonymous ----------------
    print("\n=== Anonymous ===")
    unknown = Plant.anonymous()
    unknown.show()
    show_stats(unknown)