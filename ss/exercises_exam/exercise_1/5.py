import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

data_1 = [81, 95, 88, 85, 84, 90]
data_2 = [85, 94, 91, 92, 83, 90]

confidence = 0.95
interval = two_sample_population_from_data(data_1, data_2, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))
