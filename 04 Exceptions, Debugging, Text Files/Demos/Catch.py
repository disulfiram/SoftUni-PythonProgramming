people = [{'name': "Мария", 'gender': "female", }, {'name': "Калоян", 'gender': "male", }, ]


def print_person(person: dict):
    print("{} ({}) is interested in {}".format(
        person['name'],
        person['age'],
        ', '.join(person['interests'])
    ))


def print_people(people: list):
    for person in people:
        print_person(person)

try:
    print_people(people)
except KeyError as e:
    print("Unhandled KeyError exception: " + str(e))