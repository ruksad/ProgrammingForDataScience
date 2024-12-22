import numpy as np

urn = ["b", "b", "b", "w", "w"]
print("Sample 1:", np.random.choice(urn,size=2,replace=False))
print("Sample 2:", np.random.choice(urn,size=2,replace=False))
print(np.__version__)
