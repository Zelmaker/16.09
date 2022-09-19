import re
import json


def load_data() -> dict:
    file = open("homework16.json")
    loaded_data = json.load(file)
    return loaded_data


def make_list_of_logins() -> list:
    logins_to_check = []
    for i in loaded_json:
        logins_to_check.append(i["login"])
    return logins_to_check


def main() -> None:
    list_to_check = make_list_of_logins()
    r = re.compile("^([^A-Z])(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{5,10}[^@$!%*?&_-]$")
    newlist = list(filter(r.search, list_to_check))
    print(newlist)


if __name__ == "__main__":
    loaded_json = load_data()
    main()
