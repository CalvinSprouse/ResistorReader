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


def get_resistance(*bands):
    band_list = list(bands)
    tolerance = get_tolerance(band_list.pop())
    multiplier = get_mult(band_list.pop())
    value = int("".join([str(get_color_num(color)) for color in band_list]))
    resistance = multiplier*int(value)
    r_min, r_max = get_range(resistance, float(tolerance))
    return {"resistance": str(EngNumber(resistance)),
            "tolerance": str(EngNumber(tolerance)),
            "min": str(EngNumber(r_min)), "max": str(EngNumber(r_max))}


try:
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description="Return the resistance and tolerance for a given set of bands")
        parser.add_argument(
            "bands", metavar="b", type=str, nargs="+", help="List of bands in order L-R")

        args = vars(parser.parse_args())
        result = get_resistance(*args["bands"])
        print(f"Resistance (Ohms): {result['resistance']} +-{result['tolerance']}%\n"
              f"Min (Ohms): {result['min']}\nMax (Ohms): {result['max']}")
except Exception:
    print("Illegal Entry")