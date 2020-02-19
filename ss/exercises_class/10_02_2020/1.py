import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats

######################################
# Exercise 1
######################################
n = 100
m = 14.21
s = 6.87
confidence = 0.95
interval = confidence_interval(m, s, n, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
