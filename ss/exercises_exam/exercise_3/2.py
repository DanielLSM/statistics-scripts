import numpy as np
import matplotlib.pyplot as plt
from ss.stats_utils import linear_regression

mm_HG = [
    95, 90, 125, 105, 110, 105, 90, 90, 80, 110, 90, 105, 90, 110, 110, 140
]
ml = [
    274, 170, 352, 317, 171, 150, 245, 120, 190, 288, 205, 150, 175, 64, 276,
    318
]

# a)
statistic = linear_regression(mm_HG, ml)
m = statistic[0]
b = statistic[1]
r_value = statistic[2]
p_value = statistic[3]
standard_error_of_estimate = statistic[4]
print(statistic)
plt.title("Scatter Diagram")
plt.xlabel("Systolic Br")
plt.ylabel("Blood Loss")
plt.plot(mm_HG, ml, 'o')
#https://blog.minitab.com/blog/adventures-in-statistics-2/how-to-interpret-regression-analysis-results-p-values-and-coefficients
# The p-value for each term tests the null hypothesis that the coefficient is equal to zero (no effect). A low p-value (< 0.05) indicates that you can reject the null hypothesis.
x = np.arange(min(mm_HG), max(mm_HG), 1)
y = m * x + b
plt.plot(x, y, '-')
alpha = 0.05
if p_value < alpha:
    print("H0 hypothesis that m=0 can be rejected")
else:
    print("H0 can not be rejected")
plt.show()
