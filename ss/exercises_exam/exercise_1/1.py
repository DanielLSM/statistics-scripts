import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import confidence_interval_from_data

######################################
# Exercise 1
######################################
data = [25, 32, 30, 20, 15, 34, 36, 28, 22, 31, 27, 33, 26, 19, 21, 20, 26, 35, 17, 24]

confidence = .95
describe_stats(data)
interval = confidence_interval_from_data(data, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))
