#
#   Author: Scott Crooks
#
#   Purpose: System for tracking the number of happy/unhappy passengers
#            for Codetown school bus stops/routes and calculating what routes need new buses
#
#   Usage: To use, run this file / see readme.md
#

import csv
import re
import sys


def sort_route_data(routes: list[dict]) -> list[dict]:
    """
    sort_route_data sorts inputted list[dict] by happy_customer_ratio.

    :param routes: list[dict] of route data
    :return: sorted list[dict] of route data
    """
    sorted_routes = sorted(routes, key=lambda d: d['happy_customer_ratio'], reverse=True)
    return sorted_routes


def verify_route(route_data: str) -> bool:
    """
    verify_route compares the inputted route string against a regex expression
    and returns true if the inputted string matches the regex expression.

    :param route_data: Route string, format: 100,100,100
    :return: Boolean, True if regex expression matched
    """
    regex = r'^\d+,\d+,\d+$'
    if re.search(regex, route_data) is not None:
        return True
    else:
        return False


def create_route_dict(route_data: str) -> dict:
    """
    create_route_dict attempts to create a dictionary from the inputted string
    and returns said dictionary.

    :param route_data: Route data string
    :return: Route dictionary
    """

    # The route data is given as a string, so we must split the string to form the dictionary
    data = route_data.split(',')

    route_dict = {
        "route_id": int(data[0]),
        "happy_passengers": int(data[1]),
        "unhappy_passengers": int(data[2]),
        "happy_customer_ratio": round(float(data[1]) / float(data[2]), 2)
    }

    return route_dict


def read_route_data(file: str, routes_list: list[dict]) -> None:
    """
    read_route_data attempts to read requested file, and if successful creates a list
    of dictionaries containing the route data

    :param routes_list: List of route dictionaries
    :param file: File to read data from.
    """

    # Attempt to open file
    with open(file, newline='') as csvfile:
        # Create a new csv reader
        reader = csv.reader(csvfile, delimiter=' ')
        # Read through each line in file
        for row in reader:
            route_txt = row[0]
            if verify_route(row[0]):
                # If there are no errors with data create a new dict and append to list
                routes_list.append(create_route_dict(row[0]))
            else:
                # If there is an error in the data, give an error message and exit with code 1 (error)
                error_message = "An error has occurred while attempted to read \"{}\"." \
                                "\nPlease ensure that file is structured correctly before attempting a rerun." \
                                "\nExiting program."
                print(error_message.format(file))
                sys.exit(1)


def request_int_input(message: str, minimum: int = None, maximum: int = None) -> int:
    """
    get_int_input requests an integer input from the
    user of a minimum value, specified by minimum.

    :param message: The message presented to the user
    :param minimum: Minimum allowed input
    :param maximum: Maximum allowed input
    :return: int
    """
    while True:
        try:
            input_num = int(input(message))

            if minimum is not None and input_num < minimum:
                print("Invalid input. Please enter an integer of at least " + str(minimum) + ".")
            elif maximum is not None and input_num > maximum:
                print("Invalid input. Please enter an integer of at least " + str(maximum) + ".")
            else:
                return input_num
        except:
            print("Invalid input. Please enter an integer")


def main():
    """
    main controls core program loop.
    """
    routes = []
    read_route_data("routes.txt", routes)
    routes = sort_route_data(routes)
    print(str(routes))

    extra_buses = request_int_input("How many routes can have an extra bus?", 0, len(routes))

    print("You should add buses to the following routes: ")
    for i in range(extra_buses):
        print(str(routes[i].get('route_id')))


# Program entry:
main()
