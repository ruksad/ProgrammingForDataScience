'''
in Pennsylvania, Trump received 48.18%
Clinton received 47.46%
and other 100-48.18% - 47.46% of the 6,165,478 votes cast,
 this version of URN model uses 3 types of marbles in it, this is called multivariate hypergeometric
'''

import numpy as np
from scipy.stats import multivariate_hypergeom

proportions= np.array([.4818, .4746, 1-(.4818+.4746)])
n= 1_500 # sample size for elections polling in US
N= 6_165_478 # Total number of voters in pennsylvania

votes = np.trunc(N * proportions).astype(int)
print(f"votes: {votes}")
