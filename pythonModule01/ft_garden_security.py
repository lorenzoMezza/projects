#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print("Current state:", end=" ")
    rose.show()