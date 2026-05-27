def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if(age > 60):
        print("Plant is ready to harvest!")
        return
    print("Plant needs more time to grow.")