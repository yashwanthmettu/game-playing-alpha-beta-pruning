import sys

def red_blue_nim():
    if len(sys.argv) < 2:
        print("command need to be filled with atleast 3 arguments ")
        sys.exit()
    red_balls = int(sys.argv[1])
    blue_balls = int(sys.argv[2])

    if len(sys.argv) < 4:
        player='computer'
        version = 'standard'

    else:
        version = sys.argv[3].lower()

        if version=="computer" or version=="human":
            player=version
            version='standard'
        else:
            player='computer' if len(sys.argv)<5 else sys.argv[4].lower()

    if version=='computer' or version=='human':
        player=version
        version='standard'

    #player='human' if len(sys.argv)>=5 and sys.argv[4]=='human' else 'computer'

    level=None if len(sys.argv) < 6 else int(sys.argv[5])
    balls = {"red": red_balls, "blue": blue_balls}
    print(f" red balls:{red_balls} and blue balls:{blue_balls} and player: {player}")

    if version == 'standard':
        standard.red_blue_nim_game(balls, player, level)
    else:
        misere.red_blue_nim_game(balls, player, level)

class standard:
    def red_blue_nim_game(total_balls, player_turn, level):
        no_of_balls = total_balls
        player = player_turn
        count = 0
        def remaining_balls():
            print(f"Balls in the pile are {no_of_balls['red']} red balls and {no_of_balls['blue']} blue balls")
        print("Game Started")
        remaining_balls()

        def repeat():
            nonlocal player, count

            if player == 'human':
                pile, amt = standard.human(no_of_balls)
                no_of_balls[pile] -= amt
                print(f"The user removed {amt} marble(s) from the {pile} pile.")
            elif player == 'system':
                pile, amt = standard.system(no_of_balls, level)
                no_of_balls[pile] -= amt
                print(f"system eliminated {amt} ball from the {pile} pile.")
            remaining_balls()


        while no_of_balls["red"] > 0 and no_of_balls["blue"] > 0:
            repeat()
            if player == 'human':
                player = 'system'
            elif player == 'system':
                player = 'human'

        print("Game Over")

        if no_of_balls["red"] == 0 or no_of_balls["blue"] == 0:
            if player == 'human':
                player = 'system'
            else:
                player = 'human'

        print(f"{player} LOST the Game!")
        final_score = 2 * no_of_balls["red"] + 3 * no_of_balls["blue"]
        print(f"Score: {final_score}")

    def human(balls):
        pile = input("choose the pile (red or blue): ")
        if pile in ["red", "blue"]:
            if balls.get(pile, 0) > 0:
                amt = input(f"how many balls do you want to pick from the selected pile (1/2): ")
                if amt.isdigit():
                    amt=int(amt)
                else:
                    amt=1
                if amt in [1,2]:
                    return pile, amt
        print("Invalid choice")



    def minmax_alpha_beta(balls, level, alpha, beta, is_max):
        if balls["red"] == 0 or balls["blue"] == 0:
            return standard.depth(balls,is_max)

        if is_max:
            res = float("-infinity")
            for move in standard.possible_moves(balls):
                new_balls = balls.copy()
                new_balls[move[0]] -= move[1]
                res = max(res, standard.minmax_alpha_beta(balls, 100 if level == None else level - 1, alpha, beta, False))
                alpha = max(alpha, res)
                if beta <= alpha:
                    break
            return res
        else:
            res = float("infinity")
            for move in standard.possible_moves(balls):
                new_balls = balls.copy()
                new_balls[move[0]] -= move[1]
                res = min(res, standard.minmax_alpha_beta(new_balls, 100 if level == None else level - 1, alpha, beta, True))
                beta = min(beta, res)
                if beta <= alpha:
                    break
            return res

    def system(balls, level):
        best_move = None
        best_move_score = float("-infinity")
        for move in standard.possible_moves(balls):
            new_balls = balls.copy()
            new_balls[move[0]] -= move[1]
            curr_score = standard.minmax_alpha_beta(new_balls, level, float("-inf"), float("inf"), False)
            if curr_score > best_move_score:
                best_move = move
                best_move_score = curr_score
        if best_move is not None:
            return best_move[0], best_move[1]
        else:
            return None, None

    def possible_moves(balls):
        moves = []
        if balls["red"] > 0:
            if balls["red"]>2:
                moves.append(("red", 2))
            elif balls["red"]>=1:
                moves.append(("blue", 1))
            else:
                moves.append(("red", 1))
        if balls["blue"] > 0:
            if balls["blue"]>2:
                moves.append(("blue", 2))
            elif balls["blue"]>=1:
                moves.append(("red", 1))
            else:
                moves.append(("blue", 1))
        return moves

    def depth(balls, is_max):
        if is_max:
            return -(2*balls["red"]+3*balls["blue"])
        else:
            return (2*balls["red"]+3*balls["blue"])

class misere:
    def red_blue_nim_game(total_balls, player_turn, level):
        no_of_balls = total_balls
        player = player_turn
        def remaining_balls():
            print(f"no of balls present in the pile are: {no_of_balls['red']} red balls, {no_of_balls['blue']} blue balls")

        print("Game Started")
        remaining_balls()

        def repeat():
            nonlocal player
            if player == 'human':
                pile,amt = misere.human(no_of_balls)
                no_of_balls[pile] -= amt
                print(f"{amt} marble(s) removed from {pile} pile.")
            elif player == 'system':
                pile, amt = misere.system(no_of_balls, level)
                no_of_balls[pile] -= amt
                print(f"system eliminated {amt} from the {pile} pile.")
            remaining_balls()

        while no_of_balls["red"] > 0 and no_of_balls["blue"] > 0:
            repeat()
            if player == 'human':
                player = 'system'
            elif player == 'system':
                player = 'human'


        print("Game Over")


        print(f"{player} WON the game!")
        final_score = 2 * no_of_balls["red"] + 3 * no_of_balls["blue"]
        print(f"Score: {final_score}")

    def human(balls):
        pile = input("choose the pile (red or blue): ")
        if pile in ["red", "blue"]:
            if balls.get(pile, 0) > 0:
                amt = input(f"how many balls do you want to pick from the selected pile (1/2): ")
                if amt.isdigit():
                    amt = int(amt)
                elif amt!=2 or amt!=1:
                    print("Invalid choice")
                if amt in [1, 2]:
                    return pile, amt
                else:
                    print("Invalid choice")

        print("Invalid choice")

    def maxmin_alpha_beta(balls, level, alpha, beta, is_min):
        if balls["red"] == 0 or balls["blue"] == 0:
            return misere.depth(balls,is_min)

        if is_min:
            res = float("-infinity")
            for move in misere.possible_moves(balls):
                new_balls = balls.copy()
                new_balls[move[0]] -= move[1]
                res = max(res, misere.maxmin_alpha_beta(balls, 100 if level == None else level - 1, alpha, beta, False))
                alpha = max(alpha, res)
                if beta <= alpha:
                    break
            return res
        else:
            res = float("infinity")
            for move in misere.possible_moves(balls):
                new_balls = balls.copy()
                new_balls[move[0]] -= move[1]
                res = min(res,
                          misere.maxmin_alpha_beta(new_balls, 100 if level == None else level - 1, alpha, beta, True))
                beta = min(beta, res)
                if beta <= alpha:
                    break
            return res

    def system(balls, level):
        best_move = None
        best_move_score = float("-infinity")
        for move in misere.possible_moves(balls):
            new_balls = balls.copy()
            new_balls[move[0]] -= move[1]
            curr_score = misere.maxmin_alpha_beta(new_balls, level, float("-inf"), float("inf"), False)
            if curr_score > best_move_score:
                best_move = move
                best_move_score = curr_score
        if best_move is not None:
            return best_move[0], best_move[1]
        else:
            return None, None

    def possible_moves(balls):
        moves = []
        if balls["red"] > 0:
            moves.append(("red", 1))
        if balls["blue"] > 0:
            moves.append(("blue", 1))
        return moves

    def depth(balls, is_min):
        if is_min:
            return (2*balls["red"]+3*balls["blue"])
        else:
            return -(2*balls["red"]+3*balls["blue"])

red_blue_nim()
