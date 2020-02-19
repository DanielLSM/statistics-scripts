import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import confidence_interval_from_data

######################################
# Exercise 6
######################################
data = [25, 32, 30, 20, 15, 34, 36, 28, 22, 31, 27, 33, 26, 19, 21, 20, 26, 35, 17, 24]

confidence = .99
describe_stats(data)
interval = confidence_interval_from_data(data, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
