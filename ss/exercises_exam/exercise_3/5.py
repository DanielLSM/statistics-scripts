import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

brand_a = [0.5, 0, 3.2, 1.4, 0.0, 1.0, 8.6, 2.9]
brand_b = [4.7, 6.2, 0.0, 10.5, 2.1, 0.8]

confidence = 0.95
describe_stats(brand_a)
describe_stats(brand_b)
interval = two_sample_population_from_data(brand_a, brand_b, confidence)

print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(
    interval[0], interval[1], confidence * 100))
