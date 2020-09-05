import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # r1, r2
    #  _________
    # [____A____]_______
    #           [___B___]
    # if two rectangles make intersection return rectangle of intersection
    # they intersect?

    # if both:
    # find who's if one y line is between other's y lines
    # find who's if one x line is between other's x lines
    def rect_helper(r1, r2):
        # calculate both y lines
        y1 = r1.y
        y2 = r1.y + r1.height
        other_y1 = r2.y
        other_y2 = r2.y + r2.height
        # calculate both x lines
        x1 = r1.x
        x2 = r1.x + r1.width
        other_x1 = r2.x
        other_x2 = r2.x + r2.width

        if (x1 <= other_x2 and x2 >= other_x1 and
                y1 <= other_y2 and y2 >= other_y1):
            return True

        return False

    def calculate_intersection(r1, r2):
        return Rect(
            max(r1.x, r2.x), 
            max(r1.y, r2.y), 
            min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
            min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y)
        )


         
    if not rect_helper(r1, r2):
        return Rect(0, 0, -1, -1)

    return calculate_intersection(r1, r2)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
