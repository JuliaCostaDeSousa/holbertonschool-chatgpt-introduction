#!/usr/bin/python3

def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie si un joueur a gagné."""
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification de la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérification de la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Joue une partie de Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]  # Initialisation du plateau
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Vérification des entrées valides pour les lignes et colonnes
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter values between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Mise à jour du plateau
            board[row][col] = player

            # Changement de joueur
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter integers only.")
    
    print_board(board)
    print(f"Player {player} wins!")  # Affiche le bon gagnant (celui qui a joué dernier)

if __name__ == "__main__":
    tic_tac_toe()
