import numpy as np
import matplotlib.pyplot as plt
from ss.stats_utils import linear_regression

test_score_x = [65, 50, 55, 65, 55, 70, 65, 70, 55, 70, 50, 55]
chemestry_grade_y = [85, 74, 76, 90, 85, 87, 94, 98, 81, 91, 76, 74]

# a)
statistic = linear_regression(test_score_x, chemestry_grade_y)
m = statistic[0]
b = statistic[1]
r_value = statistic[2]
p_value = statistic[3]
standard_error_of_estimate = statistic[4]
print(statistic)
plt.title("Scatter Diagram")
plt.xlabel("test score x")
plt.ylabel("chemestry grade y")
plt.plot(test_score_x, chemestry_grade_y, 'o')
#https://blog.minitab.com/blog/adventures-in-statistics-2/how-to-interpret-regression-analysis-results-p-values-and-coefficients
# The p-value for each term tests the null hypothesis that the coefficient is equal to zero (no effect). A low p-value (< 0.05) indicates that you can reject the null hypothesis.
x = np.arange(min(test_score_x), max(test_score_x), 1)
y = m * x + b
plt.plot(x, y, '-')
alpha = 0.05
if p_value < alpha:
    print("H0 hypothesis that m=0 can be rejected")
else:
    print("H0 can not be rejected")
plt.show()
