import random
from Neighbourhood import Neighbourhood
from WasteDept import WasteDept

current_hour = 9


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
    return day


def is_operating_hours():
    global current_hour  # Access the global variable

    # Define the end hour (e.g., 5 PM)
    end_hour = 17

    # Check if the current hour is within the operating hours
    if current_hour < end_hour:
        current_hour += 1  # Increment the current hour
        return True
    else:
        return False


def get_hour():
    return current_hour


def waste_collections(neighbourhoods, waste_units):
    for neighbourhood in neighbourhoods:
        # Check if it's operating hours before collecting waste
        if is_operating_hours():
            for house in neighbourhood.houses:
                # Randomly allocate waste to different waste units
                for _ in range(house.residents):
                    waste_type = random.choice(list(waste_units.keys()))
                    waste_unit = waste_units[waste_type]
                    waste_unit.collect_waste(1)
        elif not is_operating_hours():
            return False
    return True


def main():
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

    # Flags to track whether the day has been printed for each waste type
    day_printed = {"Monday": False, "Tuesday": False, "Wednesday": False}

    while not all(unit.current == unit.capacity for unit in waste_units.values()):
        # Collect recycling first
        while waste_units["recycle"].current < waste_units["recycle"].capacity:
            day = weekly_Schedule(waste_units)
            if day == "Monday" and not day_printed["Monday"]:
                print("\nToday is Monday")
                day_printed["Monday"] = True
            weekly_Schedule(waste_units)
            print("Recycling collection unit for Monday:", waste_units["recycle"].current, "/200")

        # Collect garbage second
        while waste_units["garbage"].current < waste_units["garbage"].capacity:
            day = weekly_Schedule(waste_units)
            if day == "Wednesday" and not day_printed["Wednesday"]:
                print("\nToday is Wednesday")
                day_printed["Wednesday"] = True
            weekly_Schedule(waste_units)
            print("Garbage collection unit for Wednesday:", waste_units["garbage"].current, "/200")

        # Collect organics last
        while waste_units["organics"].current < waste_units["organics"].capacity:
            day = weekly_Schedule(waste_units)
            if day == "Tuesday" and not day_printed["Tuesday"]:
                print("\nToday is Tuesday")
                day_printed["Tuesday"] = True
            weekly_Schedule(waste_units)
            print("Organics collection unit for Tuesday:", waste_units["organics"].current, "/200")

    print("\nAll waste collected!")
    print("Final collected amounts:")
    print("Recycling:", waste_units["recycle"].current)
    print("Organics:", waste_units["organics"].current)
    print("Garbage:", waste_units["garbage"].current)


if __name__ == "__main__":
    main()
