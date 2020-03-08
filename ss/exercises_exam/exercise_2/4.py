import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data
from ss.stats_utils import two_sample_dependant_from_data

data_1 = [
    33, 31, 32, 30, 29, 29, 28, 29, 27, 28, 27, 26, 25, 25, 24, 24, 23, 23, 22, 221, 22, 21, 17, 16,
    16
]
data_2 = [
    27, 31, 29, 33, 31, 30, 30, 23, 30, 29, 26, 27, 24, 20, 25, 24, 32, 23, 24, 15, 24, 23, 18, 17,
    24
]

confidence = 0.95
interval = two_sample_dependant_from_data(data_1, data_2, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))
