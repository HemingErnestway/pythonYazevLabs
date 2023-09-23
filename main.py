from test_shape_contains_point import *
import pandas as pd


def main():
    # auto_test_shape_contains_point()
    # manual_test_shape_contains_point()

    r = 2.45
    points = generate_coordinates(100_000, r)
    df = pd.DataFrame(
        np.array([[round(p.x, 2), round(p.y, 2), shape_contains_point(p, r)]
                  for p in points]),
        columns=['x', 'y', 'P'],
        index=[i + 1 for i in range(len(points))])

    df.to_excel('data.xlsx', index=False)
    bd = pd.read_excel('data.xlsx')
    print(bd)

    # print(check_generated_points(points, r))
    # log_check_generated_points(points, r)


if __name__ == '__main__':
    main()
