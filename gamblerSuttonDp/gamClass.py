
p = 0.4
kind = 'random'
Prob = [ 1 - p, p ]

if p < 0 :
    kind = 'random'
else :
    kind = 'informed'

for i in [0, 1]:
    print ("Probability of coin turning", i, "is", Prob[i], "\n")

i = 0
while i < 2:
    print ("Probability of coin turning", i, "is", Prob[i], "\n")
    i += 1

def sum(stakes):
    total = 0
    for elem in stakes:
        total += elem
    return total

print (sum([10, 20]))
print (sum([20, 40, 80]))

stake = [] #empty list
stake.append(10) #adding 10 to the list

print (range(5))


class Gambler:
    def __init__(self, p=-1):
        """
        Gambler constructor.

        Parameters
        ----------
        p:      probability of scoring heads (default: -1 for no knowledge)
        kind:   gambler type [random|informed]
        """
        if p < 0:  # the gambler has no knowledge of the coin
            self.kind = 'random'
        else:  # the gambler has the knowledge of the coin
            self.kind = 'informed'

            # probability of coin turning 0 and 1
            self.Prob = [1 - p, p]

            # perform strategy learning
            self.value_iteration()

    def update_allowed_stakes(self, capital):
        """
        The allowed stakes for a given capital
        """
        stakes = []

        # the gambler can only bet if he/she has between 1 and 99 dollars
        if capital > 0 and capital < 100:
            # the gambler's goal is to reach 100 dollars so only betting upto maximum
            for a in range(1, min(capital, 100 - capital) + 1):
                stakes.append(a)
        return stakes

    def reward(self, new_capital):
        """
        The gambler reaches the goal when the new cpaital is 100
        """
        if new_capital == 100:
            return 1
        else:
            return 0

    def learned_strategy(self, capital):
        """
        Informed strategy
        """

        # estimate the value of each action for a given state
        stake_values = self.stake_values(capital)

        #return the action that has the highest value
        return numpy.argmax(stake_values) + 1

    def stake_values(self, capital):

        # value for each stake is initially unknown
        # TODO: initialise stake_values to empty list

        # we iterate over possible stakes
        possible_stakes = self.update_allowed_stakes(capital)

        # TODO: for every possible stake

        # TODO: initialise stake value to zero

        # TODO: for every possible coin outcome

        # TODO using the function self.update_capital() estimate new_capital

        # TODO probability of outcome x ( reward(new_capital) + self.capital_values[new_capital])

        # TODO: estimate the reward of new_capital using self.reward function
        # add it to self.capital_value of new_capital,
        # scale the sum with probability of that outcome and add it to the value

        # TODO: add value to the list stake_values

        return stake_values

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

            for i in range(101):
                # keep the record of old value for each possible starting capital
                v = self.capital_values[i]

                #keep initial and final dummy state for zero capital and 100 capital - do not update the value
                if i == 0 or i == 100:
                    continue

                # what is the value of each allowed stake for this capital
                stake_values = self.stake_values(capitals[i])

                #TODO: value of the capital is the value of the stake which has the highest value

                #keep track of how much the capital values have changed
                Delta = max(Delta, math.fabs(v - self.capital_values[i]))

            #if the values have not changed a lot then break
            if Delta < math.exp(-20):
                break

random_gambler = Gambler()
print (random_gambler.kind)

gamblers = [Gambler(p), Gambler()]