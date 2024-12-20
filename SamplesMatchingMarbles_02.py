import numpy as np


def portion_of_sample():
    sample_size = 10000
    urn = ["b", "b", "b", "w", "w"]

    sample = [np.random.choice(urn, size=2, replace=False) for i in range(sample_size)]
    is_matching = [marble1 == marble2 for marble1, marble2 in sample]
    print(f"Portion of samples with matching marbles: {np.mean(is_matching)}")


if __name__ == "__main__":
    portion_of_sample()
