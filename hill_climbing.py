import numpy as np
from numpy.random import randn
from numpy.random import rand


def hillclimbing(objective, bounds, n_iterations, step_size, dim):
    # generate an initial point
    sol = bounds[:, 0] + rand(dim) * (bounds[:, 1] - bounds[:, 0])
    solution = [(bounds[:, 0] + rand(dim) *
                 (bounds[:, 1] - bounds[:, 0]))[0] for i in range(10)]
    # evaluate the initial point
    solution_eval = objective(solution)
    # run the hill climb
    solutions = list()
    solutions.append(solution)
    for i in range(n_iterations):
        # take a step
        candidate = solution + np.abs(randn(dim)) * step_size

        # evaluate candidate point
        candidte_eval = objective(candidate)
        # check if we should keep the new point
        if candidte_eval <= solution_eval:
            # store the new point
            solution, solution_eval = candidate, candidte_eval
            # keep track of solutions
            solutions.append(solution)
            # report progress
            print('>%d f(%s) = %.5f' % (i, solution, solution_eval))

    solution = [np.abs(x) / sum(np.abs(solution)) for x in solution]

    return [solution, solution_eval, solutions]
