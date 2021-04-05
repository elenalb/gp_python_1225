# композиция


# len1 * height
# len2 * height
# S = 2 * (len1 * height + len2 * height) - s_windows - s_doors


class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height


class Room:
    def __init__(self, len1, len2, height):
        self.square = 2 * (len1 * height + len2 * height)
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for wd in self.wd:
            main_square -= wd.square
        return main_square


r = Room(10, 15, 3)
print(r.square)
r.add_win_door(2, 2)  # 4
r.add_win_door(1, 1)  # 1
r.add_win_door(2, 1)  # 2
for el in r.wd:
    print(f"Площадь окна-двери: {el.square}")
print(r.common_square())
