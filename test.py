import numpy as np
from biffron import biffron_decision

corr = np.array([
    [1.0, 0.2, 0.1],
    [0.2, 1.0, 0.15],
    [0.1, 0.15, 1.0],
])

res = biffron_decision(corr, mu=2.0)

print(res)
