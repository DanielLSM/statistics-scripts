from ss.stats_utils import frequency_hypothesis_chisquare
from scipy.stats.distributions import chi2
import itertools

obs_1_low = [6, 12, 32]
obs_2_average = [33, 61, 18]
obs_3_high = [13, 15, 0]
f_expected = [1 / 3, 1 / 3, 1 / 3]

categorical_obs = [obs_1_low, obs_2_average, obs_3_high]

assert round(sum(f_expected), 6) == 1.0

expected_1_low = [round(sum(obs_1_low) * i, 2) for i in f_expected]
expected_2_average = [round(sum(obs_2_average) * i, 2) for i in f_expected]
expected_3_high = [round(sum(obs_3_high) * i, 2) for i in f_expected]

categorical_expected = [expected_1_low, expected_2_average, expected_3_high]

obs = list(itertools.chain(*categorical_obs))
expected = list(itertools.chain(*categorical_expected))

print("obs: {}".format(obs))
print("expected: {}".format(expected))
ddof = (len(categorical_obs) - 1) * (len(categorical_expected) - 1)
statistic = frequency_hypothesis_chisquare(obs, expected, ddof=ddof)
print("statistic is: {}".format(round(statistic[0], 2)))
crit_statistic = chi2.ppf(0.99, df=ddof)
print("degrees of freedom: {}".format(ddof))
print("For area=0.05, X is {}".format(round(crit_statistic, 2)))
if statistic[0] > crit_statistic:
    print("We can reject the hypothesis H0")
else:
    print("Hypothesis H0 can not be rejected")
