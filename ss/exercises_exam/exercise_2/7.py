import numpy as np
import matplotlib.pyplot as plt
from ss.stats_utils import linear_regression

data_IQ = [99, 110, 141, 108, 123, 129, 132, 88, 101, 105, 97, 96, 118, 113]
data_score = [54, 70, 100, 61, 83, 86, 98, 51, 64, 68, 52, 55, 71, 76]

# a)
statistic = linear_regression(data_IQ, data_score)
m = statistic[0]
b = statistic[1]
r_value = statistic[2]
p_value = statistic[3]
standard_error_of_estimate = statistic[4]
print(statistic)
plt.title("Scatter Diagram")
plt.xlabel("IQ")
plt.ylabel("Score")
plt.plot(data_IQ, data_score, 'o')
#https://blog.minitab.com/blog/adventures-in-statistics-2/how-to-interpret-regression-analysis-results-p-values-and-coefficients
# The p-value for each term tests the null hypothesis that the coefficient is equal to zero (no effect). A low p-value (< 0.05) indicates that you can reject the null hypothesis.
x = np.arange(min(data_IQ), max(data_IQ), 1)
y = m * x + b
plt.plot(x, y, '-')
alpha = 0.05
if p_value < alpha:
    print("H0 hypothesis that m=0 can be rejected")
else:
    print("H0 can not be rejected")
plt.show()
