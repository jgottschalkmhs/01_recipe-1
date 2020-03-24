# ask user for the amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, convert to ml

# if no unit given / unit is unknown, leave as is


# **** function go here ****
def general_converter(how_much, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        x_by = dictionary.get(unit)
        how_much = how_much * x_by * conversion_factor

    return how_much


def unit_checker():
    unit_to_check = input("Unit? ")

    # abbreviations lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    cup = ["c", "C", "cup", "CUP"]
    ounce = ["ounce", "OZ"]
    pint = ["pint, pt", "P"]
    quart = ["qt", "q", "quart"]
    pound = ["lb", "pound"]
    litre = ["L", "litre"]

    if unit_to_check == "":
        print("you chose {}".format(unit_to_check))
        return unit_to_check

    elif unit_to_check == "T" or unit_to_check.lower() in tablespoon:
        return "tbs"
    elif unit_to_check.lower() in teaspoon:
        return "tsp"
    elif unit_to_check.lower() in cup:
        return "cup"
    elif unit_to_check.lower() in ounce:
        return "ounce"
    elif unit_to_check.lower() in pint:
        return "pint"
    elif unit_to_check.lower() in quart:
        return "pint"
    elif unit_to_check.lower in pound:
        return "pound"
    if unit_to_check.lower() in litre:
        return "litre"

    # **** main routine goes here ****


unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000
}
keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # get unit and change it to match dictionary
    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    # keep_going = input("<enter> or q")
