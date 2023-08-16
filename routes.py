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
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            if verify_route(', '.join(row)):
                data = row[0].split(',')

                route_dict = {
                    "route_id": int(data[0]),
                    "happy_passengers": int(data[1]),
                    "unhappy_passengers": int(data[2])
                }
                routes.append(route_dict)
            else:
                print("Error reading line")


read_route_data("routes.txt")
print(routes)