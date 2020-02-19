import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import confidence_interval_from_data

######################################
# Exercise 6
######################################
data = [
    0.55, 0.56, 0.52, 0.59, 0.51, 0.50, \
    0.42, 0.41, 0.37, 0.22, 0.24, 0.41, \
    0.49, 0.59, 0.75, 0.65, 0.63, 0.61, \
    0.72, 0.77, 0.76, 0.39, 0.26, 0.68, \
    0.30, 0.32, 0.44, 0.61, 0.54, 0.47
]
confidence = .99
describe_stats(data)
interval = confidence_interval_from_data(data, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
