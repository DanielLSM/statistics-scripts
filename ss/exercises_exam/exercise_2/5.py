import math
from ss.stats_utils import two_sample_proportion

n_A = 100
p_A = 32 / n_A

n_B = 100
p_B = 24 / n_B

confidence = 0.99
print("Proportion A: {}".format(p_A))
print("Proportion B: {}".format(p_B))

interval = two_sample_proportion(p_A, n_A, p_B, n_B, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))
