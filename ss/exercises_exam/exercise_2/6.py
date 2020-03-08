from ss.stats_utils import two_sample_mannwhitneyu_test

data_x = [38, 195, 56, 3, 51, 89]
data_y = [125, 73, 138, 35, 51, 190, 169]

statistic = two_sample_mannwhitneyu_test(data_x, data_y)
# interpret
# Reject H0 if U < 6 for 5% or 3 for 1%
alpha = 0.05
if statistic[1] > alpha:
    print('Same distribution (fail to reject H0)')
else:
    print('Different distribution (reject H0)')
