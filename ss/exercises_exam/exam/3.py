from ss.stats_utils import frequency_hypothesis_chisquare
from scipy.stats.distributions import chi2
import itertools

obs_less_5 = [25, 39]
obs_5_10 = [42, 40]
obs_more_10 = [33, 21]
f_expected = [1 / 2, 1 / 2]

categorical_obs = [obs_less_5, obs_5_10, obs_more_10]

assert round(sum(f_expected), 6) == 1.0

expected_less_5 = [round(sum(obs_less_5) * i, 2) for i in f_expected]
expected_5_10 = [round(sum(obs_5_10) * i, 2) for i in f_expected]
expected_more_10 = [round(sum(obs_more_10) * i, 2) for i in f_expected]

categorical_expected = [expected_less_5, expected_5_10, expected_more_10]

obs = list(itertools.chain(*categorical_obs))
expected = list(itertools.chain(*categorical_expected))

print("obs: {}".format(obs))
print("expected: {}".format(expected))
ddof = (len(categorical_obs) - 1) * (len(categorical_expected) - 1)
statistic = frequency_hypothesis_chisquare(obs, expected, ddof=ddof)
print("statistic is: {}".format(round(statistic[0], 2)))
crit_statistic = chi2.ppf(0.95, df=ddof)
print("degrees of freedom: {}".format(ddof))
print("For area=0.05, X is {}".format(round(crit_statistic, 2)))
if statistic[0] > crit_statistic:
    print("We can reject the hypothesis H0")
else:
    print("Hypothesis H0 can not be rejected")
