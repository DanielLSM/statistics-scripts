from ss.stats_utils import anova_one_way

method_a = [73, 77, 67, 71]
method_b = [91, 81, 87, 85]
method_c = [72, 77, 76, 79]

stat_tuple = anova_one_way(method_a, method_b, method_c)
F = stat_tuple[0]
p_value = stat_tuple[1]
alpha = 0.05
print("F:{}".format(F))
print("p_value:{}".format(p_value))
if p_value < alpha:
    print("H0 can be rejected")
else:
    print("H0 can not be rejected")