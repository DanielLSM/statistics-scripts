import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data
from ss.stats_utils import two_sample_dependant_from_data

data_1 = [
    2.35, 2.55, 1.95, 2.79, 3.21, 2.97, 3.44, 2.58, 2.66, 2.31, 3.43, 2.37,
    1.82, 2.98, 2.53
]
data_2 = [
    2, 1.71, 2.22, 2.71, 1.83, 2.14, 3.72, 2.10, 2.58, 1.32, 3.7, 1.59, 2.07,
    2.15, 2.05
]

confidence = 0.95
interval = two_sample_dependant_from_data(data_1, data_2, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(
    interval[0], interval[1], confidence * 100))
