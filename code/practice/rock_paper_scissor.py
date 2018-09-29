"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""

# This program uses if/else to identify winner

def rps_game_():

    while True:
        winner = ''
        player_1 = input('Player-1 Choose Rock-Paper-Scissor:')
        player_2 = input('Player-2 Choose Rock-Paper-Scissor:')

        if player_1 == 'Rock' and player_2 == 'Scissor':
            print('player-1 wins')
            winner = 'player-1'
        elif player_1 == 'Scissor' and player_2 == 'Paper':
            print('player-1 wins')
            winner = 'player-1'
        elif player_1 == 'Paper' and player_2 == 'Rock':
            print('player-1 wins')
            winner = 'player-1'
        if player_2 == 'Rock' and player_1 == 'Scissor':
            print('player-2 wins')
            winner = 'player-2'
        elif player_2 == 'Scissor' and player_1 == 'Paper':
            print('player-2 wins')
            winner = 'player-2'
        elif player_2 == 'Paper' and player_1 == 'Rock':
            print('player-2 wins')
            winner = 'player-2'
        elif player_2 == player_1:
            print('Its a tie ')

        msg = input('Would you like to play again{}? (y/n)'.format(' ' + winner))

        if msg == 'n':
            print('Game Over!')
            break;

# This program uses dictionary to save game possible states
# The winner is found by getting difference between game states


def rps_game():

    print('Please chose rock, paper or scissor')

    game = {'rock': 1, 'paper': 2, 'scissor': 3}

    while True:

        player_1 = input('Player-1: ')
        player_2 = input('Player-2: ')

        res = game.get(player_1) - game.get(player_2)

        if res in [1, -2]:
            print('Player-1 wins')
            if input('Would you like to play again? (y/n)') == 'n':
                print('Game over!')
                break;
        elif res in [-1, 2]:
            print('Player-2 wins')
            if input('Would you like to play again? (y/n)') == 'n':
                print('Game over!')
                break;
        elif res == 0:
            print('Its a tie, please continue ')


if __name__ == "__main__":
    rps_game()
    # rps_game_()