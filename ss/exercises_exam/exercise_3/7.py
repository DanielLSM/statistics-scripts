import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data
from ss.stats_utils import two_sample_dependant_from_data

data_1 = [24.3, 26.2, 23.8, 27.9, 21.8, 23.9]
data_2 = [24, 26.1, 24, 27.3, 21.1, 24.2]

confidence = 0.95
interval = two_sample_dependant_from_data(data_1, data_2, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(
    interval[0], interval[1], confidence * 100))
