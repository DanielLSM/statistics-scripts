from ss.stats_utils import two_sample_mannwhitneyu_test

data_x = [38, 195, 56, 3, 51, 89]
data_y = [125, 73, 138, 35, 51, 190, 169]

output = two_sample_mannwhitneyu_test(data_x, data_y)
print(output)