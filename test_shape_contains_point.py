from shape_contains_point import *


def auto_test_shape_contains_point() -> None:
    assert shape_contains_point(Point(1, 0), 1) is True
    log_shape_contains_point(Point(1, 0), 1)

    assert shape_contains_point(Point(0, 1), 1) is True
    log_shape_contains_point(Point(0, 1), 1)

    assert shape_contains_point(Point(-1, 0), 1) is True
    log_shape_contains_point(Point(-1, 0), 1)

    assert shape_contains_point(Point(-0.2, 0.3), 0.5) is True
    log_shape_contains_point(Point(-0.2, 0.3), 0.5)

    assert shape_contains_point(Point(0, -1), 1) is False
    log_shape_contains_point(Point(0, -1), 1)

    try:
        shape_contains_point(Point("a", "b"))
    except TypeError:
        print("❌ Invalid input data, expected (Point, float), got (str, str)")

    try:
        shape_contains_point(Point(2, 3), -5)
    except RadiusError:
        print("❌ Invalid input data, radius must be a positive number")


def manual_test_shape_contains_point() -> None:
    print("Manual test has started. To quit enter [q]")
    r = float(input("Enter radius (float): "))
    while True:
        user_input = input("Enter x, y (floats) separated by space: ")
        if user_input.lower() == "q":
            break

        if len(user_input.split()) != 2:
            print("❌ You have to pass exactly 2 floats, separated by space")
            continue

        user_input_split = user_input.split()

        try:
            x, y = map(float, user_input_split)
        except ValueError:
            print(f"❌ Unable to parse given values as floats")
            continue

        try:
            log_shape_contains_point(Point(x, y), r)
        except RadiusError:
            print("❌ Radius must be a positive number")
