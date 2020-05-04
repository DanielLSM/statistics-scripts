import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

brand_a = [
    61, 110, 249, 93, 19, 95, 20, 41, 91, 67, 37, 50, 114, 150, 98, 54, 107,
    60, 19, 32
]
brand_b = [3, 18, 35, 55, 60, 68, 75, 83, 99, 114, 115, 125, 133, 136, 247]

confidence = 0.95
describe_stats(brand_a)
describe_stats(brand_b)
interval = two_sample_population_from_data(brand_a, brand_b, confidence)

print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(
    interval[0], interval[1], confidence * 100))
