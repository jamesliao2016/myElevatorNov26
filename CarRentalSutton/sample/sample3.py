'''
Jacks Car Rental problem
source: https://github.com/yyang768osu/SuttonReinforcementLearning
'''
from itertools import product
import copy
import numpy as np


class MM1NQueue(object):
    '''
    define a M/M/1/N queue, where N = max queue size
    '''
    def __init__(self, ini_num_pkt, max_num_pkt, arrival_rate, service_rate):
        self.ini_num_pkt = ini_num_pkt
        self.max_num_pkt = max_num_pkt
        self.arrival_rate = float(arrival_rate)
        self.service_rate = float(service_rate)

    def reset_ini_num_pkt(self, ini_num_pkt):
        '''
        reset the initial number of packets
        '''
        self.ini_num_pkt = ini_num_pkt

    def run_one_unit_time(self):
        '''
        run the queue for one unit time and return the (queue_length, num_sevice) tuple
        '''
        queue_length = self.ini_num_pkt
        time = 0
        num_service = 0
        while True:
            t_arrival = np.random.exponential(scale=1/self.arrival_rate)
            t_service = np.random.exponential(scale=1/self.service_rate)
            if t_arrival > t_service:
                time = time + t_service
                if time > 1:
                    break
                if queue_length:
                    num_service += 1
                    queue_length -= 1
            else:
                time = time + t_arrival
                if time > 1:
                    break
                queue_length = min(self.max_num_pkt, queue_length+1)
        return queue_length, num_service

    def run_multiple_unit_slots(self):
        '''
        invoke self.run_one_unit_time multiple times and obtain the following
        statistics:
        end_queue_length_frequency: a list with size self.max_num_pkt+1,
                                    end_queue_length_frequency[n] is the frequency
                                    of the queue length = n at the end of one unit time
        average_num_service: the average number of services at the end of one unit time
        '''
        end_queue_length_frequency = np.array([0]*(self.max_num_pkt+1), dtype=float)
        average_num_service = 0.0
        num_runs = 200000
        for _ in range(num_runs):
            (queue_length, num_service) = self.run_one_unit_time()
            end_queue_length_frequency[queue_length] += 1
            average_num_service += num_service
        average_num_service = average_num_service/num_runs
        end_queue_length_frequency = end_queue_length_frequency/float(num_runs)
        return (end_queue_length_frequency, average_num_service)


class JacksCarRental(object):
    '''
    this class captures the Jacks car rental problem setup
    '''
    def __init__(self,
                 max_num_car=20,
                 arrival_rate_loc1=3,
                 service_rate_loc1=3,
                 arrival_rate_loc2=2,
                 service_rate_loc2=4,
                 max_num_move_car=5):
        self.max_num_car = max_num_car
        self.arrival_rate_loc1 = arrival_rate_loc1
        self.service_rate_loc1 = service_rate_loc1
        self.arrival_rate_loc2 = arrival_rate_loc2
        self.service_rate_loc2 = service_rate_loc2
        self.max_num_move_car = max_num_move_car
        self.calc_trans_prob_and_reward()

    def calc_trans_prob_and_reward(self):
        '''
        this function calculates the transition probability from a morning state to a evening state,
        and the reward of a morning state.
        '''
        self.num_car_trans_prob_loc1 = np.zeros(shape=(self.max_num_car+1, self.max_num_car+1))
        self.num_car_trans_prob_loc2 = np.zeros(shape=(self.max_num_car+1, self.max_num_car+1))
        self.num_car_trans_reward_loc1 = np.zeros(shape=(self.max_num_car+1))
        self.num_car_trans_reward_loc2 = np.zeros(shape=(self.max_num_car+1))
        queue_loc1 = MM1NQueue(ini_num_pkt=0, max_num_pkt=self.max_num_car,
                               arrival_rate=self.arrival_rate_loc1,
                               service_rate=self.service_rate_loc1)
        queue_loc2 = MM1NQueue(ini_num_pkt=0, max_num_pkt=self.max_num_car,
                               arrival_rate=self.arrival_rate_loc2,
                               service_rate=self.service_rate_loc2)
        for ini_num_car in range(self.max_num_car+1):
            queue_loc1.reset_ini_num_pkt(ini_num_car)
            queue_loc2.reset_ini_num_pkt(ini_num_car)
            (self.num_car_trans_prob_loc1[ini_num_car],
             self.num_car_trans_reward_loc1[ini_num_car]) = queue_loc1.run_multiple_unit_slots()
            (self.num_car_trans_prob_loc2[ini_num_car],
             self.num_car_trans_reward_loc2[ini_num_car]) = queue_loc2.run_multiple_unit_slots()
        self.num_car_trans_reward_loc1 = 10 * self.num_car_trans_reward_loc1
        self.num_car_trans_reward_loc2 = 10 * self.num_car_trans_reward_loc2

    def value_iteration(self,
                        gamma=0.9,
                        num_iter_improvement=5):
        '''
        value iteration generator function
        '''
        policy_matrix = np.zeros(shape=(self.max_num_car+1, self.max_num_car+1), dtype=int)

        # Policy iteration
        for _ in range(num_iter_improvement):
            # policy evaluation
            value_matrix = np.zeros(shape=(self.max_num_car+1, self.max_num_car+1))
            self.policy_evaluation(value_matrix, policy_matrix, gamma)
            yield copy.deepcopy(value_matrix), copy.deepcopy(policy_matrix)
            self.policy_improvement(value_matrix, policy_matrix, gamma)

    def policy_iteration(self,
                         gamma=0.9,
                         num_iter_eval=100,
                         num_iter_improvement=5):
        '''
        policy iteration generator function
        '''
        policy_matrix = np.zeros(shape=(self.max_num_car+1, self.max_num_car+1), dtype=int)

        # Policy iteration
        for _ in range(num_iter_improvement):
            # policy evaluation
            value_matrix = np.zeros(shape=(self.max_num_car+1, self.max_num_car+1))
            for _ in range(num_iter_eval):
                self.policy_evaluation(value_matrix, policy_matrix, gamma)

            yield copy.deepcopy(value_matrix), copy.deepcopy(policy_matrix)
            self.policy_improvement(value_matrix, policy_matrix, gamma)

    def policy_evaluation(self, value_matrix, policy_matrix, gamma):
        '''
        policy evaluation
        '''
        value_matrix_old = copy.deepcopy(value_matrix)
        for i, j in product(range(self.max_num_car+1),
                            range(self.max_num_car+1)):
            l = i - policy_matrix[i, j]
            m = j + policy_matrix[i, j]
            prob_transition_matrix = \
            self.num_car_trans_prob_loc1[l].reshape((self.max_num_car+1, 1))*\
            self.num_car_trans_prob_loc2[m]
            value_matrix[i, j] = (self.num_car_trans_reward_loc1[l] +
                                  self.num_car_trans_reward_loc2[m] +
                                  gamma*sum(sum(prob_transition_matrix*value_matrix_old)) -
                                  abs(policy_matrix[i, j])*2)

    def policy_improvement(self, value_matrix, policy_matrix, gamma):
        '''
        greedy policy improvement
        '''
        for i, j in product(range(self.max_num_car+1), range(self.max_num_car+1)):
            action = 0
            max_reward = 0
            for potential_action in range(-self.max_num_move_car, self.max_num_move_car+1):
                l = i - potential_action
                m = j + potential_action
                if (l >= 0 and l <= self.max_num_car and
                        m >= 0  and m <= self.max_num_car):
                    prob_transition_matrix =\
                    self.num_car_trans_prob_loc1[l].reshape((self.max_num_car+1, 1))*\
                    self.num_car_trans_prob_loc2[m]
                    reward = (self.num_car_trans_reward_loc1[l] +
                              self.num_car_trans_reward_loc2[m] +
                              gamma*sum(sum(prob_transition_matrix*value_matrix)) -
                              abs(potential_action)*2)
                    if reward > max_reward:
                        action = potential_action
                        max_reward = reward
            policy_matrix[i, j] = action

# module testing code
if __name__ == '__main__':
    import time
    start_time = time.time()
    jacks_car_rental = JacksCarRental()
    for value_matrix, policy_matrix in jacks_car_rental.policy_iteration(num_iter_improvement=5):
        print(policy_matrix)

    print("--- %s seconds ---" % (time.time() - start_time))