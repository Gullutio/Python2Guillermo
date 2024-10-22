capitals = {
    "Spain": "Madrid",
    "Singapore": "Singapore",
    "Vietnam": "Hanoi",
    "Malaysia": "Kuala Lumpur",
    "France": "Paris",
    "Afghanistan": "Kabul",
    "Albania": "Tirane",
    "Algeria": "Algiers",
    "Andorra": "Andorra La Vieja",
    "Angola": "Luanda",
    "Antigua and Barbuda": "Saint John's",
    "Argentina": "Buenos Aires",
    "Aremenia": "Yerevan",
    "Australia": "Canberra",
}

print("-- Capital Lookup --")
country = input("Enter country: ")
print(f"The capital of {country} is {capitals[country]}")

capitals["Australia"] = "Sydney"
print(capitals)
