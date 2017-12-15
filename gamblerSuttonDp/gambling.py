__author__ = 'milicagasic, phs26'

import argparse
from Gambler import *
from Coin import *

def test_gambler(coin, gambler, starting_capital, attempts):
    """
    Test function
    """

    #current attempt
    i = 0

    #total loss
    loss = 0

    while i < attempts:
        #initialise the captial in this attempt
        capital = starting_capital

        #while it is possible to bet
        while capital > 0 and capital < 100:
            #choose the stake according to gamblers strategy
            action = gambler.strategy(capital)
            #throw the coin
            coin_outcome=coin.throw()
            #update capital
            new_capital =gambler.update_capital(coin_outcome,capital,action)
            #calcuate the loss
            loss += capital - new_capital
            #new capital
            capital = new_capital

        i+=1
    return loss


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Gambling')
    parser.add_argument('-c', '--capital', help='set the starting capital amount', default=75, type=int)
    parser.add_argument('-p', '--head_prob', help='set the head probability of a coin', default=0.4, type=float)
    args = parser.parse_args()

    capital = args.capital
    p = args.head_prob

    coin = Coin(p)
    gamblers = [Gambler(p), Gambler()]

    ## TODO test random gambler

    ## TODO print how much the random gamler has lost

    ## TODO test informed gambler

    ## TODO print how much informed gambler has lost
