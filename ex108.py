def converter(_input, measure):
    if measure.capitalize() == "Teaspoon":
        cup = _input // 48
        tbsp = _input % 48 // 3
        tsp = (_input % 48) % 3
    elif measure.capitalize() == "Tablespoon":
        cup = _input // 16
        tbsp = _input % 16
        tsp = (_input % 16) / 3
    elif measure.capitalize() == "Cup":
        cup = _input
        tbsp = 0
        tsp = 0
    return f"cup:{cup:.0f}, tbsp:{tbsp:.0f}, tsp:{tsp:.0f}"


input_text = int(input("type in your number of units - "))
measurment = input("type in tablespoon, teaspoon or cup - ")
print(converter(input_text, measurment))
