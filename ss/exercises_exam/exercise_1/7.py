import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

data_1 = [71, 75, 65, 69, 73, 66, 68, 71, 74, 68]
data_2 = [72, 77, 84, 78, 69, 70, 77, 73, 65, 75]

confidence = 0.95
describe_stats(data_1)
describe_stats(data_2)
interval = two_sample_population_from_data(data_1, data_2, confidence)
print("confidence interval is: {} with {}%".format(interval, confidence * 100))
