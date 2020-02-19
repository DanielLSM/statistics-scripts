import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats

######################################
# Exercise 4
######################################
n = 300
p = 63 / n
confidence = 0.95
interval = one_sample_prop_proportion(p, n, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
