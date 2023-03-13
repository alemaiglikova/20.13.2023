class Chessboard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.numbers_to_letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def is_on_board(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def get_square(self, square):
        if len(square) != 2:
            raise ValueError("Invalid square: {}".format(square))
        letter, number = square[0].lower(), square[1]
        if letter not in self.letters_to_numbers:
            raise ValueError("Invalid square: {}".format(square))
        x = self.letters_to_numbers[letter]
        y = int(number) - 1
        if not self.is_on_board(x, y):
            raise ValueError("Invalid square: {}".format(square))
        return x, y


class Queen:
    def __init__(self, square):
        self.x, self.y = Chessboard().get_square(square)

    def can_attack(self, square):
        x, y = Chessboard().get_square(square)
        return self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y)


class Knight:
    def __init__(self, square):
        self.x, self.y = Chessboard().get_square(square)

    def can_attack(self, square):
        x, y = Chessboard().get_square(square)
        dx, dy = abs(x - self.x), abs(y - self.y)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


if __name__ == '__main__':
    try:
        queen_square = input("Введите координаты клетки ферзя (например, a1): ")
        queen = Queen(queen_square)
        target_square = input("Введите целевую клетку (например, b2): ")
        if queen.can_attack(target_square):
            print("Ферзь может атаковать целевую клетку")
        else:
            print("Ферзь не может атаковать целевую клетку")

        knight_square = input("Введите координаты клетки коня: ")
        knight = Knight(knight_square)
        target_square = input("Введите целевую клетку: ")
        if knight.can_attack(target_square):
            print("Конь может попасть на целевую клетку")
        else:
            print("Конь не может попасть на целевую клетку")
    except ValueError as e:
        print("Ошибка:", e)