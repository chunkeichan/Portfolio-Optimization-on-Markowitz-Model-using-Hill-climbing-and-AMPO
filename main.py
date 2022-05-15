from ampo_test import ampoTest
import time
from params import stocklist, bound, max_iters, bounds, n_iterations, step_size, input_sol
from sharpe_ratio_function import findSharperatio, inputSharperatio, verifySharperatio
from hill_climbing import hillclimbing
from numpy.random import seed


def ampo(objective):
    print("Start time: %s" % time.strftime("%d/%m/%Y, %H:%M:%S"))

    best_solution = ampoTest(objective, len(
        stocklist), bound=bound, max_iters=max_iters)
    print('Best solution:' + str(best_solution))
    print('Best fitness:' + str(findSharperatio(best_solution)))

    print("End time: %s" % time.strftime("%d/%m/%Y, %H:%M:%S"))


def hillClimb(objective):
    print("Start time: %s" % time.strftime("%d/%m/%Y, %H:%M:%S"))

    # seed the pseudorandom number generator
    seed(5)
    best_solution, score, solutions = hillclimbing(
        objective, bounds, n_iterations, step_size, len(
            stocklist))
    print('Best solution:' + str(best_solution))
    print('Best fitness:' + str(findSharperatio(best_solution)))

    print("End time: %s" % time.strftime("%d/%m/%Y, %H:%M:%S"))


def getData(input_sol):
    value_sharperatio, value_return, value_risk = verifySharperatio(
        input_sol, rec=1)
    print("Sharpe Ratio, Return and Risk for the input solution are {}, {} and {} respectively.".format(
        value_sharperatio, value_return, value_risk))


if __name__ == "__main__":

    # Main

    # Selected objective function
    objective = inputSharperatio

    # 1 - Use AMPO to find the best proportions
    ampo(objective)

    # 2 - Use Hill Climbing to find the best proportions
    # hillClimb(objective)

    # 3 - Save the process data (if necessary)
    # getData(input_sol)

    # 4 - Verify if the sum of weighting is 100% (if necessary)
    # print("Total Percentage: %s%%" % (sum(input_sol)*100))
