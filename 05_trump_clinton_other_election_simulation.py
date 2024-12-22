'''
in Pennsylvania, Trump received 48.18%
Clinton received 47.46%
and other 100-48.18% - 47.46% of the 6,165,478 votes cast,
 this version of URN model uses 3 types of marbles in it, this is called multivariate hypergeometric
'''

import numpy as np
from scipy.stats import multivariate_hypergeom

proportions = np.array([.4818, .4746, 1 - (.4818 + .4746)])  # 0th is trump, 1 is clinton and others
n = 1_500  # sample size for elections polling in US
N = 6_165_478  # Total number of voters in pennsylvania

votes = np.trunc(N * proportions).astype(int)
print(f"votes: {votes}")


def trumps_advantage(actual_votes, sample_size):
    sample_votes = multivariate_hypergeom.rvs(actual_votes, sample_size)
    return (sample_votes[0] - sample_votes[1]) / sample_size


if __name__ == "__main__":
    simulations = [trumps_advantage(votes, n) for _ in range(100_000)]
    mean = np.mean(simulations)
    print(f"mean of trumps advantage {mean}");
