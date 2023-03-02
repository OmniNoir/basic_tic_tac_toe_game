X = "X"

O = "O"

class game:

    def __init__(self):

        self.player_turn = 0

        self.message = ""

        self.game_board = []

        self.game_not_ended = True

        self.count = 0

        self.print_board

    def print_board(self):

        print("-----     ____   -----   ___      ____  _____       ____\n"
              "  |    |  |        |    /   \    |        |  /---\  |\n"
              "  |    |  |        |   / ___ \   |        |  |    | |---\n"
              "  |    |  |___     |  /       \  |___     |  \___/  |___   by Noir.\n")

        for x in range(0, 3):

            y = abs(x - 3)

            print(" ")

            print(str(y) + " " + self.game_board[-2 + (1 - x)][0] + " | " + self.game_board[-2 + (1 - x)][1] + " | " + self.game_board[-2 + (1 -x)][2])

        print("\n"
              "  " + "1" + "   " + "2" + "   " + "3")

    def check_for_pattern(self, player):

        if self.game_board[0][0] == player.symbol and self.game_board[0][1] == player.symbol and self.game_board[0][2] == player.symbol: return True

        elif self.game_board[1][0] == player.symbol and self.game_board[1][1] == player.symbol and self.game_board[1][2] == player.symbol: return True

        elif self.game_board[2][0] == player.symbol and self.game_board[2][1] == player.symbol and self.game_board[2][2] == player.symbol: return True

        elif self.game_board[0][0] == player.symbol and self.game_board[1][0] == player.symbol and self.game_board[2][0] == player.symbol: return True

        elif self.game_board[0][1] == player.symbol and self.game_board[1][1] == player.symbol and self.game_board[2][1] == player.symbol: return True

        elif self.game_board[0][2] == player.symbol and self.game_board[1][2] == player.symbol and self.game_board[2][2] == player.symbol: return True

        elif self.game_board[0][0] == player.symbol and self.game_board[1][1] == player.symbol and self.game_board[2][2] == player.symbol: return True

        elif self.game_board[0][2] == player.symbol and self.game_board[1][1] == player.symbol and self.game_board[2][0] == player.symbol: return True

        return False

    def main(self):

        while self.game_not_ended:

            self.game_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

            self.count = 0

            while self.game_not_ended:

                self.print_board()

                if self.player_turn == 0:

                    int_y, int_x = input("\n").split()

                    int_y = int(int_y)

                    int_x = int(int_x)

                    if self.game_board[int_y - 1][int_x - 1] == player2.symbol:

                        print("\n"
                              "Cannot not place X on player 2 symbol.")

                        continue

                    if int_y > 0 and int_y < 4 and int_x > 0 and int_x < 4:

                        self.game_board[int_y - 1][int_x - 1] = player1.symbol

                        self.count += 1

                        if self.check_for_pattern(player1):

                            self.print_board()

                            print("Player 1 has won!")

                            self.game_not_ended = False

                            break

                        elif self.count >= 8:

                            player_input = input("\n"
                                                 "Draw! Want to play again? Y/N: ").lower()

                            if player_input == "yes" or player_input == "y":

                                break

                        else:

                            self.player_turn = 1

                    else:

                        print("\n"
                              "Out of range. Please try again.")

                elif self.player_turn == 1:

                    int_y, int_x = input("\n"
                                         "").split()

                    int_y = int(int_y)

                    int_x = int(int_x)

                    if self.game_board[int_y - 1][int_x - 1] == player1.symbol:

                        print("\n"
                              "Cannot not place O on player 1 symbol.")

                        continue

                    if int_y > 0 and int_y < 4 and int_x > 0 and int_x < 4:

                        self.game_board[int_y - 1][int_x - 1] = player2.symbol

                        self.count += 1

                        if self.check_for_pattern(player2):

                            self.print_board()

                            print("Player 2 has won!")

                            self.game_not_ended = False

                            break

                        elif self.count >= 8:

                            player_input = input("\n"
                                                 "Draw! Want to play again? Y/N: ").lower()

                            if player_input == "yes" or player_input == "y":

                                break

                        else:

                            self.player_turn = 0

                    else:

                        print("\n"
                              "Out of range. Please try again.")

class player:

    def __init__(self, symbol):

        self.symbol = symbol

player1, player2 = player(symbol=X), player(symbol=O)

Game = game()

Game.main()