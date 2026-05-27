def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))

    for i in range(1, days + 1):
        print(f"Day {i}")

    print("Harvest time!")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(i):
        if i > days:
            print("Harvest time!")
            return

        print(f"Day {i}")
        count(i + 1)

    count(1)
