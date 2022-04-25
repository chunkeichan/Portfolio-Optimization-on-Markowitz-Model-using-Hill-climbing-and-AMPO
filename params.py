import pandas as pd
from numpy import asarray

# Input parameters here.

# General
risk_free_rate = 0.02
df = pd.read_csv("./data/SharePrices_modified.csv")
stocklist_raw = df.columns.tolist()
stocklist = stocklist_raw[1:]

# AMPO
bound = [0, 1]
max_iters = 500

# Hill Climbing
# define range for input
bounds = asarray([[-5, 5]])
# define the total iterations
n_iterations = max_iters
# define the maximum step size
step_size = 0.5

# For (1)saving the process data or (2)verification
input_sol = [0.2498929405645637, 6.496507323403164e-05, 0.12259369934482517, 0.0003648254296078391, 0.2499785644827348,
             0.03665222671165858, 0.09238220978512585, 6.532150754216844e-05, 0.0012148812783890303, 0.2467903658223189]
