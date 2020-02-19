import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

data_1 = [12.5, 9.5, 13.5, 13.75, 12, 13.75, 12.5, 9.5, 12, 13.5, 12, 12]
data_2 = [9.5, 10.5, 9, 9.75, 10, 13, 10, 13.5, 10, 9.5, 10, 9.75]

confidence = 0.9
interval = two_sample_population_from_data(data_1, data_2, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
