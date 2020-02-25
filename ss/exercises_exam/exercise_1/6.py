import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

data_1 = [21, 24, 22, 23, 25, 23, 26, 20]
data_2 = [23, 27, 20, 22, 26, 20, 27, 19]

confidence = 0.95
describe_stats(data_1)
describe_stats(data_2)
interval = two_sample_population_from_data(data_1, data_2, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))

# squared_sum = 0
# for _ in data_1:
#     squared_sum += (_ - 23)**2

# squared_sum = math.sqrt(squared_sum / (len(data_1) - 1))

# print(squared_sum)
