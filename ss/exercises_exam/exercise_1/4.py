import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

data_1 = [142, 136, 158, 145, 150, 148]
data_2 = [137, 140, 148, 147, 143, 140]

confidence = 0.9
interval = two_sample_population_from_data(data_1, data_2, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
