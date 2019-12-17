def total_steps_to_segment_intersect(line_one, line_two):
    X1, X2, Y1, Y2 = 0, 2, 1, 3

    def is_horizontal(line):
        return line[X1] != line[X2] and \
               line[Y1] == line[Y2]

    def is_vertical(line):
        return line[Y1] != line[Y2] and \
               line[X1] == line[X2]

    def is_perpendicular():
        return (is_vertical(line_one[0]) and is_horizontal(line_two[0])) or \
               (is_vertical(line_two[0]) and is_horizontal(line_one[0]))

    def align_line(line):
        if line[X1] < line[X2] or line[Y1] < line[Y2]:
            return (line[X1], line[Y1]), (line[X2], line[Y2])
        else:
            return (line[X2], line[Y2]), (line[X1], line[Y1])

    def dist(x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    vertical = line_one if is_vertical(line_one[0]) else line_two
    horizontal = line_one if is_horizontal(line_one[0]) else line_two
    vertical_bottom, vertical_top = align_line(vertical[0])
    horizontal_left, horizontal_right = align_line(horizontal[0])
    intersection = (vertical_bottom[X1], horizontal_left[Y1])
    length_to_intersection = vertical[1] + \
                             horizontal[1] + \
                             dist(*vertical[0][0:2], *intersection) + \
                             dist(*horizontal[0][0:2], *intersection)
    if is_perpendicular() and \
            horizontal_left[X1] <= vertical_top[X1] <= horizontal_right[X1] and \
            vertical_top[Y1] >= horizontal_right[Y1] >= vertical_bottom[Y1]:
        return length_to_intersection
    else:
        return None


def make_directions_from_string(str):
    """
    in "R1,U10,L3"
    out [(R, 1), (U, 10), (L, 3)]
    """
    return list(map(lambda x: (x[0], int(x[1:])), str.split(sep=",")))


def make_nodes(instructions, start=((0, 0), 0)):
    """
    in [(R, 1), (U, 10), (L, 3)]
    out [(0,0), (1,0), (1,10), (-2,10)]
    """
    UP, DOWN, LEFT, RIGHT = "U", "D", "L", "R"

    def delta(dirr, dist):
        def is_vertical():
            return dirr == UP or dirr == DOWN

        def is_positive_direction():
            return dirr == RIGHT or dirr == UP

        signum = 1 if is_positive_direction() else -1
        d_x = 0 if is_vertical() else signum * dist
        d_y = signum * dist if is_vertical() else 0
        return d_x, d_y

    nodes = [start]
    for element in instructions:
        direction, distance = element
        (x, y), d0 = nodes[-1]
        dx, dy = delta(direction, distance)
        nodes.append(((x + dx, y + dy), d0 + distance))
    return nodes


def make_segments_from_nodes(nodes):
    """
    in [((x1,y1), l0), ((x2, y2), l1), ((x3, y3), l2) ...]
    out [(x1,y1,x2,y2), (x2,y2,x3,y3), ...]
    """
    return [((*pair[0][0], *pair[1][0]), pair[0][1]) for pair in zip(nodes, nodes[1:])]


def main(input_file):
    with open(input_file) as lines:
        directions = (make_directions_from_string(line) for line in lines)
        nodes = (make_nodes(instructions) for instructions in directions)
        wire_1, wire_2 = (make_segments_from_nodes(node_list) for node_list in nodes)
        intersections = (total_steps_to_segment_intersect(segment_1, segment_2) for segment_1 in wire_1 for segment_2 in wire_2)
        real_intersections = filter(lambda intersection: intersection is not None, intersections)
        closest_intersection = sorted(real_intersections)
        print(closest_intersection[0])


if __name__ == "__main__":
    main("input.txt")
