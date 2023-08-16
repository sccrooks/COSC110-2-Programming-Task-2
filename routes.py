import csv
import re

routes = []


def sort_route_data(list: list[dict]) -> None:
    pass


def verify_route(string: str) -> bool:
    regex = "^\d+,\d+,\d+$"
    if re.search(regex, string) is not None:
        return True
    else:
        return False


def read_route_data(file: str):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if verify_route(', '.join(row)):
                print(', '.join(row))
            else:
                print("false")


read_route_data("routes.txt")
