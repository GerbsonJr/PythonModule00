def count(day, total):
    if day > total:
        print("Harvest time!")
        return
    print(f"Day {day}")
    count(day + 1, total)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count(1, days)
