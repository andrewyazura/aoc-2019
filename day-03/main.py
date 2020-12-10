import collections

with open('day-3/input.txt', 'r') as file:
    puzzle_input_str = [[j.strip() for j in i.split(',')]
                        for i in file.readlines()]


def format_input_data(puzzle_input_str):
    puzzle_input = []

    for line in puzzle_input_str:
        puzzle_input.append([])

        for move in line:
            puzzle_input[-1].append([move[0], int(move[1:])])

    return puzzle_input


def build_lines_coords(puzzle_input):
    points_count = collections.defaultdict(
        lambda: collections.defaultdict(list))

    # points_count = {
    #     (x, y): {
    #         'lines': [0, 1],
    #         'distance': [321, 765]
    #     },
    #     ...
    # }

    for line_id in range(len(puzzle_input)):
        pointer = [0, 0]
        steps = 0
        for move in puzzle_input[line_id]:
            if move[0] == 'U':
                for _ in range(move[1]):
                    steps += 1
                    pointer[1] += 1
                    points_count[tuple(pointer)]['lines'].append(line_id)
                    points_count[tuple(pointer)]['distance'].append(steps)

            elif move[0] == 'D':
                for _ in range(move[1]):
                    steps += 1
                    pointer[1] -= 1
                    points_count[tuple(pointer)]['lines'].append(line_id)
                    points_count[tuple(pointer)]['distance'].append(steps)

            elif move[0] == 'R':
                for _ in range(move[1]):
                    steps += 1
                    pointer[0] += 1
                    points_count[tuple(pointer)]['lines'].append(line_id)
                    points_count[tuple(pointer)]['distance'].append(steps)

            elif move[0] == 'L':
                for _ in range(move[1]):
                    steps += 1
                    pointer[0] -= 1
                    points_count[tuple(pointer)]['lines'].append(line_id)
                    points_count[tuple(pointer)]['distance'].append(steps)

    return points_count


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def part_1(puzzle_input):
    puzzle_input = format_input_data(puzzle_input)
    points_coords = build_lines_coords(puzzle_input)

    intersections = []
    for key, value in points_coords.items():
        if len(set(value['lines'])) == 2:
            intersections.append(key)

    distances = [manhattan_distance((0, 0), point) for point in intersections]

    return min(distances)


def part_2(puzzle_input):
    puzzle_input = format_input_data(puzzle_input)
    points_coords = build_lines_coords(puzzle_input)

    intersections = []
    for key, value in points_coords.items():
        if len(set(value['lines'])) == 2:
            intersections.append(key)

    steps = [sum(points_coords[point]['distance']) for point in intersections]
    return min(steps)


print(part_1(puzzle_input_str))
print(part_2(puzzle_input_str))
