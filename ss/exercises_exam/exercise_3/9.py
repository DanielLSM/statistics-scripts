import math
from ss.stats_utils import confidence_interval, one_sample_prop_proportion, describe_stats
from ss.stats_utils import two_sample_population, two_sample_proportion, two_sample_population_from_data

salary = [118, 115, 122, 99, 106, 125, 102, 100, 92, 103, 113, 129]
piece_work = [115, 126, 113, 110, 135, 102, 124, 137, 108, 128]

confidence = 0.99
describe_stats(salary)
describe_stats(piece_work)
interval = two_sample_population_from_data(salary, piece_work, confidence)

print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(
    interval[0], interval[1], confidence * 100))
