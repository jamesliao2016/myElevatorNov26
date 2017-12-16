"Reinforcement Learning Gamblers Problem"
"Value iteration method to generate v* and pi*"
"@author = Prateek Bhat"
# Revised above author's code

# import plotly.plotly as py
# import plotly.graph_objs as go
import matplotlib.pyplot as plt

# py.sign_in('username', 'API key')

"Discount factor"
gamma = 1
"Probability of occurence of Head"
probhead = 0.4
"The number of states availabe"
numStates = 100
"List for storing the reward value"
reward = [0 for _ in range(101)]
reward[100]=1
"Small threshold value for comparing the difference"
theta = 1e-15
"List to store the value function for all states form 1 to 99"
value=[0 for _ in range(101)]
"List to store the amount of bet that gives the max reward"
policy = [0 for _ in range(101)]


def gambler():
    delta = 1
    iteraNum = 1
    while delta > theta:
        delta = 0
        "Looping over all the states i.e the money in hand for a current episode"
        for i in range(1,numStates):
            oldvalue = value[i]
            bellmanequation(i)
            diff = abs(oldvalue-value[i])
            delta = max(delta,diff)
        iteraNum += 1
    print (value)
    print(iteraNum)

    # xaxis = [i for i in range(100)]
    # del value[101:]
    # del value[:1]
    # del policy[101:]
    # del policy[:1]
    # print(len(xaxis))
    print(len(policy))
    print(value)
    plt.plot(policy)
    # plt.plot(value)
    plt.show()
    # print(policy)
def bellmanequation(num):
    "Initialize optimal value to be zero"
    optimalvalue = value[num]
    "The range of number of bets"
    for bet in range(0,min(num,100-num)+1):
        "Amount after winning and loosing"
        win = num + bet
        loss = num - bet
        "calculate the average of possible states for an action"
        "In this case it would be Head or Tails"
        sum = probhead * (reward[win] + gamma * value[win]) \
              + (1 - probhead) * (reward[loss] + gamma * value[loss])
        "Choose the action that gives the max reward and update the policy and value for that"
        if sum > optimalvalue:
            optimalvalue = sum
            value[num] = sum
            policy[num] = bet

if __name__=="__main__":
    gambler()