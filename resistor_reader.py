from engineering_notation import EngNumber

import argparse
import math


# dicts
color_num_dict = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
    "blue": 6, "violet": 7, "grey": 8, "white": 9}


mult_dict = {
    "gold": 0.1, "silver": 0.01}
for key, val in color_num_dict:
    mult_dict[key] = math.pow(10, int(val))


tolerance_dict = {
    "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 0.5, "blue": 0.25,
    "violet": 0.1, "grey": 0.05, "gold": 5, "silver": 10}


temp_coeff_dict = {
    "black": 100, "red": 50, "orange": 15, "yellow": 25, "blue": 10, "violet": 5}


# functions
def get_color_num(color: str):
    try:
        return color_num_dict[color.lower()]
    except KeyError:
        return None


def get_mult(color: str):
    try:
        return mult_dict[color.lower()]
    except KeyError:
        return None


def get_tolerance(color: str):
    try:
        return tolerance_dict[color.lower()]
    except KeyError:
        return None


def get_range(value, tolerance):
    return value*(1-(tolerance/100)), value*(1+(tolerance/100))


def get_temp_coeff(color: str):
    try:
        return temp_coeff_dict[color.lower()]
    except KeyError:
        return None


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
