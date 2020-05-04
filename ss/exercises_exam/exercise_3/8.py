from ss.stats_utils import two_sample_mannwhitneyu_test

data_1 = [26.2, 29.3, 31.3, 28.7, 27.4, 25.1, 26, 27.2, 27.5, 29.8, 32.6, 34.6]
data_2 = [25.3, 28.2, 29.2, 27.1, 26.8, 26.5, 30.7, 31.3, 26.3, 24.9]

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
