__author__ = 'milicagasic, phs26'

import random
import numpy
import math

import matplotlib.pyplot as plt


class Gambler:
    
    def __init__(self, p=-1):
        """ 
        Gambler constructor.

        Parameters
        ----------
        p:      probability of scoring heads (default: -1 for no knowledge)
        kind:   gambler type [random|informed] 
        """
        if p < 0:   # the gambler has no knowledge of the coin
            self.kind = 'random'
        else:       # the gambler has the knowledge of the coin
            self.kind = 'informed'

            #probability of coin turning 0 and 1
            self.Prob = [1 - p, p]

            #perform strategy learning
            self.value_iteration()


    def update_allowed_stakes(self, capital):
        """ 
        The allowed stakes for a given capital
        """ 
        stakes = []

        # the gambler can only bet if he/she has between 1 and 99 dollars
        if capital > 0 and capital < 100:
            #the gambler's goal is to reach 100 dollars so only betting upto maximum
            for a in range(1, min(capital, 100 - capital) + 1):
                stakes.append(a)
        return stakes


    def update_capital(self, coin_outcome, capital, stake):
        """
        Update the capital:
            Remove the money of the last bet if unsuccessful
            Add if successful
        """
        if coin_outcome == 0:
            new_capital = capital - stake
        else:
            new_capital = capital + stake

        return new_capital

    def random_strategy(self, capital):
        """
        Randomly choose allowed stake
        """
        # first check the allowed stakes
        stakes = self.update_allowed_stakes(capital)

        #then choose a random allowed stake
        self.stake = random.choice(stakes)

        return self.stake

    def reward(self, new_capital):
        """
        The gambler reaches the goal when the new cpaital is 100
        """
        if new_capital == 100:
            return 1
        else:
            return 0

    def stake_values(self, capital):

        # value for each stake is initially unknown
        # TODO: initialise stake_values to empty list

        # we iterate over possible stakes
        possible_stakes = self.update_allowed_stakes(capital)

        # TODO: for every possible stake

        # TODO: initialise stake value to zero

        # TODO: for every possible coin outcome

        # TODO using the function self.update_capital() estimate new_capital

        # probability of outcome times future reward

        # TODO: estimate the reward of new_capital using self.reward function
        # add it to self.capital_value of new_capital,
        # scale the sum with probability of that outcome and add it to the value

        # TODO: add value to the list stake_values

        # TODO: return stake_values

    def value_iteration(self):
        """
        Core update algorithm
        """

        # initial capital values
        self.capital_values = numpy.zeros(101)

        #initial possible starting capital
        capitals = range(101)

        while True:

            Delta = 0

            for capital in capitals:
                # keep the record of old value for each possible starting capital
                v = self.capital_values[capital]

                #keep initial and final dummy state for zero capital and 100 capital - do not update the value
                if capital == 0 or capital == 100:
                    continue

                # what is the value of each allowed stake for this capital
                stake_values = self.stake_values(capital)

                #TODO: value of the capital is the value of the stake which has the highest value

                # keep track of how much the capital values have changed
                Delta = max(Delta, math.fabs(v - self.capital_values[capital]))

            # if the values have not changed a lot then break
            if Delta < math.exp(-20):
                break

    def learned_strategy(self, capital):
        """
        Informed strategy
        """

        # estimate the value of each action for a given state
        stake_values = self.stake_values(capital)

        #return the action that has the highest value
        return numpy.argmax(stake_values) + 1

    def plot_value_function(self):
        """
        Plot value function with respect to the cpitals
        """
        # possible capitals: 1 to 99
        capitals = range(1, 100)
        # plot values for possible capitals (do not plot capital points 0 and 99)
        plt.plot(capitals, self.capital_values[1:-1], '-')
        plt.xlabel("Capital")
        plt.ylabel("Value estimates")
        plt.show()


    def strategy(self, state):
        """
        Depending on the kind of gambler choose the corresponding strategy
        """
        if self.kind == 'random':
            return self.random_strategy(state)
        elif self.kind == 'informed':
            return self.learned_strategy(state)
        else:
            raise (Exception("No valid kind is given"))


    def plot_strategy(self):
        """
        Plot the statgy curve using matplotlib
        """
        # possible states
        capitals = range(1, 100)

        #policy
        strategy = []
        for capital in capitals:
            strategy.append(self.learned_strategy(capital))

        #plot values for policy

        plt.plot(capitals, strategy, "-")
        plt.xlabel("Capital")
        plt.ylabel("Stake")
        plt.show()
