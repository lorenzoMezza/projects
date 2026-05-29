#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def grow(self):
        self.height += self.growth_rate

    def age_up(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)

    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")

        rose.grow()
        rose.age_up()

        rose.show()

    total_growth = rose.height - start_height

    print(f"Growth this week: {round(total_growth, 1)}cm")