from itertools import combinations
from itertools import permutations


def sample_from_seven_distinct_letters():
    all_samples = ["".join(sample) for sample in combinations("ABCDEFG", 3)]
    print(all_samples)
    print(len(all_samples))


def permutation_of_drawing_marbles_from_sample(sample):
    all_perms = ["".join(perm) for perm in permutations(sample)]
    print(all_perms)
    print(f"Perms length {len(all_perms)} of sample {sample}")


if __name__ == "__main__":
    sample_from_seven_distinct_letters()
    permutation_of_drawing_marbles_from_sample("ABC")
