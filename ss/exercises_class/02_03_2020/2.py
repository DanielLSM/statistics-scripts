from ss.stats_utils import frequency_hypothesis_chisquare
from scipy.stats.distributions import chi2

freq_expected = [0.3, 0.2, 0.2, 0.1, 0.1, 0.1]
assert round(sum(freq_expected), 6) == 1.0
cases = [152, 114, 106, 51, 43, 43]
expected = [round(i * sum(cases), 2) for i in freq_expected]
print("obs: {}".format(cases))
print("expected: {}".format(expected))
ddof = len(cases) - 1
statistic = frequency_hypothesis_chisquare(cases, expected, ddof=ddof)
print(statistic)
crit_statistic = chi2.ppf(0.95, df=ddof)
print("degrees of freedom: {}".format(ddof))
print("For area=0.05, X is {}".format(crit_statistic))
if statistic[0] > crit_statistic:
    print("We can reject the hypothesis H0")
else:
    print("Hypothesis H0 can not be rejected")
