import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import confidence_interval_from_data
data = [
    310, 222, 680, 299, 202, 525, 568, 447, 129, 406, 331, 644, 461, 204, 396, 684, 517, 322, 343,
    259, 526, 288, 330, 205, 294, 496, 366
]

confidence = .95
describe_stats(data)
interval = confidence_interval_from_data(data, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
