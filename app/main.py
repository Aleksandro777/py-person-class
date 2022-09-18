class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person_list.append(Person(human["name"], human["age"]))

    for human in people:
        if human.get("wife") is not None:
            Person.people[human["name"]].wife = \
                Person.people[human["wife"]]
        elif human.get("husband") is not None:
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
    return person_list
