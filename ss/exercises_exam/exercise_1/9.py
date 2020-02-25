import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

data_1 = [14, 4, 10, 6, 3, 11, 12]
data_2 = [16, 17, 13, 12, 7, 16, 11, 8, 7]

confidence = 0.99
describe_stats(data_1)
describe_stats(data_2)
interval = two_sample_population_from_data(data_1, data_2, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))
