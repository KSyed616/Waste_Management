import random
from Neighbourhood import Neighbourhood
from WasteDept import WasteDept


def waste_collections(neighbourhoods, waste_units):
    for neighbourhood in neighbourhoods:
        for house in neighbourhood.houses:
            # Randomly allocate waste to different waste units
            for _ in range(house.residents):
                waste_type = random.choice(list(waste_units.keys()))
                waste_unit = waste_units[waste_type]
                waste_unit.collect_waste(1)


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

    # Print current load in each waste unit
    for unit_type, unit in waste_units.items():
        print(f"{unit_type.capitalize()} unit current load: {unit.current}/{unit.capacity}")


if __name__ == "__main__":
    main()