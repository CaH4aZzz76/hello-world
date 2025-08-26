def print_board(board):
    print("Текущее поле:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    for row in board:
        if " " in row:
            return None
    return "Ничья"


def get_move(player, board):
    while True:
        coords = input(f"Игрок {player}, введите координаты (строка и столбец через пробел, 1-3): ").split()

        if len(coords) != 2:
            print("Введите две координаты через пробел.")
            continue

        if not (coords[0].isdigit() and coords[1].isdigit()):
            print("Введите целые числа.")
            continue

        x, y = map(int, coords)

        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Координаты должны быть в диапазоне от 1 до 3.")
            continue

        if board[x - 1][y - 1] != " ":
            print("Эта клетка занята, выберите другую.")
            continue

        return x - 1, y - 1

def main():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        x, y = get_move(current_player, board)
        board[x][y] = current_player

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Ничья":
                print("Игра окончена: ничья!")
            else:
                print(f"Игра окончена! Победил игрок {result}!")
            break
        current_player = "O" if current_player == "X" else "X"

main()