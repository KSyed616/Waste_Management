import random
from Neighbourhood import Neighbourhood
from WasteDept import WasteDept


def weekly_Schedule(waste_units):
    random_int = random.randint(1, 3)

    if random_int == 1:
        day = "Monday"
        waste_units["recycle"].collect_waste()
    elif random_int == 2:
        day = "Tuesday"
        waste_units["organics"].collect_waste()
    else:
        day = "Wednesday"
        waste_units["garbage"].collect_waste()

    print(f"Today is {day}")
    return day


def waste_collections(neighbourhoods, waste_units):
    for neighbourhood in neighbourhoods:
        for house in neighbourhood.houses:
            # Randomly allocate waste to different waste units
            for _ in range(house.residents):
                waste_type = random.choice(list(waste_units.keys()))
                waste_unit = waste_units[waste_type]
                waste_unit.collect_waste(1)


def main():
    global unit
    n1 = Neighbourhood(50)
    n2 = Neighbourhood(75)
    n3 = Neighbourhood(50)

    neighbourhoods = [n1, n2, n3]

    recycle_unit = WasteDept("recycle")
    organics_unit = WasteDept("organics")
    garbage_unit = WasteDept("garbage")

    waste_units = {
        "recycle": recycle_unit,
        "organics": organics_unit,
        "garbage": garbage_unit
    }

    waste_collections(neighbourhoods, waste_units)

    day = weekly_Schedule(waste_units)
    # Print a message based on the day
    if day == "Monday":
        print("Garbage collection unit for Monday:", waste_units["recycle"].current, "/200")
    elif day == "Tuesday":
        print("Garbage collection unit for Tuesday:", waste_units["organics"].current, "/200")
    else:
        print("Garbage collection unit for Wednesday:", waste_units["garbage"].current, "/200")


if __name__ == "__main__":
    main()
