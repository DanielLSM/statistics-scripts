from ss.stats_utils import two_sample_mannwhitneyu_test

data_1 = [51, 82, 47, 50, 38, 61, 56, 40, 45]
data_2 = [81, 80, 76, 66, 70, 60, 52, 88, 85]

statistic = two_sample_mannwhitneyu_test(data_1, data_2)
# interpret
# Reject H0 if U < 6 for 5% or 3 for 1%
stat_value = statistic[0]
p_value = statistic[1]
print("Statistic:{}".format(stat_value))
print("p value:{}".format(p_value))

alpha = 0.05
if p_value > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')

import math
from ss.stats_utils import describe_stats
from ss.stats_utils import two_sample_population_from_data

confidence = 0.99
describe_stats(data_1)
describe_stats(data_2)
interval = two_sample_population_from_data(data_1, data_2, confidence)

print("confidence interval is: [{:.2f} ; {:.2f}] with {:.2f}%".format(
    interval[0], interval[1], confidence * 100))