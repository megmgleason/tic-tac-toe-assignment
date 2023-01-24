##emfrom tic_tac_toe.game import Player, Game
from tic_tac_toe.game import Player, Game, Board
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent

AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Random Agent", RandomAgent)
]


def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = "\n".join(
                map(lambda x: "\t{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: \n{}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent
        except ValueError:
            return None

    agent = _try_pick()

    while agent is None:
        print("Incorrect selection, try again.")
        agent = _try_pick()

    return AGENTS[agent][1](player)

import time
def main():
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    play = "y"


    num_plays = 0
    total_plays = 1000
    start_time = time.time()
    process_time = time.process_time()
    num_draws = 0
    num_x_wins = 0
    num_o_wins = 0


    while (num_plays < total_plays):
     #   while play == "y":
            game = Game(player_x, player_o)
            game.play()
            winner = Board.winner


            num_plays += 1
            num_draws = Game.num_draws
            num_x_wins = Game.num_x_wins
            num_o_wins = Game.num_o_wins


    print("Average wall time of each game: {}".format((float((time.time() - start_time)/ total_plays)) * 1000) + " milliseconds")
    print("Average CPU processing time of each game: {}".format((float(time.process_time()-process_time) / total_plays) * 1000) + " milliseconds")
    print("number of draws: {}".format(num_draws))
    print("number of X wins: {}".format(num_x_wins))
    print("number of O wins: {}".format(num_o_wins))




if __name__ == "__main__":
    main()
