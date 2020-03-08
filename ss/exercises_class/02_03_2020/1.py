from ss.stats_utils import frequency_hypothesis_chisquare
from scipy.stats.distributions import chi2

cases = [6, 20, 35, 41, 48]
# freq_cases = [i / sum(cases) for i in cases]
# freq_exp = [1 / len(cases) for i in cases]
ddof = len(cases) - 1
statistic = frequency_hypothesis_chisquare(cases, None, ddof)
crit_statistic = chi2.ppf(0.95, df=ddof)
print(statistic)
print("degrees of freedom: {}".format(ddof))
print("For area=0.05, X is {}".format(crit_statistic))
if statistic[0] > crit_statistic:
    print("We can reject the hypothesis H0")
else:
    print("Hypothesis H0 can not be rejected")
