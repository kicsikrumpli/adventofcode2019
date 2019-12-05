def intersect_segments(line_one, line_two):
    X1, X2, Y1, Y2 = 0, 2, 1, 3

    def is_horizontal(line):
        return line[X1] != line[X2] and \
               line[Y1] == line[Y2]

    def is_vertical(line):
        return line[Y1] != line[Y2] and \
               line[X1] == line[X2]

    def is_perpendicular():
        return (is_vertical(line_one) and is_horizontal(line_two)) or \
               (is_vertical(line_two) and is_horizontal(line_one))

    def align_line(line):
        if line[X1] < line[X2] or line[Y1] < line[Y2]:
            return (line[X1], line[Y1]), (line[X2], line[Y2])
        else:
            return (line[X2], line[Y2]), (line[X1], line[Y1])

    vertical = line_one if is_vertical(line_one) else line_two
    horizontal = line_one if is_horizontal(line_one) else line_two
    vertical_bottom, vertical_top = align_line(vertical)
    horizontal_left, horizontal_right = align_line(horizontal)
    if is_perpendicular() and \
            horizontal_left[X1] <= vertical_top[X1] <= horizontal_right[X1] and \
            vertical_top[Y1] >= horizontal_right[Y1] >= vertical_bottom[Y1]:
        return vertical_bottom[X1], horizontal_left[Y1]
    else:
        return None


def make_directions_from_string(str):
    """
    in "R1,U10,L3"
    out [(R, 1), (U, 10), (L, 3)]
    """
    return list(map(lambda x: (x[0], int(x[1:])), str.split(sep=",")))


def make_nodes(instructions, start=(0,0)):
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
        x, y = nodes[-1]
        dx, dy = delta(direction, distance)
        nodes.append((x + dx, y + dy))
    return nodes


def make_segments_from_nodes(nodes):
    """
    in [(x1,y1), (x2, y2), (x3, y3) ...]
    out [(x1,y1,x2,y2), (x2,y2,x3,y3), ...]
    """
    return [(*pair[0], *pair[1]) for pair in zip(nodes, nodes[1:])]


def main(input):
    with open(input) as lines:
        directions = (make_directions_from_string(line) for line in lines)
        nodes = (make_nodes(instructions) for instructions in directions)
        wire_1, wire_2 = (make_segments_from_nodes(node_list) for node_list in nodes)
        intersections = (intersect_segments(segment_1, segment_2) for segment_1 in wire_1 for segment_2 in wire_2)
        real_intersections = filter(lambda intersection: intersection is not None, intersections)
        closest_intersection = sorted(map(lambda point: abs(point[0]) + abs(point[1]), real_intersections))
        print(closest_intersection[0])


if __name__ == "__main__":
    main("input.txt")
