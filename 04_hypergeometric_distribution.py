import numpy as np

def hypergeometric_distribution():
    simulation_fast= np.random.hypergeometric(ngood=4,nbad=3,nsample=3,size=10_000)
    print(simulation_fast)
    unique_els, counts_els = np.unique(simulation_fast, return_counts=True)
    print(f"unique_els: {unique_els} and count_els: {counts_els}")


if __name__=="__main__":
    hypergeometric_distribution()