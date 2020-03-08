import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data
from ss.stats_utils import two_sample_dependant_from_data

before = [38, 11, 34, 25, 17, 38, 12, 27, 32, 29]
after = [45, 24, 41, 39, 30, 44, 30, 39, 40, 41]

# dependant since it is the same 10 participants
confidence = 0.95
interval = two_sample_dependant_from_data(before, after, confidence)
print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(interval[0], interval[1],
                                                                      confidence * 100))
