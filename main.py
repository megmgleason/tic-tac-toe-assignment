from tic_tac_toe.game import Player, Game
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent
from tic_tac_toe.agents.smart_agent import SmartAgent
from tic_tac_toe.agents.smart_agent_pruning import SmartAgentPruning
from tic_tac_toe.agents.suboptimal_agent import SuboptimalAgent


AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Random Agent", RandomAgent),
    ("Smart Agent", SmartAgent),
    ("Smart Agent w/ Alpha Beta Pruning", SmartAgentPruning),
    ("Suboptimal Agent", SuboptimalAgent)
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


def main():
    num_plays = 0
    x_wins = 0
    o_wins = 0
    ties = 0
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    play = "y"

    ##go back and put this in methods with error handling pls
    print("")
    board_size = int(input("Choose a size for the board... "))

    num_to_win = int(input("Choose a winning length... "))


    print("")

    while play == "y":
        game = Game(player_x, player_o, board_size, num_to_win )
        game.play()
        play = input("Play again? y/[n]: ")
    # while num_plays < 100:
    #     num_plays = num_plays + 1
    #     game = Game(player_x, player_o, board_size, num_to_win)
    #     game.play()





if __name__ == "__main__":
    main()
