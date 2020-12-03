import itertools

puzzle_input = []

with open('day-6/input.txt', 'r') as file:
    puzzle_input = [i.strip().split(')') for i in file.readlines()]


space_objects = {}


class SpaceObject:
    def __init__(self, name):
        self.name = name
        self.orbits = None

    def set_orbits(self, space_object):
        self.orbits = space_object

    def count_orbits(self):
        return (1 + self.orbits.count_orbits()) if self.orbits else 0

    def path_to_root(self):
        return [self.orbits, *(self.orbits.path_to_root() if self.orbits else [])]

    def __repr__(self):
        return f'<SpaceObject {self.name}>'


def first_common_object(space_obj_1, space_obj_2):
    path_1 = space_obj_1.path_to_root()[:-1]
    path_2 = space_obj_2.path_to_root()[:-1]

    for objects in itertools.product(path_1, path_2):
        if len(set(objects)) == 1:
            return objects[0]

    return False


def distance_between_objects(to_object, from_object):
    counter = 0
    path = from_object.path_to_root()[:-1]

    for obj in path:
        if obj == to_object:
            return counter

        counter += 1

    return False


def part_1(puzzle_input):
    objects_names = set(itertools.chain(*puzzle_input))

    for name in objects_names:
        space_objects[name] = SpaceObject(name)

    for pair in puzzle_input:
        space_objects[pair[1]].set_orbits(space_objects[pair[0]])

    return sum([space_objects[name].count_orbits() for name in objects_names])


def part_2(puzzle_input):
    objects_names = set(itertools.chain(*puzzle_input))

    for name in objects_names:
        space_objects[name] = SpaceObject(name)

    for pair in puzzle_input:
        space_objects[pair[1]].set_orbits(space_objects[pair[0]])

    common = first_common_object(space_objects['YOU'], space_objects['SAN'])

    return distance_between_objects(common, space_objects['YOU'])\
        + distance_between_objects(common, space_objects['SAN'])


print(part_1(puzzle_input))
print(part_2(puzzle_input))
