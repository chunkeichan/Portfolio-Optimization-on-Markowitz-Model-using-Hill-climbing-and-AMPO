from ampo.ampo import AMPO
import numpy as np


def ampoTest(func, dim, bound, max_iters):
    algo = AMPO(func=func, dim=dim, bound=bound, pop=50, max_iters=max_iters,
                p_ld_ls=0.8, p_ls_ls=0.8, pr=0.6, w=0.1, r=0.9, show_info=True)
    best_solution, best_fitness, fitness = algo.run()
    best_solution = [np.abs(x) / sum(np.abs(best_solution))
                     for x in best_solution]
    return best_solution
