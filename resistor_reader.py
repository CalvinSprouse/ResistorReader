from engineering_notation import EngNumber

import argparse
import math


def get_color_num(color: str):
    if color.lower() == "black":
        return 0
    elif color.lower() == "brown":
        return 1
    elif color.lower() == "red":
        return 2
    elif color.lower() == "orange":
        return 3
    elif color.lower() == "yellow":
        return 4
    elif color.lower() == "green":
        return 5
    elif color.lower() == "blue":
        return 6
    elif color.lower() == "violet":
        return 7
    elif color.lower() == "grey":
        return 8
    elif color.lower() == "white":
        return 9


def get_mult(color: str):
    if color.lower() == "gold":
        return 0.1
    elif color.lower() == "silver":
        return 0.01
    return math.pow(10, int(get_color_num(color)))


def get_tolerance(color: str):
    if color.lower() == "brown":
        return 1
    elif color.lower() == "red":
        return 2
    elif color.lower() == "orange":
        return 3
    elif color.lower() == "yellow":
        return 4
    elif color.lower() == "green":
        return 0.5
    elif color.lower() == "blue":
        return 0.25
    elif color.lower() == "violet":
        return 0.1
    elif color.lower() == "grey":
        return 0.05
    elif color.lower() == "gold":
        return 5
    elif color.lower() == "silver":
        return 10


def get_range(value, tolerance):
    return value*(1-(tolerance/100)), value*(1+(tolerance/100))


def get_temp_coeff(color: str):
    if color.lower() == "black":
        return 100
    elif color.lower() == "red":
        return 50
    elif color.lower() == "orange":
        return 15
    elif color.lower() == "yellow":
        return 25
    elif color.lower() == "blue":
        return 10
    elif color.lower() == "violet":
        return 5


def get_resistance(*bands):
    # vars
    band_list = list(bands)
    temp_coeff = None

    # get band color conversion
    if len(band_list) == 6:
        temp_coeff = get_temp_coeff(band_list.pop())
    tolerance = get_tolerance(band_list.pop())
    multiplier = get_mult(band_list.pop())

    # math on values
    resistance = multiplier*int(
        "".join([str(get_color_num(color)) for color in band_list]))
    r_min, r_max = get_range(resistance, float(tolerance))

    # return dict
    return_dict = {"resistance": str(EngNumber(resistance)),
                   "tolerance": str(tolerance),
                   "min": str(EngNumber(r_min)), "max": str(EngNumber(r_max))}
    if temp_coeff:
        return_dict["temp_coeff"] = str(EngNumber(temp_coeff))
    return return_dict


try:
    if __name__ == "__main__":
        # create parser
        parser = argparse.ArgumentParser(
            description="Return the resistance and tolerance for a given set of bands")
        parser.add_argument(
            "bands", metavar="bands", type=str, nargs="+", help="List of bands in order L-R")

        # get arg dict
        args = vars(parser.parse_args())

        # print input for clarity
        print("Resistor Input:", ", ".join(str(band).lower().capitalize() for band in args["bands"]))

        # potentially throw error
        result = get_resistance(*args["bands"])

        # output
        output = (f"Resistance (Ohms): {result['resistance']} +-{result['tolerance']}%\n"
                  f"Min (Ohms): {result['min']}\nMax (Ohms): {result['max']}\n")
        try:
            output += f"Temperature Coefficient (ppm/K): {result['temp_coeff']}"
        except KeyError:
            pass
        print(output)
except Exception:
    print("Illegal Entry - Check Spelling and Order")
