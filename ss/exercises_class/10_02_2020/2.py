import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats

######################################
# Exercise 2
######################################
n = 42
m = 680
s = 35
confidence = 0.99
interval = confidence_interval(m, s, n, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
