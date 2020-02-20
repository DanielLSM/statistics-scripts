import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats

######################################
# Exercise 8 equal to 2
######################################
n = 4063
p = 533 / n
confidence = 0.95
interval = one_sample_prop_proportion(p, n, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
