def ft_water_reminder():
    dayNum = int(input("Days since last watering: "))
    if(dayNum > 2):
        print("Water the plants!")
        return
    print("Plants are fine")