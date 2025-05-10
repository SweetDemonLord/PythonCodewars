def validate_battlefield(field):
    from collections import defaultdict
    visited = [[False]*10 for _ in range(10)]
    ship_sizes = defaultdict(int)

    def is_valid(x, y):
        return 0 <= x < 10 and 0 <= y < 10

    def has_diagonal_contact(x, y):
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            if is_valid(x+dx, y+dy) and field[x+dx][y+dy] == 1:
                return True
        return False

    def dfs(x, y, ship):
        if not is_valid(x, y) or visited[x][y] or field[x][y] == 0:
            return
        visited[x][y] = True
        ship.append((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(x+dx, y+dy, ship)

    for i in range(10):
        for j in range(10):
            if field[i][j] == 1 and not visited[i][j]:
                if has_diagonal_contact(i, j):
                    return False  # ships can't touch diagonally
                ship = []
                dfs(i, j, ship)
                xs = [x for x, y in ship]
                ys = [y for x, y in ship]
                if len(set(xs)) > 1 and len(set(ys)) > 1:
                    return False  # ship is not straight
                ship_sizes[len(ship)] += 1

    expected_fleet = {1: 4, 2: 3, 3: 2, 4: 1}
    return ship_sizes == expected_fleet

from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield_scipy(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]


def validate_battlefield2(field):
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in field]))

    ships = []

    # this algorithm uses the field 2-dimensional array itself to store information about the size of ships found
    for i in range(0, 10):
        for j in range(0, 10):
            # if not at end of any edge in 2d-array, check that sum of two cross diagonal elements is not more than max
            # if it is then two ships are two close
            if j < 9 and i < 9:
                if field[i][j] + field[i + 1][j + 1] > max(field[i][j], field[i + 1][j + 1]):
                    return False
                if field[i + 1][j] + field[i][j + 1] > max(field[i + 1][j], field[i][j + 1]):
                    return False
            # if the element at position (i, j) is occupied then add the current value of position to next
            if j < 9 and field[i][j] > 0 and field[i][j + 1] > 0:
                field[i][j + 1] += field[i][j]
            elif i < 9 and field[i][j] > 0 and field[i + 1][j] > 0:
                field[i + 1][j] += field[i][j]
            elif field[i][j] > 0:
                ships.append(field[i][j])  # since we add numbers

    ships.sort()

    return ships == [1, 1, 1, 1, 2, 2, 2,
                     3, 3, 4]  # if the ships we have found are of correct configuration then it will equal this array
battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield2(battleField))

print(validate_battlefield_scipy(battleField))