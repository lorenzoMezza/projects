#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1.0

    def age_up(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created:", end=" ")
        plant.show()