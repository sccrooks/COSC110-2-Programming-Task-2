import csv
import re

routes = []


def sort_route_data(list: list[dict]) -> list[dict]:
    sorted_routes = sorted(list, key=lambda d: d['happy_customer_ratio'])
    return sorted_routes


def verify_route(string: str) -> bool:
    """

    :param string: route
    :return:
    """
    regex = r'^\d+,\d+,\d+$'
    if re.search(regex, string) is not None:
        return True
    else:
        return False


def create_route_dict(route_data: str) -> dict:
    """

    :param route_data:
    :return:
    """
    data = route_data.split(',')

    route_dict = {
        "route_id": int(data[0]),
        "happy_passengers": int(data[1]),
        "unhappy_passengers": int(data[2]),
        "happy_customer_ratio": round(float(data[1]) / float(data[2]), 2)
    }

    return route_dict


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
            if verify_route(row[0]):
                routes.append(create_route_dict(row[0]))
            else:
                print("Error reading line")


read_route_data("routes.txt")
routes = sort_route_data(routes)
print(routes)
