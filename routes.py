import csv
import re

routes = []


def sort_route_data(list: list[dict]) -> None:
    pass


def verify_route(string: str) -> bool:
    """

    :param string: route
    :return:
    """
    regex = "^\d+,\d+,\d+$"
    if re.search(regex, string) is not None:
        return True
    else:
        return False

def create_route_dict(route_data: str) -> None:
    pass

def read_route_data(file: str) -> None:
    """
    Attempts to read requested csv file, and if successful creates a list
    of dictionaries containing the route data

    :param file: File to read data from.
    """
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            route_txt = row[0]

            if verify_route(route_txt):
                data = route_txt.split(',')

                route_dict = {
                    "route_id": int(data[0]),
                    "happy_passengers": int(data[1]),
                    "unhappy_passengers": int(data[2]),
                    "happy_customer_ratio": round(float(data[1]) / float(data[2]), 2)
                }
                routes.append(route_dict)
            else:
                print("Error reading line")


read_route_data("routes.txt")
print(routes)